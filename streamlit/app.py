import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Executive Overview",
    layout="wide"
)

# ---------- HEADER ----------
st.title("Executive Overview")
st.caption("Dummy dashboard • native Streamlit only")

# ---------- KPI ROW ----------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Revenue", "₹12.4M", "+8.2%")
col2.metric("Active Users", "18,240", "+3.1%")
col3.metric("Conversion Rate", "4.6%", "-0.4%")
col4.metric("Churn", "1.9%", "-0.2%")

st.divider()

# ---------- MAIN CONTENT ----------
left, right = st.columns([2, 1])

with left:
    st.subheader("Revenue Trend")

    dates = pd.date_range("2025-01-01", periods=30)
    revenue = np.cumsum(np.random.randint(80, 140, size=30))

    chart_df = pd.DataFrame({
        "Date": dates,
        "Revenue": revenue
    }).set_index("Date")

    st.line_chart(chart_df)

with right:
    st.subheader("User Distribution")

    user_df = pd.DataFrame({
        "Segment": ["Free", "Pro", "Enterprise"],
        "Users": [12000, 4800, 1440]
    })

    st.bar_chart(user_df.set_index("Segment"))

st.divider()

# ---------- TABLE + INSIGHTS ----------
bottom_left, bottom_right = st.columns([3, 2])

with bottom_left:
    st.subheader("Recent Transactions")

    table_df = pd.DataFrame({
        "User": ["Aman", "Riya", "Karan", "Neha", "Ishaan"],
        "Plan": ["Pro", "Free", "Enterprise", "Pro", "Free"],
        "Amount (₹)": [2400, 0, 12000, 2400, 0],
        "Status": ["Success", "Pending", "Success", "Success", "Failed"]
    })

    st.dataframe(table_df, use_container_width=True)

with bottom_right:
    st.subheader("Insights")

    st.info("Revenue growth is healthy but slowing.")
    st.warning("Conversion dipped this week.")
    st.success("Churn remains under control.")

