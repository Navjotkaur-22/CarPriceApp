# app.py
import streamlit as st
import pandas as pd
import os
import cloudpickle

st.set_page_config(page_title="Car Price Predictor", layout="centered")
st.title("🚗 Car Price Prediction")
st.markdown(
    "Upload a CSV with the same feature columns used during training, or use the manual form for a single estimate."
)

# reliable model path (works regardless of CWD)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "car_price_pipeline.pkl")

# Load model
if not os.path.exists(MODEL_PATH):
    st.error(f"Model file not found: {MODEL_PATH}. Please put 'car_price_pipeline.pkl' in the app folder.")
    st.stop()

# debug prints (optional — safe to keep)
print("DEBUG >>> Current Working Directory:", os.getcwd())
print("DEBUG >>> Files in CWD:", os.listdir("."))
print("DEBUG >>> MODEL_PATH:", MODEL_PATH)
print("DEBUG >>> Exists?:", os.path.exists(MODEL_PATH))

# Load with cloudpickle (handles custom objects better)
try:
    with open(MODEL_PATH, "rb") as f:
        pipeline = cloudpickle.load(f)
except Exception as e:
    st.error(f"Failed to load model: {e}")
    st.stop()

st.sidebar.header("Mode")
mode = st.sidebar.radio("Choose mode", ["Batch (CSV upload)", "Single input (form)"])

# -----------------------
# Batch CSV upload mode
# -----------------------
if mode == "Batch (CSV upload)":
    uploaded_file = st.file_uploader(
        "Upload CSV file (must contain all features expected by the model)",
        type=["csv"],
    )
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Preview of uploaded data:")
            st.dataframe(df.head())

            if st.button("Predict batch"):
                preds = pipeline.predict(df)
                df_out = df.copy()
                df_out["predicted_price"] = preds
                st.success("Predictions complete ✅")
                st.dataframe(df_out.head())
                csv = df_out.to_csv(index=False).encode("utf-8")
                st.download_button(
                    "Download predictions CSV",
                    data=csv,
                    file_name="predictions.csv",
                    mime="text/csv",
                )
        except Exception as e:
            st.error(f"Failed to read or predict: {e}")

# -----------------------
# Single input (form) mode
# -----------------------
else:
    st.write(
        "Use the manual form to give a quick single estimate. (If you get errors about missing columns, use CSV mode.)"
    )

    # Categorical inputs — adjust options if your training data used different values
    make = st.selectbox(
        "Make",
        sorted(
            [
                "unknown",
                "alfa-romero",
                "audi",
                "bmw",
                "chevrolet",
                "dodge",
                "honda",
                "isuzu",
                "jaguar",
                "mazda",
                "mercedes-benz",
                "mercury",
                "mitsubishi",
                "nissan",
                "peugot",
                "plymouth",
                "porsche",
                "renault",
                "saab",
                "subaru",
                "toyota",
                "volkswagen",
                "volvo",
            ]
        ),
    )
    fuel_type = st.selectbox("Fuel Type", ["gas", "diesel"])
    aspiration = st.selectbox("Aspiration", ["std", "turbo"])
    num_of_doors = st.selectbox("Number of doors", ["two", "four", "unknown"])
    body_style = st.selectbox("Body style", ["hardtop", "wagon", "sedan", "hatchback", "convertible"])
    drive_wheels = st.selectbox("Drive Wheels", ["rwd", "fwd", "4wd"])
    engine_location = st.selectbox("Engine Location", ["front", "rear"])

    # Numeric inputs (defaults chosen for convenience)
    wheel_base = st.number_input("Wheel Base", min_value=0.0, value=95.0)
    length = st.number_input("Length", min_value=0.0, value=170.0)
    width = st.number_input("Width", min_value=0.0, value=65.0)
    height = st.number_input("Height", min_value=0.0, value=50.0)
    curb_weight = st.number_input("Curb Weight", min_value=0.0, value=2000.0)
    engine_size = st.number_input("Engine Size", min_value=0.0, value=100.0)
    horsepower = st.number_input("Horsepower", min_value=0.0, value=100.0)
    city_mpg = st.number_input("City MPG", min_value=0.0, value=20.0)
    highway_mpg = st.number_input("Highway MPG", min_value=0.0, value=25.0)

    # Build a single-row DataFrame with exact column names expected by your pipeline
    input_dict = {
        "make": [make],
        "fuel-type": [fuel_type],
        "aspiration": [aspiration],
        "num-of-doors": [num_of_doors],
        "body-style": [body_style],
        "drive-wheels": [drive_wheels],
        "engine-location": [engine_location],
        "wheel-base": [wheel_base],
        "length": [length],
        "width": [width],
        "height": [height],
        "curb-weight": [curb_weight],
        "engine-size": [engine_size],
        "horsepower": [horsepower],
        "city-mpg": [city_mpg],
        "highway-mpg": [highway_mpg],
    }

    X_single = pd.DataFrame.from_dict(input_dict)
    st.write("Input preview:")
    st.table(X_single.T)

    if st.button("Predict single"):
        try:
            pred = pipeline.predict(X_single)[0]
            st.success(f"Predicted price: ₹ {round(pred, 2)}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
            st.info("If you see missing column errors, use a CSV with exact column names from training.")

# Footer
st.markdown("---")
st.caption("Note: This app is for demonstration. Model trained for educational project (PRCP-1017 / PTID-CDS-AUG-25-2990).")

