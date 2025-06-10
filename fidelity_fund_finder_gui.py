import yfinance as yf
import pandas as pd
import streamlit as st

# --------------------------
# Define Fidelity Fund Data
# --------------------------
fidelity_funds = {
    'FXAIX': {'name': 'Fidelity 500 Index Fund', 'goal': 'growth', 'risk': 'moderate'},
    'FSKAX': {'name': 'Fidelity Total Market Index', 'goal': 'growth', 'risk': 'moderate'},
    'FZROX': {'name': 'Fidelity ZERO Total Market Index', 'goal': 'growth', 'risk': 'moderate'},
    'FDGRX': {'name': 'Fidelity Growth Company', 'goal': 'growth', 'risk': 'high'},
    'FBALX': {'name': 'Fidelity Balanced Fund', 'goal': 'balanced', 'risk': 'moderate'},
    'FAGIX': {'name': 'Fidelity Capital & Income', 'goal': 'income', 'risk': 'high'},
    'FSICX': {'name': 'Fidelity Strategic Income', 'goal': 'income', 'risk': 'moderate'},
    'FCONX': {'name': 'Fidelity Conservative Income Bond', 'goal': 'income', 'risk': 'low'},
    'FITLX': {'name': 'Fidelity U.S. Sustainability Index Fund', 'goal': 'esg', 'risk': 'moderate'},
    'FSLEX': {'name': 'Fidelity Environment and Alternative Energy', 'goal': 'esg', 'risk': 'moderate'},
    'FSELX': {'name': 'Fidelity Select Semiconductors', 'goal': 'growth', 'risk': 'high'},
    'FSPTX': {'name': 'Fidelity Select Technology', 'goal': 'growth', 'risk': 'high'},
}

# --------------------------
# Helper Functions
# --------------------------
def is_esg(fund_name):
    keywords = ['sustainable', 'esg', 'responsible', 'green', 'environment', 'climate']
    return any(kw in fund_name.lower() for kw in keywords)

def is_fy2026_aligned(fund_name):
    keywords = ['clean', 'renewable', 'technology', 'infrastructure', 'semiconductor',
                'sustainable', 'ai', 'innovation', 'resilience', 'green', 'broadband']
    return any(kw in fund_name.lower() for kw in keywords)

# --------------------------
# Streamlit UI
# --------------------------
st.set_page_config(page_title="Fidelity Fund Finder", layout="centered")

st.title("🧠 Fidelity Fund Finder")
st.markdown("Use live data + ESG and FY2026 alignment filters to choose top Fidelity funds.")

goal = st.selectbox("1️⃣ Investment Goal", ['growth', 'income', 'balanced', 'esg'])
risk = st.selectbox("2️⃣ Risk Tolerance", ['low', 'moderate', 'high'])
want_esg = st.checkbox("✅ Prioritize ESG/Sustainable Funds")
want_fy2026 = st.checkbox("📊 Prioritize FY2026 Aligned Funds")
submit = st.button("🔍 Find My Funds")

if not submit:
    st.info("👈 Use the filters above, then click the button to see fund recommendations.")

# --------------------------
# Filtering & Logic
# --------------------------
if submit:
    filtered_funds = {
        ticker: meta for ticker, meta in fidelity_funds.items()
        if meta['goal'] == goal and meta['risk'] == risk
    }

    if not filtered_funds:
        st.warning("No funds match your criteria. Try adjusting your filters.")
    else:
        fund_data = []

        for ticker, meta in filtered_funds.items():
            try:
                fund = yf.Ticker(ticker)
                hist = fund.history(period="5y")
                if len(hist) > 0:
                    start_price = hist['Close'][0]
                    end_price = hist['Close'][-1]
                    return_pct = ((end_price - start_price) / start_price) * 100
                else:
                    return_pct = None

                info = fund.info
                expense_ratio = info.get('annualReportExpenseRatio', None)

                fund_name = meta['name']
                esg_flag = 'Yes' if is_esg(fund_name) else 'No'
                fy_flag = 'Yes' if is_fy2026_aligned(fund_name) else 'No'

                fund_data.append({
                    'Ticker': ticker,
                    'Fund Name': fund_name,
                    '5-Year Return (%)': round(return_pct, 2) if return_pct else "N/A",
                    'Expense Ratio (%)': round(expense_ratio * 100, 2) if expense_ratio else "N/A",
                    'Risk': meta['risk'],
                    'Goal': meta['goal'],
                    'ESG Fund': esg_flag,
                    'FY2026 Aligned': fy_flag
                })
            except Exception as e:
                st.error(f"Error loading {ticker}: {e}")

        df = pd.DataFrame(fund_data)

        # Apply additional filters
        if want_esg:
            df = df[df['ESG Fund'] == 'Yes']
        if want_fy2026:
            df = df[df['FY2026 Aligned'] == 'Yes']

        if df.empty:
            st.warning("No results after applying ESG/FY2026 filters.")
        else:
            st.success(f"{len(df)} fund(s) matched your criteria:")
            st.dataframe(df.sort_values(by="5-Year Return (%)", ascending=False))

            csv = df.to_csv(index=False)
            st.download_button("📥 Download CSV", csv, file_name="fidelity_fund_recommendations.csv")
