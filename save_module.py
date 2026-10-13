import os


def save_analysis(analysis):

    os.makedirs("outputs",exist_ok=True)

    filename="outputs/medical_analysis.txt"

    with open(filename,"w",encoding="utf-8") as file:

        file.write(
            "AI-POWERED MEDICAL SYMPTOM ANALYSIS\n"
        )

        file.write(
            "="*45+"\n\n"
        )

        file.write(analysis)

    return filename