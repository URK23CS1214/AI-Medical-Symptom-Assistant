import ollama


def generate_follow_up_questions(profile,symptoms):

    prompt=f"""
Generate 5 useful follow-up questions based only on
the following patient information and symptoms.

Age: {profile["Age"]}
Sex: {profile["Sex"]}
Duration: {profile["Duration"]}
Severity: {profile["Severity"]}

Symptoms:
{symptoms}

Ask questions that help clarify the symptoms.

Do not diagnose the user.
Do not invent information.

Return only the questions.
"""

    response=ollama.chat(
        model="llama3.2:latest",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        options={
            "num_ctx":1024
        }
    )

    return response["message"]["content"]