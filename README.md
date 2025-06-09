# fidelity-fund-finder
A Streamlit app to filter Fidelity funds using live data, ESG, and FY2026 alignment

# Clone the empty repo you just created
git clone https://github.com/KristinWG/fidelity-fund-finder.git
cd fidelity-fund-finder

# Create folders and add code
mkdir app
cd app

# Save the Streamlit app
nano fidelity_fund_finder_gui.py
# (Paste the script I gave you earlier, then Ctrl+O Enter to save and Ctrl+X to exit)

# Go back to main folder and add other files
cd ..
nano requirements.txt
# Paste: streamlit, yfinance, pandas

nano .gitignore
# Paste: __pycache__/ *.pyc *.pyo .env .DS_Store

nano LICENSE
# Paste in MIT License content (optional but recommended)

# Update README
nano README.md
# Paste the README content from earlier

# Stage and push
git add .
git commit -m "Initial commit with Streamlit app"
git push origin main

