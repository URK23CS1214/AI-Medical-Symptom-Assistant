# 🩺 AI-Powered Medical Symptom Assistant
# URK23CS1214
An AI-powered Medical Symptom Assistant developed using Python, Streamlit, Ollama and Llama 3.2.

The application accepts patient information and natural-language symptoms and generates an informational symptom analysis, possible conditions, follow-up questions, medical-attention guidance and a safety disclaimer.

> ⚠️ This application is for educational and informational purposes only. It does not provide a medical diagnosis and does not replace advice from a qualified healthcare professional.

## Features

- Patient information collection
- Natural-language symptom input
- Symptom extraction
- Missing-information detection
- AI-based symptom analysis
- Possible-condition identification
- Follow-up question generation
- Medical-attention guidance
- Structured response
- Medical disclaimer
- Save analysis to a text file

## Technologies Used

- Python
- Streamlit
- Ollama
- Llama 3.2
- Pandas
- Prompt Engineering

## Project Structure

```text
MedicalAssistant/
│
├── app.py
├── input_module.py
├── profile_module.py
├── symptom_module.py
├── context_module.py
├── prompt_module.py
├── analysis_module.py
├── question_module.py
├── safety_module.py
├── save_module.py
├── requirements.txt
│
├── data/
│   └── sample_cases.csv
│
├── screenshots/
│
└── outputs/
    └── medical_analysis.txt