#!/usr/bin/env python3
"""Key-parity and placeholder check for i18n files (no dependencies)."""
import json, re, sys, pathlib

HERE = pathlib.Path(__file__).parent
EN = json.loads((HERE / "en.json").read_text(encoding="utf-8"))
PLACEHOLDER = re.compile(r"\{[a-z]+\}")
ok = True
for path in sorted(HERE.glob("*.json")):
    if path.name == "en.json":
        continue
    data = json.loads(path.read_text(encoding="utf-8"))
    problems = []
    missing = [k for k in EN if k not in data]
    extra = [k for k in data if k not in EN]
    if missing:
        problems.append(f"missing keys: {missing[:8]}{'...' if len(missing) > 8 else ''}")
    if extra:
        problems.append(f"unknown keys: {extra[:8]}{'...' if len(extra) > 8 else ''}")
    for k in EN:
        if k not in data:
            continue
        for a, b in ((EN[k], data[k]),):
            if isinstance(a, list) or isinstance(b, list):
                if not (isinstance(a, list) and isinstance(b, list) and len(a) == len(b)):
                    problems.append(f"{k}: array length mismatch")
                continue
            pa, pb = sorted(PLACEHOLDER.findall(str(a))), sorted(PLACEHOLDER.findall(str(b)))
            if pa != pb:
                problems.append(f"{k}: placeholders {pa} vs {pb}")
    if problems:
        ok = False
        print(f"FAIL {path.name}")
        for p in problems:
            print(f"  - {p}")
    else:
        print(f"PARITY OK {path.name} ({len(data)} keys)")
sys.exit(0 if ok else 1)
