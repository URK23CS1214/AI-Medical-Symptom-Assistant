import streamlit as st


def collect_patient_information():

    st.subheader("👤 Patient Information")

    col1,col2=st.columns(2)

    with col1:

        age=st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=22
        )

        sex=st.selectbox(
            "Sex",
            ["Female","Male","Other","Prefer not to say"]
        )

        duration=st.text_input(
            "Duration of Symptoms",
            "2 days"
        )

    with col2:

        severity=st.selectbox(
            "Severity",
            ["Mild","Moderate","Severe"]
        )

        history=st.text_area(
            "Relevant Medical History",
            placeholder="Example: No known relevant condition"
        )

        medications=st.text_area(
            "Current Medications",
            placeholder="Enter medications if relevant"
        )

    allergies=st.text_area(
        "Allergies",
        placeholder="Enter allergies if relevant"
    )

    symptoms=st.text_area(
        "Describe your symptoms",
        height=150,
        placeholder="Example: I have fever and cough for two days. My throat is also painful."
    )

    profile={
        "age":age,
        "sex":sex,
        "duration":duration,
        "severity":severity,
        "history":history,
        "medications":medications,
        "allergies":allergies,
        "symptoms":symptoms
    }

    return profile