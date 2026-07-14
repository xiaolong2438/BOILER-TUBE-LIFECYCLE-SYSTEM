#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import sys


def find_id(node) -> str:
    if isinstance(node, dict):
        for key in ("uuid", "database_id", "id"):
            value = node.get(key)
            if value:
                return str(value)
        for value in node.values():
            found = find_id(value)
            if found:
                return found
    elif isinstance(node, list):
        for value in node:
            found = find_id(value)
            if found:
                return found
    return ""


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: resolve_d1_id.py <json-file>", file=sys.stderr)
        return 1
    path = pathlib.Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    result = find_id(data)
    if not result:
        print("Could not resolve D1 database id.", file=sys.stderr)
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
