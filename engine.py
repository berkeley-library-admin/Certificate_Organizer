# =====================================================================
# MODULE 1: SMART DATA PROCESSING ENGINE (engine.py)
# Purpose: Handles name parsing, capitalization, and compound last names.
# =====================================================================

def format_certificate_name(raw_name):
    """
    Cleans spacing anomalies and structures names into:
    GIVEN NAME(S) + MIDDLE INITIAL + LAST NAME (ALL CAPS)
    Supports compound last names (e.g., Dela Cruz, Del Rosario, San Jose)
    """
    words = [word.upper() for word in raw_name.split()]
    if not words:
        return ""
        
    # Standardize edge cases with very short entries
    if len(words) == 1:
        return words[0]
    if len(words) == 2:
        return f"{words[0]} {words[1]}"
        
    # List of common multi-word last name prefixes (Fixed single brackets)
    compound_prefixes = {"DELA", "DEL", "DE", "LOS", "SAN", "SANTA", "CRUZ"}

    # If the second-to-last word is a prefix, group it with the final word
    if words[-2] in compound_prefixes:
        last_name = f"{words[-2]} {words[-1]}"
        
        # Check if there's a middle name left before the compound last name
        if len(words) >= 4:
            middle_initial = words[-3][0] + "."
            given_names = " ".join(words[:-3])
            return f"{given_names} {middle_initial} {last_name}"
        else:
            # No middle name provided, just given name + compound last name
            given_names = " ".join(words[:-2])
            return f"{given_names} {last_name}"

    # Default fallback logic for regular single-word last names
    last_name = words[-1]
    middle_initial = words[-2][0] + "."
    given_names = " ".join(words[:-2])
    
    return f"{given_names} {middle_initial} {last_name}"
