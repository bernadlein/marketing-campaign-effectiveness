import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Marketing Campaign Effectiveness", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data/marketing_campaign_effectiveness.csv", parse_dates=["Start_Date","End_Date"])
    df['CTR_%'] = (df['Clicks'] / df['Impressions']) * 100
    df['Conversion_Rate_%'] = (df['Conversions'] / df['Clicks']) * 100
    df['ROI_%'] = ((df['Revenue_USD'] - df['Spend_USD']) / df['Spend_USD']) * 100
    df['Cost_per_Conversion'] = df['Spend_USD'] / df['Conversions']
    return df

df = load_data()

st.title("📊 Marketing Campaign Effectiveness")
st.caption("Portfolio demo — Python + Streamlit")

# Sidebar filters
channels = st.sidebar.multiselect("Filter Channel", sorted(df["Channel"].unique()), default=sorted(df["Channel"].unique()))
min_date, max_date = df["Start_Date"].min(), df["End_Date"].max()
date_range = st.sidebar.date_input("Date range", (min_date, max_date), min_value=min_date, max_value=max_date)

f = (df["Channel"].isin(channels)) & (df["Start_Date"] >= pd.to_datetime(date_range[0])) & (df["End_Date"] <= pd.to_datetime(date_range[1]))
fdf = df.loc[f].copy()

# KPIs
col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Total Spend", f"${fdf['Spend_USD'].sum():,.0f}")
col2.metric("Total Revenue", f"${fdf['Revenue_USD'].sum():,.0f}")
col3.metric("ROI %", f"{( (fdf['Revenue_USD'].sum()-fdf['Spend_USD'].sum())/max(fdf['Spend_USD'].sum(),1) )*100:,.1f}%")
col4.metric("CTR %", f"{(fdf['Clicks'].sum()/max(fdf['Impressions'].sum(),1))*100:,.2f}%")
col5.metric("Conversion Rate %", f"{(fdf['Conversions'].sum()/max(fdf['Clicks'].sum(),1))*100:,.2f}%")
col6.metric("Cost/Conversion", f"${(fdf['Spend_USD'].sum()/max(fdf['Conversions'].sum(),1)):,.2f}")

st.divider()

# Charts
left, right = st.columns(2)

with left:
    st.subheader("ROI % by Channel")
    fig1 = plt.figure(figsize=(6,4))
    fdf.groupby("Channel")["ROI_%"].mean().sort_values().plot(kind="bar")
    plt.ylabel("ROI (%)")
    st.pyplot(fig1, clear_figure=True)

with right:
    st.subheader("Cost per Conversion by Channel")
    fig2 = plt.figure(figsize=(6,4))
    fdf.groupby("Channel")["Cost_per_Conversion"].mean().sort_values().plot(kind="bar")
    plt.ylabel("Cost per Conversion ($)")
    st.pyplot(fig2, clear_figure=True)

st.subheader("Campaign Table")
st.dataframe(fdf.sort_values("ROI_%", ascending=False).reset_index(drop=True))