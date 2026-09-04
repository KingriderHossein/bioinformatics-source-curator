#!/usr/bin/env python3
"""Validate an exported 02_SOURCE_REGISTRY CSV against protocol 1.0.0."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from urllib.parse import urlsplit, urlunsplit

VERSION = "1.0.0"

REQUIRED = [
    "source_id", "domain_id", "source_type", "source_name", "official_url",
    "source_role", "monitoring_method", "monitoring_endpoint",
    "authority_score", "relevance_score", "activity_score",
    "primariness_score", "monitorability_score", "total_score", "priority",
    "approved_for_radar", "status", "last_verified",
]

PREPRINT_HOSTS = {
    "biorxiv.org", "www.biorxiv.org", "medrxiv.org", "www.medrxiv.org",
    "arxiv.org", "www.arxiv.org",
}


def norm_url(value: str) -> str:
    value = (value or "").strip()
    if not value:
        return ""
    parts = urlsplit(value)
    host = parts.netloc.lower()
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower() or "https", host, path, "", ""))


def expected_priority(total: int) -> str:
    if total >= 21:
        return "A"
    if total >= 16:
        return "B"
    if total >= 11:
        return "C"
    return "REJECT"


def as_bool(value: str) -> bool:
    return (value or "").strip().upper() in {"TRUE", "YES", "1", "Y"}


def validate(path: str) -> list[str]:
    errors: list[str] = []
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        headers = reader.fieldnames or []
        missing = [c for c in REQUIRED if c not in headers]
        if missing:
            return [f"Missing required columns: {', '.join(missing)}"]
        rows = list(reader)

    ids = [r["source_id"].strip() for r in rows if r["source_id"].strip()]
    for value, count in Counter(ids).items():
        if count > 1:
            errors.append(f"Duplicate source_id: {value} ({count} rows)")

    urls = [norm_url(r["official_url"]) for r in rows if norm_url(r["official_url"])]
    for value, count in Counter(urls).items():
        if count > 1:
            errors.append(f"Duplicate canonical official_url: {value} ({count} rows)")

    score_cols = [
        "authority_score", "relevance_score", "activity_score",
        "primariness_score", "monitorability_score",
    ]

    for i, row in enumerate(rows, start=2):
        sid = row["source_id"].strip() or f"row {i}"
        try:
            scores = [int(row[c]) for c in score_cols]
            if any(s < 0 or s > 5 for s in scores):
                errors.append(f"{sid}: score outside 0..5")
                continue
            total = sum(scores)
            recorded_total = int(row["total_score"])
        except ValueError:
            errors.append(f"{sid}: non-integer score/total")
            continue

        if total != recorded_total:
            errors.append(f"{sid}: total_score={recorded_total}, expected {total}")

        exp = expected_priority(total)
        recorded_priority = row["priority"].strip().upper()
        if recorded_priority != exp and row["status"].strip().upper() == "ACTIVE":
            errors.append(f"{sid}: priority={recorded_priority}, expected {exp}")

        host = urlsplit(row["official_url"].strip()).netloc.lower()
        if as_bool(row["approved_for_radar"]) and host in PREPRINT_HOSTS:
            errors.append(f"{sid}: preprint host approved_for_radar ({host})")

        if as_bool(row["approved_for_radar"]):
            if row["status"].strip().upper() != "ACTIVE":
                errors.append(f"{sid}: approved_for_radar but status is not ACTIVE")
            if recorded_priority not in {"A", "B"}:
                errors.append(f"{sid}: approved_for_radar but priority is not A/B")
            if not row["monitoring_method"].strip() or not row["monitoring_endpoint"].strip():
                errors.append(f"{sid}: approved_for_radar without monitoring method/endpoint")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path")
    parser.add_argument("--version", action="version", version=VERSION)
    args = parser.parse_args()
    errors = validate(args.csv_path)
    if errors:
        print(f"FAILED: {len(errors)} issue(s)")
        for err in errors:
            print(f"- {err}")
        return 1
    print("OK: registry CSV passed protocol 1.0.0 validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
