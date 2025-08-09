import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "marketing_campaign_effectiveness.csv"
OUT_DIR = Path(__file__).resolve().parents[1] / "images"
OUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH, parse_dates=["Start_Date","End_Date"])

# KPI calculations
df['CTR_%'] = (df['Clicks'] / df['Impressions']) * 100
df['Conversion_Rate_%'] = (df['Conversions'] / df['Clicks']) * 100
df['ROI_%'] = ((df['Revenue_USD'] - df['Spend_USD']) / df['Spend_USD']) * 100
df['Cost_per_Conversion'] = df['Spend_USD'] / df['Conversions']

# ROI by channel
plt.figure(figsize=(6,4))
df.groupby("Channel")["ROI_%"].mean().sort_values().plot(kind="bar")
plt.title("Average ROI by Channel")
plt.ylabel("ROI (%)")
plt.tight_layout()
plt.savefig(OUT_DIR / "roi_by_channel.png")
plt.close()

# CTR by channel
plt.figure(figsize=(6,4))
df.groupby("Channel")["CTR_%"].mean().sort_values().plot(kind="bar")
plt.title("Average CTR by Channel")
plt.ylabel("CTR (%)")
plt.tight_layout()
plt.savefig(OUT_DIR / "ctr_by_channel.png")
plt.close()

# Conversion rate by channel
plt.figure(figsize=(6,4))
df.groupby("Channel")["Conversion_Rate_%"].mean().sort_values().plot(kind="bar")
plt.title("Average Conversion Rate by Channel")
plt.ylabel("Conversion Rate (%)")
plt.tight_layout()
plt.savefig(OUT_DIR / "conversion_rate_by_channel.png")
plt.close()