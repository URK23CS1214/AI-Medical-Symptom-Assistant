def create_patient_profile(data):

    profile={
        "Age":data["age"],
        "Sex":data["sex"],
        "Duration":data["duration"],
        "Severity":data["severity"],
        "Medical History":data["history"],
        "Medications":data["medications"],
        "Allergies":data["allergies"]
    }

    return profile