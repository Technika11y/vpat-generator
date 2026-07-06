"""vpat-generator <check|report> <results.json> [--product NAME]

`check`  validates the results (exit 1 on errors); `report` renders a Markdown ACR."""
import argparse
import json
import sys

from .report import validate, has_errors, render


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(prog="vpat-generator")
    parser.add_argument("command", choices=["check", "report"])
    parser.add_argument("results", help="criteria results JSON (list of {id, conformance, remarks})")
    parser.add_argument("--product", default="<product>", help="product name for the report header")
    args = parser.parse_args(argv)

    with open(args.results) as fh:
        results = json.load(fh)

    findings = validate(results)
    for f in findings:
        print(f"{f['severity'].upper():5} {f['message']}", file=sys.stderr)

    if args.command == "check":
        return 1 if has_errors(findings) else 0

    # report: refuse to render from invalid input (fail closed)
    if has_errors(findings):
        print("refusing to render: results have errors", file=sys.stderr)
        return 1
    print(render(results, product=args.product))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
