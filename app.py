import streamlit as st
import google.generativeai as genai

# ----------------------------
# Configure Gemini
# ----------------------------
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(
    page_title="🩺 AI Health Assistant",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 AI Human Health Assistant")
st.write("Ask any health-related question.")

question = st.text_area(
    "Enter your health question",
    placeholder="Example: What are the symptoms of diabetes?"
)

if st.button("Analyze"):

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    prompt = f"""
You are an experienced medical information assistant.

Answer the user's health question in simple language.

Use the following format:

Disease / Condition:
Symptoms:
Possible Causes:
Risk Factors:
Diagnosis:
Treatment Options:
Home Care Tips:
Prevention:
When to See a Doctor:
Emergency Warning Signs:
Disclaimer:

User Question:
{question}

Rules:
- Give educational information only.
- Do NOT diagnose the user.
- Recommend consulting a healthcare professional for diagnosis.
- If symptoms suggest an emergency, clearly state that immediate medical attention is needed.
"""

    with st.spinner("Analyzing..."):

        response = model.generate_content(prompt)

        st.success("Analysis Complete")

        st.markdown(response.text)

st.markdown("---")
st.caption(
    "⚠ This assistant provides general educational information only and is not a substitute for professional medical advice, diagnosis, or treatment."
)
