"""Create the Typesense 'memory' collection for plan-my-year."""

import sys
import typesense
from typesense.exceptions import ObjectAlreadyExists

client = typesense.Client({
    "api_key": "plan-my-year-dev",
    "nodes": [{"host": "localhost", "port": "8108", "protocol": "http"}],
    "connection_timeout_seconds": 30,
})

schema = {
    "name": "memory",
    "fields": [
        {"name": "type", "type": "string", "facet": True},
        {"name": "title", "type": "string"},
        {"name": "content", "type": "string"},
        {"name": "date", "type": "string", "sort": True},
        {"name": "tags", "type": "string[]", "facet": True},
        {"name": "source_file", "type": "string", "facet": True},
        {
            "name": "embedding",
            "type": "float[]",
            "embed": {
                "from": ["content"],
                "model_config": {
                    "model_name": "ts/all-MiniLM-L12-v2",
                },
            },
        },
    ],
}


def main():
    try:
        client.collections.create(schema)
        print("Created 'memory' collection.")
    except ObjectAlreadyExists:
        print("'memory' collection already exists — dropping and recreating.")
        client.collections["memory"].delete()
        client.collections.create(schema)
        print("Recreated 'memory' collection.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if "ECONNREFUSED" in str(e) or "Connection" in str(e):
            print("Typesense not running. Start with: docker compose up -d", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
