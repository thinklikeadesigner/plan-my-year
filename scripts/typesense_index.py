"""Parse plan-my-year flat files and upsert documents into Typesense."""

from __future__ import annotations

import csv
import glob
import os
import re
import sys

import typesense

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

client = typesense.Client({
    "api_key": "plan-my-year-dev",
    "nodes": [{"host": "localhost", "port": "8108", "protocol": "http"}],
    "connection_timeout_seconds": 30,
})

collection = client.collections["memory"]


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------

def parse_tracker() -> list[dict]:
    path = os.path.join(ROOT, "tracker.csv")
    if not os.path.exists(path):
        return []
    docs = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row.get("date", "").strip()
            if not date:
                continue
            parts = []
            for key, val in row.items():
                if key == "date" or not val or not val.strip():
                    continue
                parts.append(f"{key}: {val.strip()}")
            content = f"Date: {date}. " + ". ".join(parts)
            tags = ["tracker"]
            if row.get("notes"):
                tags.append("notes")
            docs.append({
                "id": f"tracker-{date}",
                "type": "tracker",
                "title": f"Tracker — {date}",
                "content": content,
                "date": date,
                "tags": tags,
                "source_file": "tracker.csv",
            })
    return docs


def parse_stories() -> list[dict]:
    path = os.path.join(ROOT, "stories.md")
    if not os.path.exists(path):
        return []
    with open(path) as f:
        text = f.read()
    blocks = re.split(r"(?=^## Story \d+)", text, flags=re.MULTILINE)
    docs = []
    for block in blocks:
        m = re.match(r"## Story \d+:\s*(.+)", block)
        if not m:
            continue
        title = m.group(1).strip()
        slug = slugify(title)
        docs.append({
            "id": f"story-{slug}",
            "type": "story",
            "title": title,
            "content": block.strip(),
            "date": "",
            "tags": ["story", "behavioral"],
            "source_file": "stories.md",
        })
    return docs


def parse_contacts() -> list[dict]:
    path = os.path.join(ROOT, "contacts.md")
    if not os.path.exists(path):
        return []
    with open(path) as f:
        text = f.read()
    docs = []
    # Match the Active Contacts table rows (skip header + separator)
    in_table = False
    for line in text.splitlines():
        if "| Name |" in line:
            in_table = True
            continue
        if in_table and line.startswith("|---"):
            continue
        if in_table and line.startswith("|"):
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) >= 7:
                name, company, role, source, status, last_touch, next_action = cols[:7]
                notes = cols[7] if len(cols) > 7 else ""
                content = (
                    f"{name} at {company}. Role: {role}. "
                    f"Source: {source}. Status: {status}. "
                    f"Last touch: {last_touch}. Next action: {next_action}. "
                    f"Notes: {notes}"
                )
                slug = slugify(name) or slugify(company)
                docs.append({
                    "id": f"contact-{slug}",
                    "type": "contact",
                    "title": f"{name} — {company}",
                    "content": content,
                    "date": "",
                    "tags": ["contact", "networking"],
                    "source_file": "contacts.md",
                })
        elif in_table and not line.startswith("|"):
            in_table = False
    return docs


def parse_markdown_file(path: str, doc_type: str, id_prefix: str) -> dict | None:
    if not os.path.exists(path):
        return None
    with open(path) as f:
        content = f.read()
    basename = os.path.basename(path).replace(".md", "")
    slug = slugify(basename)
    # Try to extract a date from the filename
    date_match = re.search(r"(\d{4})", basename)
    date = date_match.group(1) if date_match else ""
    return {
        "id": f"{id_prefix}-{slug}",
        "type": doc_type,
        "title": basename,
        "content": content,
        "date": date,
        "tags": [doc_type],
        "source_file": os.path.basename(path),
    }


def parse_weekly_plans() -> list[dict]:
    docs = []
    for path in sorted(glob.glob(os.path.join(ROOT, "week-*.md"))):
        doc = parse_markdown_file(path, "weekly_plan", "week")
        if doc:
            docs.append(doc)
    return docs


def parse_monthly_plans() -> list[dict]:
    docs = []
    # Match patterns like feb-2026.md
    for path in sorted(glob.glob(os.path.join(ROOT, "*-202*.md"))):
        basename = os.path.basename(path)
        # Skip files that are weekly plans or other non-monthly files
        if basename.startswith("week-"):
            continue
        doc = parse_markdown_file(path, "monthly_plan", "monthly")
        if doc:
            docs.append(doc)
    return docs


def parse_quarterly_plans() -> list[dict]:
    docs = []
    for path in sorted(glob.glob(os.path.join(ROOT, "q[0-9]*-*.md"))):
        doc = parse_markdown_file(path, "quarterly_plan", "quarterly")
        if doc:
            docs.append(doc)
    return docs


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    try:
        collection.retrieve()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        print("Run typesense_setup.py first, or start Typesense with: docker compose up -d", file=sys.stderr)
        sys.exit(1)

    all_docs = []
    sources = [
        ("tracker.csv", parse_tracker),
        ("stories.md", parse_stories),
        ("contacts.md", parse_contacts),
        ("week-*.md", parse_weekly_plans),
        ("*-202*.md", parse_monthly_plans),
        ("q*-*.md", parse_quarterly_plans),
    ]

    for label, parser in sources:
        docs = parser()
        print(f"  {label}: {len(docs)} documents")
        all_docs.extend(docs)

    print(f"\nUpserting {len(all_docs)} documents...")
    success = 0
    for doc in all_docs:
        try:
            collection.documents.upsert(doc)
            success += 1
        except Exception as e:
            print(f"  Failed to upsert {doc['id']}: {e}", file=sys.stderr)

    print(f"Done. {success}/{len(all_docs)} documents indexed.")


if __name__ == "__main__":
    main()
