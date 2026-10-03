import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Employee Salary Analysis",
    page_icon="💰",
    layout="wide"
)

# Title
st.title("💰 Employee Salary Analysis")
st.write("Veda Technology Internship Project")

st.divider()

# Employee data
data = {
    "Employee": [
        "Arun",
        "Priya",
        "Karthik",
        "Divya",
        "Rahul",
        "Sneha",
        "Vijay",
        "Anjali",
        "Surya",
        "Keerthana"
    ],
    "Salary": [
        25000,
        32000,
        28000,
        45000,
        38000,
        30000,
        52000,
        35000,
        41000,
        29000
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate salary statistics
salaries = df["Salary"].tolist()

total_salary = sum(salaries)
average_salary = total_salary / len(salaries)
highest_salary = max(salaries)
lowest_salary = min(salaries)

highest_employee = df.loc[
    df["Salary"].idxmax(),
    "Employee"
]

# Dataset
st.header("Employee Dataset")

st.dataframe(df, use_container_width=True)

# Statistics
st.header("Salary Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Salary",
    f"₹{total_salary:,}"
)

col2.metric(
    "Average Salary",
    f"₹{average_salary:,.0f}"
)

col3.metric(
    "Highest Salary",
    f"₹{highest_salary:,}"
)

col4.metric(
    "Lowest Salary",
    f"₹{lowest_salary:,}"
)

# Highest paid employee
st.header("Highest-Paid Employee")

st.success(
    f"{highest_employee} earns ₹{highest_salary:,}"
)

# Chart
st.header("Salary Visualization")

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(
    df["Employee"],
    df["Salary"]
)

ax.set_xlabel("Employee")
ax.set_ylabel("Salary (₹)")
ax.set_title("Employee Salary Analysis")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# Conclusion
st.header("Conclusion")

st.write(
    "The employee salary dataset was successfully analyzed "
    "using Python. The application calculates total, average, "
    "highest, and lowest salaries and identifies the "
    "highest-paid employee."
)

st.success("Employee Salary Analysis completed successfully! 🎉")