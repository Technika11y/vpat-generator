import unittest

from vpat.report import validate, has_errors, render, summary
from vpat.catalog import CRITERIA


def all_supports(**overrides):
    """A full results set where every catalog criterion Supports, minus any overrides."""
    out = [{"id": cid, "conformance": "Supports", "remarks": "ok"} for cid in CRITERIA]
    for cid, conf in overrides.items():
        cid = cid.replace("_", ".")
        for r in out:
            if r["id"] == cid:
                r["conformance"] = conf
    return out


def result(cid="1.1.1", conformance="Supports", remarks=""):
    return {"id": cid, "conformance": conformance, "remarks": remarks}


class ValidateTests(unittest.TestCase):
    def test_unknown_criterion_is_error(self):
        findings = validate([result(cid="9.9.9")])
        self.assertTrue(any(f["severity"] == "error" and "unknown criterion" in f["message"] for f in findings))

    def test_invalid_conformance_level_is_error(self):
        findings = validate([result(conformance="Mostly Supports")])
        self.assertTrue(any(f["severity"] == "error" and "invalid conformance" in f["message"] for f in findings))

    def test_partial_without_remarks_warns(self):
        findings = validate([result(conformance="Partially Supports", remarks="")])
        self.assertTrue(any(f["severity"] == "warn" and "should include remarks" in f["message"] for f in findings))

    def test_partial_with_remarks_no_such_warning(self):
        findings = validate([result(conformance="Partially Supports", remarks="Contrast fails on badges")])
        self.assertFalse(any("should include remarks" in f["message"] for f in findings))

    def test_unevaluated_criteria_warn(self):
        findings = validate([result()])  # only 1.1.1 evaluated
        self.assertTrue(any(f["severity"] == "warn" and "not evaluated" in f["message"] for f in findings))

    def test_valid_result_has_no_errors(self):
        self.assertFalse(has_errors(validate([result()])))


class RenderTests(unittest.TestCase):
    def setUp(self):
        self.md = render([result(conformance="Supports")], product="Acme App")

    def test_header_includes_product(self):
        self.assertIn("Accessibility Conformance Report — Acme App", self.md)

    def test_row_present_for_evaluated_criterion(self):
        self.assertIn("| 1.1.1 Non-text Content | A | Supports |", self.md)

    def test_unevaluated_criterion_marked(self):
        self.assertIn("Not Evaluated", self.md)


class CatalogTests(unittest.TestCase):
    def test_full_a_aa_set_present(self):
        from vpat.catalog import CRITERIA
        self.assertGreaterEqual(len(CRITERIA), 55)

    def test_wcag_22_additions_present(self):
        from vpat.catalog import CRITERIA
        for cid in ("3.2.6", "3.3.7", "2.4.11", "2.5.7", "2.5.8", "3.3.8"):
            self.assertIn(cid, CRITERIA)

    def test_parsing_removed_in_wcag_22(self):
        from vpat.catalog import CRITERIA
        self.assertNotIn("4.1.1", CRITERIA)  # 4.1.1 Parsing was removed in WCAG 2.2

    def test_only_a_and_aa_levels(self):
        from vpat.catalog import CRITERIA
        self.assertEqual({c["level"] for c in CRITERIA.values()}, {"A", "AA"})


class SummaryTests(unittest.TestCase):
    def test_all_supports_conforms_to_aa(self):
        self.assertEqual(summary(all_supports())["conforms_to"], "AA")

    def test_not_applicable_still_conforms(self):
        # "Not Applicable" is an acceptable outcome for a conformance claim.
        self.assertEqual(summary(all_supports(**{"1_2_1": "Not Applicable"}))["conforms_to"], "AA")

    def test_partial_at_aa_drops_to_a(self):
        # 1.4.3 Contrast is AA — a gap there sinks AA but leaves A intact.
        self.assertEqual(summary(all_supports(**{"1_4_3": "Partially Supports"}))["conforms_to"], "A")

    def test_gap_at_a_conforms_to_nothing(self):
        # 1.1.1 Non-text Content is A — a gap there sinks everything.
        self.assertIsNone(summary(all_supports(**{"1_1_1": "Does Not Support"}))["conforms_to"])

    def test_unevaluated_blocks_the_claim(self):
        self.assertIsNone(summary([{"id": "1.1.1", "conformance": "Supports"}])["conforms_to"])

    def test_counts_cover_every_criterion(self):
        s = summary(all_supports(**{"1_4_3": "Partially Supports"}))
        self.assertEqual(sum(s["counts"].values()), len(CRITERIA))
        self.assertEqual(s["counts"]["Partially Supports"], 1)

    def test_render_states_the_verdict(self):
        self.assertIn("Conforms to WCAG 2.2 Level AA", render(all_supports()))
        self.assertIn("Does not fully conform", render(all_supports(**{"1_1_1": "Does Not Support"})))


if __name__ == "__main__":
    unittest.main()
