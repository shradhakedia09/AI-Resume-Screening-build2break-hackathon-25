# main.py
import streamlit as st
import os
from dotenv import load_dotenv

# ---------------------- SETUP ----------------------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ Missing OpenAI API Key. Please set OPENAI_API_KEY in .env or Streamlit Secrets.")
    st.stop()

# ---------------------- AGENT IMPORTS ----------------------
from Agents.policy_agent import answer_policy_question
from Agents.onboarding_agent import run
from Agents.guardrails import sanitize_input
from Agents import resume_screening_app  # ✅ Resume app
from Scheduler.run_scheduler import add_task_interactive  # ✅ Scheduler integration

# ---------------------- UI CONFIG ----------------------
st.set_page_config(page_title="AI HR Orchestrator", page_icon="🤖", layout="centered")
st.title("🤖 Unified HR AI System")

if "mode" not in st.session_state:
    st.session_state.mode = None

# ---------------------- MAIN QUERY ----------------------
query = st.text_input(
    "What would you like to do? (e.g. 'screen resumes', 'check policy', 'create onboarding plan', 'schedule task')"
)

if st.button("Submit"):
    if not query.strip():
        st.warning("Please enter a valid query.")
        st.stop()

    try:
        sanitized_query = sanitize_input(query)
    except ValueError as e:
        st.error(str(e))
        st.stop()

    q = sanitized_query.lower()

    if any(k in q for k in ["resume", "screen", "candidate", "cv"]):
        st.session_state.mode = "resume"
    elif any(k in q for k in ["policy", "leave", "vacation", "rules", "payroll", "salary"]):
        st.session_state.mode = "policy"
    elif any(k in q for k in ["onboard", "joining", "orientation", "welcome"]):
        st.session_state.mode = "onboarding"
    elif any(k in q for k in ["schedule", "calendar", "meeting", "task"]):
        st.session_state.mode = "scheduler"
    else:
        st.session_state.mode = "unknown"

# ---------------------- DYNAMIC UI ----------------------
if st.session_state.mode == "resume":
    st.subheader("📄 Resume Screening")
    resume_screening_app.run()  # ✅ Uses your Streamlit resume module

elif st.session_state.mode == "policy":
    st.subheader("📜 HR Policy Assistant")
    question = st.text_input("Ask your HR policy question:")
    if st.button("Get Policy Answer"):
        if question:
            with st.spinner("Checking policy..."):
                answer = answer_policy_question(question)
            st.success(answer)
        else:
            st.warning("Please enter a question.")

elif st.session_state.mode == "onboarding":
    st.subheader("👋 Employee Onboarding Assistant")

    onboarding_mode = st.radio(
        "Choose input method:",
        ["Single Candidate", "Batch via CSV"],
        horizontal=True
    )

    if onboarding_mode == "Single Candidate":
        name = st.text_input("Candidate Name:")
        dept = st.text_input("Department:")
        email = st.text_input("Candidate Email (optional):")

        if st.button("Generate Onboarding Plan"):
            if name and dept:
                with st.spinner("Generating onboarding plan..."):
                    plan = generate_onboarding_plan(name=name, dept=dept)
                st.text_area("🗓️ Onboarding Plan", plan, height=300)
            else:
                st.warning("Please fill both fields.")

    elif onboarding_mode == "Batch via CSV":
        st.info("Upload a CSV with columns: name, email, department")
        csv_file = st.file_uploader("Upload CSV File", type=["csv"])

        if csv_file and st.button("Generate Batch Onboarding"):
            with st.spinner("Processing onboarding batch..."):
                results = generate_onboarding_plan(csv_file=csv_file)
            st.success("✅ Batch onboarding completed!")
            st.dataframe(results)

elif st.session_state.mode == "scheduler":
    st.subheader("🗓️ Smart Task Scheduler")

    name = st.text_input("Task Name:")
    time_input = st.text_input("Preferred Time (YYYY-MM-DD HH:MM) or leave blank:")
    duration = st.number_input("Duration (hours):", min_value=1, max_value=8, value=1)
    details = st.text_area("Task Details:")

    if st.button("Add Task"):
        with st.spinner("Scheduling your task..."):
            result = add_task_interactive(name, time_input, duration, details)
        st.success(result)

elif st.session_state.mode == "unknown":
    st.info("🤔 Try asking about resumes, policies, onboarding, or scheduling.")
