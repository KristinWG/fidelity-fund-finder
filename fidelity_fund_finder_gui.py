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
# ------
