import streamlit as st
import matplotlib.pyplot as plt

# Page config
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Performance Dashboard")
st.caption("Visual insights into student academic performance")

st.divider()

# --- INPUT SECTION ---
st.subheader("📝 Student Details")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Student Name")
    mark1 = st.number_input("📘 Subject 1", 0, 100)

with col2:
    mark2 = st.number_input("📗 Subject 2", 0, 100)
    mark3 = st.number_input("📕 Subject 3", 0, 100)

st.divider()

# --- CALCULATE ---
if st.button("🚀 Generate Dashboard"):
    marks = [mark1, mark2, mark3]
    average = sum(marks) / len(marks)

    # Grade logic
    if average >= 75:
        grade = "A"
        status = "Excellent 🌟"
        feedback = "Outstanding performance! Keep aiming high."
    elif average >= 60:
        grade = "B"
        status = "Good 👍"
        feedback = "Strong work! A little more effort gets you to the top."
    elif average >= 50:
        grade = "C"
        status = "Fair ⚠️"
        feedback = "You passed, but there’s room for improvement."
    else:
        grade = "F"
        status = "At Risk ❌"
        feedback = "Extra support is recommended."

    # --- RESULTS ---
    st.subheader("📊 Performance Summary")

    c1, c2, c3 = st.columns(3)
    c1.metric("Average", f"{average:.2f}")
    c2.metric("Grade", grade)
    c3.metric("Status", status)

    st.progress(int(average))

    st.info(feedback)S

    # --- CHART ---
    st.subheader("📈 Marks Breakdown")

    fig, ax = plt.subplots()
    subjects = ["Subject 1", "Subject 2", "Subject 3"]
    ax.bar(subjects, marks)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Marks")
    ax.set_title("Subject-wise Performance")

    st.pyplot(fig)

    # --- FOOTER ---
    st.divider()
    st.caption("📌 Built with Streamlit | Student Analytics Mini Project")
