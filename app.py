import streamlit as st
import pandas as pd

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

# Employee dataset
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

df = pd.DataFrame(data)

# Salary calculations
total_salary = df["Salary"].sum()
average_salary = df["Salary"].mean()
highest_salary = df["Salary"].max()
lowest_salary = df["Salary"].min()

highest_employee = df.loc[
    df["Salary"].idxmax(),
    "Employee"
]

# Dataset
st.header("📊 Employee Dataset")

st.dataframe(
    df,
    use_container_width=True
)

# Statistics
st.header("📈 Salary Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Salary",
    f"₹{total_salary:,.0f}"
)

col2.metric(
    "Average Salary",
    f"₹{average_salary:,.0f}"
)

col3.metric(
    "Highest Salary",
    f"₹{highest_salary:,.0f}"
)

col4.metric(
    "Lowest Salary",
    f"₹{lowest_salary:,.0f}"
)

# Highest paid employee
st.header("🏆 Highest-Paid Employee")

st.success(
    f"{highest_employee} earns ₹{highest_salary:,.0f}"
)

# Chart
st.header("📊 Salary Visualization")

chart_data = df.set_index("Employee")

st.bar_chart(
    chart_data["Salary"]
)

# Conclusion
st.header("📝 Conclusion")

st.write(
    "The employee salary dataset was successfully analyzed "
    "using Python. The application calculates the total, "
    "average, highest, and lowest salaries and identifies "
    "the highest-paid employee."
)

st.success(
    "Employee Salary Analysis completed successfully-version-2! 🎉"
)