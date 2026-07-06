"""Validate criteria results and render an Accessibility Conformance Report (ACR / VPAT-style).

Pure functions over a results list, so the judgment is unit-testable without any I/O.
"""
from .catalog import CRITERIA, CONFORMANCE_LEVELS


def _f(severity, message):
    return {"severity": severity, "message": message}


def validate(results):
    """Check a list of {id, conformance, remarks} results against the catalog."""
    findings = []
    seen = set()

    for r in results:
        cid = r.get("id")
        seen.add(cid)
        if cid not in CRITERIA:
            findings.append(_f("error", f'unknown criterion "{cid}" (not in the WCAG 2.2 catalog)'))
        level = r.get("conformance")
        if level not in CONFORMANCE_LEVELS:
            findings.append(_f("error", f'criterion {cid}: invalid conformance level "{level}"'))
        # A claim of a gap without explanation is not a usable ACR entry.
        if level in ("Partially Supports", "Does Not Support") and not r.get("remarks"):
            findings.append(_f("warn", f'criterion {cid}: "{level}" should include remarks explaining the gap'))

    for cid in CRITERIA:
        if cid not in seen:
            findings.append(_f("warn", f'criterion {cid} ({CRITERIA[cid]["title"]}) not evaluated'))

    return findings


def has_errors(findings):
    return any(x["severity"] == "error" for x in findings)


def render(results, product="<product>"):
    """Render a Markdown ACR covering every catalog criterion (unevaluated ones are marked)."""
    by_id = {r.get("id"): r for r in results}
    lines = [
        f"# Accessibility Conformance Report — {product}",
        "",
        "Based on WCAG 2.2. Conformance: Supports / Partially Supports / Does Not Support / Not Applicable.",
        "",
        "| Criterion | Level | Conformance | Remarks |",
        "|---|---|---|---|",
    ]
    for cid, meta in CRITERIA.items():
        r = by_id.get(cid)
        conf = r.get("conformance", "Not Evaluated") if r else "Not Evaluated"
        remarks = (r.get("remarks", "") if r else "").replace("|", "\\|")
        lines.append(f"| {cid} {meta['title']} | {meta['level']} | {conf} | {remarks} |")
    return "\n".join(lines) + "\n"
