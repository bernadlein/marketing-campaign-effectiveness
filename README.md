# Marketing Campaign Effectiveness (Portfolio Project)

A complete, ready-to-run portfolio project for Data Analyst roles. It compares **multi‑channel marketing performance** (Facebook, Google Ads, Email) with KPIs like **ROI%**, **CTR%**, **Conversion Rate%**, and **Cost per Conversion**.

## 🚀 What's inside
- `data/marketing_campaign_effectiveness.csv` — dummy dataset
- `powerbi/` — Power Query (M), DAX measures, and theme to build a PBIX quickly
- `analytics/analysis.py` — Python script to compute metrics and save charts
- `app.py` — Streamlit app (for Hugging Face Spaces)
- `images/` — sample charts for the README/LinkedIn
- `LICENSE`, `.gitignore`

## 📊 KPIs
- **ROI%** = (Revenue - Spend)/Spend
- **CTR%** = Clicks/Impressions
- **Conversion Rate%** = Conversions/Clicks
- **Cost per Conversion** = Spend/Conversions

## 🔧 Run locally (Python)
```bash
# 1) Create venv and install deps
python -m venv .venv && . .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2) Generate charts
python analytics/analysis.py

# 3) Launch the app
streamlit run app.py
```

## 🧠 Power BI
Open `marketing_campaign_effectiveness.csv` in Power BI, paste M and DAX from `powerbi/` per instructions in `POWERBI_README.md` (also included in your downloads).

## 🔗 Live Demo (Hugging Face Spaces)
You can deploy `app.py` to a Space for a shareable live demo of your analysis. See **Deploy to Hugging Face** below.

## 📷 Preview
![ROI by Channel](images/roi_by_channel.png)
![CTR by Channel](images/ctr_by_channel.png)
![Conversion Rate by Channel](images/conversion_rate_by_channel.png)

## 🧩 Folder structure
```
marketing-campaign-effectiveness/
├── app.py
├── analytics/
│   └── analysis.py
├── data/
│   └── marketing_campaign_effectiveness.csv
├── images/
│   ├── roi_by_channel.png
│   ├── ctr_by_channel.png
│   └── conversion_rate_by_channel.png
├── powerbi/
│   ├── power_query_m_script.pq
│   ├── powerbi_measures.dax
│   └── powerbi_theme.json
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🐙 Upload to GitHub (quick steps)
```bash
# Replace YOUR-REPO with your repo name
git init
git branch -M main
git add .
git commit -m "Initial commit: Marketing Campaign Effectiveness portfolio project"

# Create repo on GitHub (in browser) then:
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```

## 🤗 Deploy to Hugging Face (Streamlit Space)
1. Create a new **Space** → SDK: **Streamlit** → set **Public** (recommended for portfolio).
2. Push this repo to the Space:
   - If you already pushed to GitHub, you can **Add Files** in the Space UI and upload everything from this repo, **or**
   - Initialize a local Git repo pointing to the Space and push:
```bash
pip install huggingface_hub
# Login in terminal (you'll be prompted)
huggingface-cli login

# Create a new Space from UI, then copy its Git URL:
git remote add hf https://huggingface.co/spaces/YOUR-USERNAME/marketing-campaign-effectiveness
git push -u hf main
```
3. The Space will automatically build with `requirements.txt` and run `app.py`.

---

### ✉️ Suggested LinkedIn post
> New portfolio project: *Marketing Campaign Effectiveness Dashboard* 🚀  
> I analyzed multi-channel performance (Facebook, Google Ads, Email) using Python + Power BI + Streamlit.  
> Key KPIs: ROI%, CTR%, Conversion Rate%, and Cost per Conversion.  
> Live demo on Hugging Face + GitHub repo in the comments.  
> #dataanalytics #powerbi #python #streamlit #portfolio

---

**Good luck with your applications! Feel free to fork this and extend with MMM or Bayesian attribution.**