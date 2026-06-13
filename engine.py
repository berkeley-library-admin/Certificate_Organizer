# =====================================================================
# MODULE 1: DATA PROCESSING ENGINE (engine.py)
# Purpose: Handles name parsing, capitalization, and formatting rules.
# =====================================================================

def format_certificate_name(raw_name):
    """
    Cleans spacing anomalies and structures names into:
    GIVEN NAME(S) + MIDDLE INITIAL + LAST NAME (ALL CAPS)
    """
    words = [word.upper() for word in raw_name.split()]
    if not words:
        return ""
    if len(words) == 1:
        return words[0]
    if len(words) == 2:
        return f"{words[0]} {words[1]}"
    
    last_name = words[-1]
    middle_initial = words[-2][0] + "."
    given_names = " ".join(words[:-2])
    
    return f"{given_names} {middle_initial} {last_name}"