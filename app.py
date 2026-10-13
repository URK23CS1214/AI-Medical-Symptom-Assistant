import streamlit as st

from input_module import collect_patient_information
from profile_module import create_patient_profile
from symptom_module import extract_symptoms
from context_module import identify_missing_information
from prompt_module import create_medical_prompt
from analysis_module import analyze_symptoms
from question_module import generate_follow_up_questions
from safety_module import medical_attention_guidance
from save_module import save_analysis


st.set_page_config(
    page_title="AI Medical Symptom Assistant",
    page_icon="🩺",
    layout="wide"
)


st.title("🩺 AI-Powered Medical Symptom Assistant")

st.write(
    "An AI-based application for informational symptom analysis "
    "using a local Llama 3.2 model."
)


st.warning(
    "⚠️ This application provides educational and informational "
    "information only. It is NOT a medical diagnosis."
)


st.divider()


# Patient information
profile_data=collect_patient_information()


st.divider()


# Analyze button
if st.button(
    "🔍 Analyze Symptoms",
    type="primary",
    use_container_width=True
):

    if not profile_data["symptoms"].strip():

        st.error(
            "Please describe your symptoms before analyzing."
        )

    else:

        with st.spinner(
            "Analyzing symptoms using AI..."
        ):

            # Create patient profile
            patient_profile=create_patient_profile(
                profile_data
            )


            # Extract symptoms
            extracted_symptoms=extract_symptoms(
                profile_data["symptoms"]
            )


            # Find missing information
            missing_information=identify_missing_information(
                patient_profile
            )


            # Generate prompt
            prompt=create_medical_prompt(
                patient_profile,
                extracted_symptoms,
                missing_information
            )


            # Generate analysis
            analysis=analyze_symptoms(
                prompt
            )


            # Generate follow-up questions
            follow_up_questions=generate_follow_up_questions(
                patient_profile,
                extracted_symptoms
            )


            # Medical attention guidance
            medical_guidance=medical_attention_guidance()


            # Store results
            st.session_state["patient_profile"]=patient_profile
            st.session_state["extracted_symptoms"]=extracted_symptoms
            st.session_state["missing_information"]=missing_information
            st.session_state["analysis"]=analysis
            st.session_state["follow_up_questions"]=follow_up_questions
            st.session_state["medical_guidance"]=medical_guidance


# Display results

if "analysis" in st.session_state:

    st.divider()

    st.header("📋 Medical Symptom Analysis")


    # Patient information
    st.subheader("👤 Patient Information")

    profile=st.session_state["patient_profile"]

    col1,col2,col3=st.columns(3)

    col1.metric(
        "Age",
        profile["Age"]
    )

    col2.metric(
        "Sex",
        profile["Sex"]
    )

    col3.metric(
        "Severity",
        profile["Severity"]
    )


    st.write(
        "**Duration:**",
        profile["Duration"]
    )


    # Extracted symptoms
    st.subheader("🩺 Reported Symptoms")

    st.markdown(
        st.session_state["extracted_symptoms"]
    )


    # Missing information
    st.subheader("ℹ️ Missing Information")

    missing=st.session_state["missing_information"]

    if missing:

        for item in missing:

            st.write("•",item)

    else:

        st.write(
            "No major missing information identified."
        )


    # AI analysis
    st.subheader("🤖 AI Analysis")

    st.markdown(
        st.session_state["analysis"]
    )


    # Follow-up questions
    st.subheader("❓ Follow-Up Questions")

    st.markdown(
        st.session_state["follow_up_questions"]
    )


    # Medical attention
    st.subheader("🚨 Medical Attention")

    st.markdown(
        st.session_state["medical_guidance"]
    )


    # Disclaimer
    st.subheader("⚠️ Disclaimer")

    st.info(
        "This AI-generated response is intended for "
        "educational and informational purposes only.\n\n"
        "It is not a medical diagnosis and does not replace "
        "advice from a qualified healthcare professional.\n\n"
        "For serious, worsening or urgent symptoms, seek "
        "appropriate medical care."
    )


    # Save
    st.divider()

    st.subheader("💾 Save Analysis")

    complete_report=(
        st.session_state["analysis"]
        + "\n\n"
        + "FOLLOW-UP QUESTIONS\n"
        + "====================\n"
        + st.session_state["follow_up_questions"]
        + "\n\n"
        + st.session_state["medical_guidance"]
    )


    if st.button(
        "💾 Save Medical Analysis",
        use_container_width=True
    ):

        filename=save_analysis(
            complete_report
        )

        st.success(
            "Analysis saved successfully!"
        )

        st.write(
            "File:",
            filename
        )