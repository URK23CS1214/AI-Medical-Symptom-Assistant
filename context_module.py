def identify_missing_information(profile):

    missing=[]

    if not profile["Duration"].strip():
        missing.append("Duration of symptoms")

    if not profile["Severity"].strip():
        missing.append("Severity of symptoms")

    if not profile["Medical History"].strip():
        missing.append("Relevant medical history")

    if not profile["Medications"].strip():
        missing.append("Current medications")

    if not profile["Allergies"].strip():
        missing.append("Allergies")

    return missing