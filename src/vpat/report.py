"""Validate criteria results and render an Accessibility Conformance Report (ACR / VPAT-style).

Pure functions over a results list, so the judgment is unit-testable without any I/O.
"""
from .catalog import CRITERIA, CONFORMANCE_LEVELS

# For a conformance claim, a criterion must be met or genuinely inapplicable. "Partially Supports",
# "Does Not Support", and "Not Evaluated" all block the claim.
_ACCEPTABLE = {"Supports", "Not Applicable"}
_LEVEL_ORDER = {"A": 1, "AA": 2}


def _f(severity, message):
    return {"severity": severity, "message": message}


def summary(results):
    """Roll up conformance counts and derive the overall WCAG 2.2 level the results support.

    A product conforms to a level only if EVERY criterion at that level or below is "Supports" or
    "Not Applicable" — one unevaluated or partially-supporting criterion sinks the whole claim,
    exactly as a real VPAT reviewer would read it.
    """
    by_id = {r.get("id"): r for r in results}

    counts = {}
    for cid in CRITERIA:
        r = by_id.get(cid)
        conf = r.get("conformance") if r else "Not Evaluated"
        counts[conf] = counts.get(conf, 0) + 1

    def level_conformant(target):
        cap = _LEVEL_ORDER[target]
        for cid, meta in CRITERIA.items():
            if _LEVEL_ORDER[meta["level"]] <= cap:
                r = by_id.get(cid)
                if (r.get("conformance") if r else None) not in _ACCEPTABLE:
                    return False
        return True

    conforms_to = None
    for lvl in ("A", "AA"):
        if level_conformant(lvl):
            conforms_to = lvl
        else:
            break

    return {
        "counts": counts,
        "conforms_to": conforms_to,
        "evaluated": sum(1 for cid in CRITERIA if cid in by_id),
        "total": len(CRITERIA),
    }


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
    s = summary(results)
    verdict = (f"**Conforms to WCAG 2.2 Level {s['conforms_to']}.**" if s["conforms_to"]
               else "**Does not fully conform to WCAG 2.2 Level A** — see the gaps below.")
    order = ["Supports", "Partially Supports", "Does Not Support", "Not Applicable", "Not Evaluated"]
    tally = " · ".join(f"{k}: {s['counts'][k]}" for k in order if s["counts"].get(k))
    lines = [
        f"# Accessibility Conformance Report — {product}",
        "",
        "Based on WCAG 2.2. Conformance: Supports / Partially Supports / Does Not Support / Not Applicable.",
        "",
        verdict,
        "",
        f"{s['evaluated']} of {s['total']} criteria evaluated — {tally}.",
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
