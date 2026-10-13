import ollama


def extract_symptoms(symptom_text):

    prompt=f"""
You are a symptom extraction assistant.

Extract only the symptoms explicitly mentioned
in the user's description.

User description:
{symptom_text}

Return the symptoms as a simple bullet list.

Do not diagnose the user.
Do not add symptoms that were not mentioned.
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