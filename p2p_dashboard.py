import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Setup Page Config
st.set_page_config(page_title="Procurement & P2P Dashboard", layout="wide")
st.title("🛒 Procurement & P2P Performance Dashboard")

# 2. Mock Data Generation (Replace this with your SQL/Excel connection)
data = {
    'Supplier': ['GlobalCorp', 'TechSupplies', 'OfficeMax', 'LogisticsInc', 'GlobalCorp'],
    'Spend': [50000, 12000, 5000, 25000, 45000],
    'Status': ['Paid', 'Pending', 'Paid', 'Late', 'Paid'],
    'Cycle_Time_Days': [5, 12, 3, 15, 6],
    'Category': ['Raw Materials', 'IT Hardware', 'Office', 'Freight', 'Raw Materials']
}
df = pd.DataFrame(data)

# 3. Sidebar Filters
st.sidebar.header("Filter Data")
selected_category = st.sidebar.multiselect(
    "Select Category", df['Category'].unique(), default=df['Category'].unique())
filtered_df = df[df['Category'].isin(selected_category)]

# 4. Top Level Metrics (KPIs)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Spend", f"${filtered_df['Spend'].sum():,}")
with col2:
    st.metric("Avg PO Cycle Time",
              f"{filtered_df['Cycle_Time_Days'].mean():.1f} Days")
with col3:
    pending_count = len(filtered_df[filtered_df['Status'] == 'Pending'])
    st.metric("Pending Invoices", pending_count)

st.divider()

# 5. Charts
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Spend by Supplier")
    fig_spend = px.bar(filtered_df, x='Supplier', y='Spend',
                       color='Category', barmode='group')
    st.plotly_chart(fig_spend, use_container_width=True)

with col_b:
    st.subheader("Invoice Status Distribution")
    fig_pie = px.pie(filtered_df, names='Status', values='Spend', hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

# 6. Data Table
st.subheader("Detailed Process View")
st.dataframe(filtered_df, use_container_width=True)
