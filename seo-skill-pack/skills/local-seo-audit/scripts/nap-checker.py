#!/usr/bin/env python3
"""
NAP (Name, Address, Phone) Consistency Checker

Compares NAP data across multiple sources and flags inconsistencies.

Usage:
    python nap-checker.py --input nap-data.json
    python nap-checker.py --name "Business Name" --address "123 Main St" --phone "555-123-4567"

Input JSON format:
[
  {
    "source": "Website",
    "name": "Bright Smile Dental",
    "address": "123 Main St, Suite 100, Austin, TX 78701",
    "phone": "(512) 555-1234",
    "website": "https://brightsmile.com"
  },
  ...
]
"""

import json
import re
import sys
import argparse
from typing import Optional


def normalize_phone(phone: str) -> str:
    """Strip a phone number down to digits only."""
    digits = re.sub(r'\D', '', phone)
    if digits.startswith('1') and len(digits) == 11:
        digits = digits[1:]
    return digits


def normalize_address(address: str) -> str:
    """Normalize common address abbreviations and formatting."""
    addr = address.lower().strip()

    replacements = {
        r'\bstreet\b': 'st',
        r'\bavenue\b': 'ave',
        r'\bboulevard\b': 'blvd',
        r'\bdrive\b': 'dr',
        r'\blane\b': 'ln',
        r'\broad\b': 'rd',
        r'\bcourt\b': 'ct',
        r'\bplace\b': 'pl',
        r'\bcircle\b': 'cir',
        r'\bparkway\b': 'pkwy',
        r'\bhighway\b': 'hwy',
        r'\bsuite\b': 'ste',
        r'\bapartment\b': 'apt',
        r'\bbuilding\b': 'bldg',
        r'\bfloor\b': 'fl',
        r'\bnorth\b': 'n',
        r'\bsouth\b': 's',
        r'\beast\b': 'e',
        r'\bwest\b': 'w',
        r'\bnortheast\b': 'ne',
        r'\bnorthwest\b': 'nw',
        r'\bsoutheast\b': 'se',
        r'\bsouthwest\b': 'sw',
    }

    for pattern, replacement in replacements.items():
        addr = re.sub(pattern, replacement, addr)

    # Remove extra whitespace, commas, periods
    addr = re.sub(r'[.,#]', '', addr)
    addr = re.sub(r'\s+', ' ', addr)
    return addr.strip()


def normalize_name(name: str) -> str:
    """Normalize a business name for comparison."""
    n = name.lower().strip()
    # Remove common suffixes
    n = re.sub(r'\b(llc|inc|ltd|corp|co|company)\b\.?', '', n)
    # Remove punctuation
    n = re.sub(r'[.,\'-]', '', n)
    n = re.sub(r'\s+', ' ', n)
    return n.strip()


def check_consistency(entries: list[dict]) -> dict:
    """Check NAP consistency across all entries and return a report."""
    if not entries:
        return {"error": "No entries provided"}

    report = {
        "total_sources": len(entries),
        "name_variations": [],
        "address_variations": [],
        "phone_variations": [],
        "website_variations": [],
        "inconsistencies": [],
        "consistency_score": 0,
    }

    # Collect normalized values
    names = {}
    addresses = {}
    phones = {}
    websites = {}

    for entry in entries:
        source = entry.get("source", "Unknown")

        if "name" in entry and entry["name"]:
            norm = normalize_name(entry["name"])
            names.setdefault(norm, []).append({"source": source, "original": entry["name"]})

        if "address" in entry and entry["address"]:
            norm = normalize_address(entry["address"])
            addresses.setdefault(norm, []).append({"source": source, "original": entry["address"]})

        if "phone" in entry and entry["phone"]:
            norm = normalize_phone(entry["phone"])
            phones.setdefault(norm, []).append({"source": source, "original": entry["phone"]})

        if "website" in entry and entry["website"]:
            url = entry["website"].lower().rstrip("/")
            url = re.sub(r'^https?://(www\.)?', '', url)
            websites.setdefault(url, []).append({"source": source, "original": entry["website"]})

    # Analyze variations
    checks_total = 0
    checks_passed = 0

    for field, variations, label in [
        (names, report["name_variations"], "Name"),
        (addresses, report["address_variations"], "Address"),
        (phones, report["phone_variations"], "Phone"),
        (websites, report["website_variations"], "Website"),
    ]:
        checks_total += 1
        if len(variations) <= 1:
            checks_passed += 1
        else:
            for norm_val, sources in variations.items():
                for s in sources:
                    field.append(s)
            # Record the inconsistency
            report["inconsistencies"].append({
                "field": label,
                "variation_count": len(variations),
                "details": [
                    {"normalized": k, "sources": [s["source"] for s in v], "original_values": [s["original"] for s in v]}
                    for k, v in variations.items()
                ]
            })

    report["consistency_score"] = round((checks_passed / checks_total * 100) if checks_total > 0 else 0)

    return report


def format_report(report: dict) -> str:
    """Format the consistency report as readable text."""
    lines = []
    lines.append("=" * 60)
    lines.append("NAP CONSISTENCY REPORT")
    lines.append("=" * 60)
    lines.append(f"\nSources checked: {report['total_sources']}")
    lines.append(f"Consistency score: {report['consistency_score']}%\n")

    if not report["inconsistencies"]:
        lines.append("ALL CONSISTENT - No NAP variations found across sources.")
    else:
        lines.append(f"INCONSISTENCIES FOUND: {len(report['inconsistencies'])} field(s)\n")
        for issue in report["inconsistencies"]:
            lines.append(f"--- {issue['field']} ({issue['variation_count']} variations) ---")
            for detail in issue["details"]:
                lines.append(f"  Normalized: '{detail['normalized']}'")
                for i, src in enumerate(detail["sources"]):
                    lines.append(f"    - {src}: \"{detail['original_values'][i]}\"")
            lines.append("")

    lines.append("=" * 60)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Check NAP consistency across sources")
    parser.add_argument("--input", "-i", help="JSON file with NAP data")
    parser.add_argument("--name", help="Reference business name")
    parser.add_argument("--address", help="Reference address")
    parser.add_argument("--phone", help="Reference phone")
    parser.add_argument("--json-output", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.input:
        with open(args.input) as f:
            entries = json.load(f)
    elif args.name or args.address or args.phone:
        entries = [{"source": "Reference", "name": args.name or "", "address": args.address or "", "phone": args.phone or ""}]
        print("Note: Only reference entry provided. Add more sources to the JSON file for comparison.")
    else:
        # Read from stdin
        data = sys.stdin.read()
        if data.strip():
            entries = json.loads(data)
        else:
            parser.print_help()
            sys.exit(1)

    report = check_consistency(entries)

    if args.json_output:
        print(json.dumps(report, indent=2))
    else:
        print(format_report(report))


if __name__ == "__main__":
    main()
