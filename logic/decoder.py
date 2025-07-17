def decode_catalog_number(catalog_number):
    """
    Decodes a 10250T catalog number into its components.
    Supports:
    - Non-Illuminated Pushbuttons
    - Illuminated Pushbuttons
    - Illuminated Push-Pulls
    - Non-Illuminated Push-Pulls
    - Standard Indicating Lights
    - PresTest
    - Master Test
    """
    parts = catalog_number.split('-')
    result = {"Catalog Number": catalog_number}

    if not parts or not parts[0].startswith("10250T"):
        result["Error"] = "Invalid catalog number format"
        return result

    suffix = parts[1] if len(parts) > 1 else ""
    result["Product Type"] = identify_product_type(suffix)

    if result["Product Type"] == "Non-Illuminated Pushbuttons":
        result.update(decode_non_illuminated_pushbutton(suffix))
    elif result["Product Type"] == "Illuminated Pushbuttons":
        result.update(decode_illuminated_pushbutton(suffix))
    elif result["Product Type"] == "Illuminated Push-Pulls":
        result.update(decode_illuminated_push_pull(suffix))
    elif result["Product Type"] == "Non-Illuminated Push-Pulls":
        result.update(decode_non_illuminated_push_pull(suffix))
    elif result["Product Type"] == "Standard Indicating Lights":
        result.update(decode_indicating_light(suffix))
    elif result["Product Type"] == "PresTest":
        result.update(decode_prestest(suffix))
    elif result["Product Type"] == "Master Test":
        result.update(decode_master_test(suffix))
    else:
        result["Error"] = "Unknown product type"

    return result


def identify_product_type(suffix):
    if suffix.startswith("A"):
        return "Non-Illuminated Pushbuttons"
    elif suffix.startswith("L"):
        return "Illuminated Pushbuttons"
    elif suffix.startswith("PP"):
        return "Illuminated Push-Pulls"
    elif suffix.startswith("NP"):
        return "Non-Illuminated Push-Pulls"
    elif suffix.startswith("IL"):
        return "Standard Indicating Lights"
    elif suffix.startswith("PT"):
        return "PresTest"
    elif suffix.startswith("MT"):
        return "Master Test"
    return "Unknown"


def decode_non_illuminated_pushbutton(code):
    return {
        "Button Type": "Non-Illuminated",
        "Color Code": code[1:] if len(code) > 1 else "Unknown"
    }

def decode_illuminated_pushbutton(code):
    return {
        "Button Type": "Illuminated",
        "Light Color": code[1:] if len(code) > 1 else "Unknown"
    }

def decode_illuminated_push_pull(code):
    return {
        "Mechanism": "Push-Pull",
        "Illumination": "Yes",
        "Color Code": code[2:] if len(code) > 2 else "Unknown"
    }

def decode_non_illuminated_push_pull(code):
    return {
        "Mechanism": "Push-Pull",
        "Illumination": "No",
        "Color Code": code[2:] if len(code) > 2 else "Unknown"
    }

def decode_indicating_light(code):
    return {
        "Device Type": "Indicating Light",
        "Color Code": code[2:] if len(code) > 2 else "Unknown"
    }

def decode_prestest(code):
    return {
        "Device Type": "PresTest",
        "Configuration": code[2:] if len(code) > 2 else "Unknown"
    }

def decode_master_test(code):
    return {
        "Device Type": "Master Test",
        "Configuration": code[2:] if len(code) > 2 else "Unknown"
    }
