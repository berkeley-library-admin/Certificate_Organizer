# =====================================================================
# MODULE 1: SMART DATA PROCESSING ENGINE (COMMA DETECTION ENABLED)
# Purpose: Handles name parsing, capitalization, compound surnames, 
#          and "Last Name, First Name" formats.
# =====================================================================

def format_certificate_name(raw_name):
    """
    Cleans spacing anomalies and structures names into:
    GIVEN NAME(S) + MIDDLE INITIAL + LAST NAME (ALL CAPS)
    Supports:
      - Standard: Given Middle Last -> GIVEN M. LAST
      - Compound: Given Middle Dela Cruz -> GIVEN M. DELA CRUZ
      - Inverted: Last, Given Middle -> GIVEN M. LAST
    """
    raw_name = raw_name.strip()
    if not raw_name:
        return ""

    # -----------------------------------------------------------------
    # RULE 1: INVERTED FORMAT DETECTION (If a comma exists)
    # -----------------------------------------------------------------
    if "," in raw_name:
        parts = raw_name.split(",", 1)
        last_name = parts[0].strip().upper()
        remaining_names = parts[1].strip().split()
        
        if not remaining_names:
            return last_name
        if len(remaining_names) == 1:
            return f"{remaining_names[0].upper()} {last_name}"
            
        # The last word among the remaining words becomes the middle name
        middle_initial = remaining_names[-1][0].upper() + "."
        given_names = " ".join([w.upper() for w in remaining_names[:-1]])
        
        return f"{given_names} {middle_initial} {last_name}"

    # -----------------------------------------------------------------
    # RULE 2: STANDARD FORMAT (No comma exists)
    # -----------------------------------------------------------------
    words = [word.upper() for word in raw_name.split()]
    if len(words) == 1:
        return words[0]
    if len(words) == 2:
        return f"{words[0]} {words[1]}"
        
    # Compound prefix check
    compound_prefixes = {"DELA", "DEL", "DE", "LOS", "SAN", "SANTA", "CRUZ", "GOLE"}

    if words[-2] in compound_prefixes:
        last_name = f"{words[-2]} {words[-1]}"
        if len(words) >= 4:
            middle_initial = words[-3][0] + "."
            given_names = " ".join(words[:-3])
            return f"{given_names} {middle_initial} {last_name}"
        else:
            given_names = " ".join(words[:-2])
            return f"{given_names} {last_name}"

    # Regular single-word last name fallback
    last_name = words[-1]
    middle_initial = words[-2][0] + "."
    given_names = " ".join(words[:-2])
    
    return f"{given_names} {middle_initial} {last_name}"
