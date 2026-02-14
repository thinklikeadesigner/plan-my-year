"""Search the Typesense 'memory' collection with hybrid semantic + full-text search."""

from __future__ import annotations

import argparse
import sys

import typesense

client = typesense.Client({
    "api_key": "plan-my-year-dev",
    "nodes": [{"host": "localhost", "port": "8108", "protocol": "http"}],
    "connection_timeout_seconds": 30,
})


def search(query: str, doc_type: str | None = None, limit: int = 5):
    params = {
        "q": query,
        "query_by": "embedding,content,title",
        "vector_query": "embedding:([], alpha: 0.5)",
        "prefix": "false",
        "per_page": limit,
        "exclude_fields": "embedding",
    }
    if doc_type:
        params["filter_by"] = f"type:={doc_type}"

    try:
        results = client.collections["memory"].documents.search(params)
    except Exception as e:
        err = str(e)
        if "ECONNREFUSED" in err or "Connection" in err:
            print("Typesense not running. Start with: docker compose up -d", file=sys.stderr)
        else:
            print(f"Search error: {e}", file=sys.stderr)
        sys.exit(1)

    hits = results.get("hits", [])
    if not hits:
        print("No results found.")
        return

    print(f"Found {len(hits)} results for: {query}\n")
    for i, hit in enumerate(hits, 1):
        doc = hit["document"]
        snippet = doc["content"][:200].replace("\n", " ")
        if len(doc["content"]) > 200:
            snippet += "..."
        print(f"{i}. [{doc['type']}] {doc['title']}")
        if doc.get("date"):
            print(f"   Date: {doc['date']}")
        print(f"   Source: {doc['source_file']}")
        print(f"   {snippet}")
        print()


def main():
    parser = argparse.ArgumentParser(description="Search plan-my-year memory")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--type", dest="doc_type", help="Filter by type: tracker, weekly_plan, monthly_plan, quarterly_plan, story, contact")
    parser.add_argument("--limit", type=int, default=5, help="Max results (default: 5)")
    args = parser.parse_args()
    search(args.query, args.doc_type, args.limit)


if __name__ == "__main__":
    main()
