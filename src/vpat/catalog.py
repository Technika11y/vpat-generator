"""WCAG 2.2 success-criteria catalog — the complete Level A + AA set (55 criteria).

Reflects WCAG 2.2: 4.1.1 Parsing was removed, and the new criteria (2.4.11, 2.5.7, 2.5.8, 3.2.6,
3.3.7, 3.3.8) are included. Level AAA is intentionally out of scope (see README roadmap).
"""

# id -> {"title": ..., "level": "A" | "AA"}
CRITERIA = {
    # ---- Level A ----
    "1.1.1": {"title": "Non-text Content", "level": "A"},
    "1.2.1": {"title": "Audio-only and Video-only (Prerecorded)", "level": "A"},
    "1.2.2": {"title": "Captions (Prerecorded)", "level": "A"},
    "1.2.3": {"title": "Audio Description or Media Alternative (Prerecorded)", "level": "A"},
    "1.3.1": {"title": "Info and Relationships", "level": "A"},
    "1.3.2": {"title": "Meaningful Sequence", "level": "A"},
    "1.3.3": {"title": "Sensory Characteristics", "level": "A"},
    "1.4.1": {"title": "Use of Color", "level": "A"},
    "1.4.2": {"title": "Audio Control", "level": "A"},
    "2.1.1": {"title": "Keyboard", "level": "A"},
    "2.1.2": {"title": "No Keyboard Trap", "level": "A"},
    "2.1.4": {"title": "Character Key Shortcuts", "level": "A"},
    "2.2.1": {"title": "Timing Adjustable", "level": "A"},
    "2.2.2": {"title": "Pause, Stop, Hide", "level": "A"},
    "2.3.1": {"title": "Three Flashes or Below Threshold", "level": "A"},
    "2.4.1": {"title": "Bypass Blocks", "level": "A"},
    "2.4.2": {"title": "Page Titled", "level": "A"},
    "2.4.3": {"title": "Focus Order", "level": "A"},
    "2.4.4": {"title": "Link Purpose (In Context)", "level": "A"},
    "2.5.1": {"title": "Pointer Gestures", "level": "A"},
    "2.5.2": {"title": "Pointer Cancellation", "level": "A"},
    "2.5.3": {"title": "Label in Name", "level": "A"},
    "2.5.4": {"title": "Motion Actuation", "level": "A"},
    "3.1.1": {"title": "Language of Page", "level": "A"},
    "3.2.1": {"title": "On Focus", "level": "A"},
    "3.2.2": {"title": "On Input", "level": "A"},
    "3.2.6": {"title": "Consistent Help", "level": "A"},          # WCAG 2.2
    "3.3.1": {"title": "Error Identification", "level": "A"},
    "3.3.2": {"title": "Labels or Instructions", "level": "A"},
    "3.3.7": {"title": "Redundant Entry", "level": "A"},          # WCAG 2.2
    "4.1.2": {"title": "Name, Role, Value", "level": "A"},
    # ---- Level AA ----
    "1.2.4": {"title": "Captions (Live)", "level": "AA"},
    "1.2.5": {"title": "Audio Description (Prerecorded)", "level": "AA"},
    "1.3.4": {"title": "Orientation", "level": "AA"},
    "1.3.5": {"title": "Identify Input Purpose", "level": "AA"},
    "1.4.3": {"title": "Contrast (Minimum)", "level": "AA"},
    "1.4.4": {"title": "Resize Text", "level": "AA"},
    "1.4.5": {"title": "Images of Text", "level": "AA"},
    "1.4.10": {"title": "Reflow", "level": "AA"},
    "1.4.11": {"title": "Non-text Contrast", "level": "AA"},
    "1.4.12": {"title": "Text Spacing", "level": "AA"},
    "1.4.13": {"title": "Content on Hover or Focus", "level": "AA"},
    "2.4.5": {"title": "Multiple Ways", "level": "AA"},
    "2.4.6": {"title": "Headings and Labels", "level": "AA"},
    "2.4.7": {"title": "Focus Visible", "level": "AA"},
    "2.4.11": {"title": "Focus Not Obscured (Minimum)", "level": "AA"},  # WCAG 2.2
    "2.5.7": {"title": "Dragging Movements", "level": "AA"},             # WCAG 2.2
    "2.5.8": {"title": "Target Size (Minimum)", "level": "AA"},          # WCAG 2.2
    "3.1.2": {"title": "Language of Parts", "level": "AA"},
    "3.2.3": {"title": "Consistent Navigation", "level": "AA"},
    "3.2.4": {"title": "Consistent Identification", "level": "AA"},
    "3.3.3": {"title": "Error Suggestion", "level": "AA"},
    "3.3.4": {"title": "Error Prevention (Legal, Financial, Data)", "level": "AA"},
    "3.3.8": {"title": "Accessible Authentication (Minimum)", "level": "AA"},  # WCAG 2.2
    "4.1.3": {"title": "Status Messages", "level": "AA"},
}

# ITI VPAT conformance vocabulary.
CONFORMANCE_LEVELS = {
    "Supports",
    "Partially Supports",
    "Does Not Support",
    "Not Applicable",
}
