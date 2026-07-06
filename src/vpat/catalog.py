"""WCAG 2.2 success-criteria catalog (Level A + AA).

PARTIAL by design for pre-alpha: a representative spread across all four principles, including the
WCAG 2.2 additions (2.4.11, 2.5.8). Extend to the full A/AA set before using for a real ACR — the
README status table states this limit honestly.
"""

# id -> {"title": ..., "level": "A" | "AA"}
CRITERIA = {
    "1.1.1": {"title": "Non-text Content", "level": "A"},
    "1.2.1": {"title": "Audio-only and Video-only (Prerecorded)", "level": "A"},
    "1.3.1": {"title": "Info and Relationships", "level": "A"},
    "1.3.2": {"title": "Meaningful Sequence", "level": "A"},
    "1.4.1": {"title": "Use of Color", "level": "A"},
    "2.1.1": {"title": "Keyboard", "level": "A"},
    "2.4.1": {"title": "Bypass Blocks", "level": "A"},
    "2.4.2": {"title": "Page Titled", "level": "A"},
    "2.4.3": {"title": "Focus Order", "level": "A"},
    "2.4.4": {"title": "Link Purpose (In Context)", "level": "A"},
    "3.1.1": {"title": "Language of Page", "level": "A"},
    "3.3.1": {"title": "Error Identification", "level": "A"},
    "3.3.2": {"title": "Labels or Instructions", "level": "A"},
    "4.1.2": {"title": "Name, Role, Value", "level": "A"},
    "1.4.3": {"title": "Contrast (Minimum)", "level": "AA"},
    "1.4.4": {"title": "Resize Text", "level": "AA"},
    "1.4.5": {"title": "Images of Text", "level": "AA"},
    "2.4.6": {"title": "Headings and Labels", "level": "AA"},
    "2.4.7": {"title": "Focus Visible", "level": "AA"},
    "2.4.11": {"title": "Focus Not Obscured (Minimum)", "level": "AA"},   # WCAG 2.2
    "2.5.8": {"title": "Target Size (Minimum)", "level": "AA"},           # WCAG 2.2
    "3.2.4": {"title": "Consistent Identification", "level": "AA"},
    "4.1.3": {"title": "Status Messages", "level": "AA"},
}

# ITI VPAT conformance vocabulary.
CONFORMANCE_LEVELS = {
    "Supports",
    "Partially Supports",
    "Does Not Support",
    "Not Applicable",
}
