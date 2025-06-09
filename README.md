import yfinance as yf
import pandas as pd
import streamlit as st

# Clone your GitHub repo
git clone https://github.com/KristinWG/fidelity-fund-finder.git
cd fidelity-fund-finder

# Create the app folder and enter it
mkdir app
cd app

# Create the Streamlit app file
nano fidelity_fund_finder_gui.py
# (Paste the full Streamlit script starting with: "import streamlit as st")
# Save with: Ctrl+O, Enter, then Ctrl+X

# Go back to main folder
cd ..

# Create the requirements.txt file
nano requirements.txt
# Paste these lines:
# streamlit
# yfinance
# pandas

# Create a .gitignore file
nano .gitignore
# Paste:
# __pycache__/
# *.pyc
# *.pyo
# .env
# .DS_Store

# Optional: Create LICENSE (MIT recommended)
nano LICENSE
# Paste MIT License text (from https://choosealicense.com/licenses/mit/)

# Update or create a README.md
nano README.md
# Paste:
# Fidelity Fund Finder
# A Streamlit app to filter Fidelity funds using live data, ESG, and FY2026 alignment

# Stage and push all files to GitHub
git add .
git commit -m "Initial commit with working Streamlit app"
git push origin main
