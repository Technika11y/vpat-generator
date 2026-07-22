# VPAT / ACR Generator

> Generates a **WCAG 2.2 Accessibility Conformance Report** (ACR / VPAT-style) from criteria
> results — and validates the inputs first, so the report is honest before it ships.
>
> Part of the **Technika11y** suite · *Root access for everyone.*

[![ci](https://github.com/technika11y/vpat-generator/actions/workflows/ci.yml/badge.svg)](https://github.com/technika11y/vpat-generator/actions/workflows/ci.yml)
![status](https://img.shields.io/badge/status-pre--alpha-orange)
![license](https://img.shields.io/badge/license-Apache--2.0-blue)
![python](https://img.shields.io/badge/python-3.10%2B-informational)

---

## Quick start

```bash
git clone https://github.com/technika11y/vpat-generator && cd vpat-generator
PYTHONPATH=src python3 -m vpat.cli report examples/results.json
```

## Status — read this first

**Pre-alpha (`v0.1.0a0`). Honest state of the code:**

| Capability | State |
|---|---|
| Validate results: unknown criterion, invalid conformance level | ✅ works, tested |
| Warn on a claimed gap ("Partially/Does Not Support") with no remarks | ✅ works, tested |
| Warn on catalog criteria that were not evaluated | ✅ works, tested |
| Render a Markdown ACR covering every catalog criterion | ✅ works, tested |
| **Fails closed** — refuses to render from invalid results | ✅ works |
| **Complete WCAG 2.2 Level A + AA catalog (55 criteria)** | ✅ works, tested |
| Section 508 mapping, HTML / OpenACR export | ⚠️ not built — [roadmap](#roadmap) |

The catalog now covers the **complete WCAG 2.2 Level A + AA set (55 criteria)** — including the 2.2
additions (Consistent Help, Redundant Entry, Focus Not Obscured, Dragging Movements, Target Size,
Accessible Authentication) and with the removed 4.1.1 Parsing excluded. Section 508 mapping and
HTML/OpenACR export are still to come.

## Why it exists

Municipal and enterprise procurement runs on VPATs, and most are written by hand — inconsistent,
and quietly missing criteria. This turns a structured set of results into a complete ACR where
*every* catalog criterion appears (unevaluated ones are labelled, not omitted), and it refuses to
render if the inputs are malformed.

## Usage

```bash
PYTHONPATH=src python -m vpat.cli check  examples/results.json
PYTHONPATH=src python -m vpat.cli report examples/results.json --product "Acme App" > acr.md
```

## Roadmap

- [ ] Optional Level AAA criteria
- [ ] Section 508 / EN 301 549 mapping columns
- [ ] HTML + OpenACR (machine-readable) export
- [ ] Ingest results from the WCAG CI Gate + Shadow-DOM Auditor
- [ ] SARIF output + the shared Technika11y CI gate

## License

[Apache-2.0](LICENSE). See [`SECURITY.md`](SECURITY.md).

---

**Part of the [Technika11y](https://github.com/technika11y) suite** · [technika11y.github.io](https://technika11y.github.io/) · security, compliance, and accessibility as one discipline.
