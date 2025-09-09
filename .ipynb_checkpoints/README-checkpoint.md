# Car Price Prediction - Streamlit App

Project ID: PTID-CDS-AUG-25-2990

Files:
- app.py                      : Streamlit application
- car_price_pipeline.pkl      : Saved preprocessing + model pipeline
- requirements.txt            : Python dependencies

How to run locally:
1. pip install -r requirements.txt
2. streamlit run app.py

Usage:
- Batch mode: upload a CSV file that contains the same feature columns used during training.
- Single mode: use the form for a quick single-row prediction (may cause errors if pipeline expects extra columns).

Note:
Ensure 'car_price_pipeline.pkl' is present in the same folder as app.py.
