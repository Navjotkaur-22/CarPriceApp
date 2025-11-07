🚗 Car Price Prediction App

An interactive **Machine Learning Web App** built with **Streamlit**, that predicts the **price of a car** based on its technical and categorical attributes.  
This project showcases an **end-to-end Data Science workflow** — from data preprocessing and model training to live deployment with a CSV-first user interface.

🌐 Live Demo  
👉 [Car Price Prediction – Streamlit App](https://carpriceapp-vajabjeanhumcu5gyqhehn.streamlit.app/)

[![Launch App](https://img.shields.io/badge/OPEN%20APP-black?style=for-the-badge&logo=streamlit)](https://carpriceapp-vajabjeanhumcu5gyqhehn.streamlit.app/)

🧠 Project Overview  
This application allows users to:

- Upload a **CSV file** for instant multi-row predictions (CSV-first UI)  
- Automatically handle feature scaling, encoding, and schema validation  
- Use a **pre-trained ML pipeline (Random Forest + preprocessing)**  
- Optionally test a **single manual input row** for quick prediction  

🧩 Features  
✅ CSV upload with data preview  
✅ Schema auto-validation (checks missing/extra columns)  
✅ OneHot + StandardScaler preprocessing pipeline  
✅ Trained **RandomForestRegressor (n_estimators = 600)**  
✅ Real-time price predictions with downloadable CSV output  
✅ User-friendly Streamlit interface  

🧮 Input Parameters  
24+ technical and categorical features including:  
`make, fuel-type, aspiration, num-of-doors, body-style, drive-wheels, engine-location, wheel-base, length, width, height, curb-weight, engine-size, horsepower, city-mpg, highway-mpg, etc.`  

📊 Dataset Summary  

- **Source:** UCI Machine Learning Repository (Automobile Dataset)  
- **Rows:** ~205 (after preprocessing)  
- **Features:** 24 predictors  
- **Target:** price  
- **Split:** 80/20 (train/test)  

🧰 Tech Stack  

- 🐍 Python 3.11 +  
- 📊 pandas · numpy · scikit-learn  
- 🎨 Streamlit (Interactive Web App)  
- 💾 cloudpickle · joblib (Model Serialization)  
- ☁️ GitHub + Streamlit Cloud (Deployment)  

📈 Model Metrics (Validation)

| Metric | Score |
|:-------|:------:|
| **R²** | `0.XXX` |
| **MAE** | `XXXX.X` |
| **RMSE** | `XXXX.X` |

🧩 Deployment  
Deployed using **Streamlit Cloud** and connected to this GitHub repository.  
The model is serialized via `cloudpickle` ensuring consistent pipeline behavior during app execution.

🚀 How to Run Locally  

```bash
# Clone this repository
git clone https://github.com/Navjotkaur-22/Car-Price-Prediction-App.git
cd Car-Price-Prediction-App

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

✨ Author

👩🏻‍💻 Navjot Kaur
🎓 MSc (IT) | Certified Data Scientist | Streamlit Developer
📍 Jalandhar, Punjab, India

🌐 Connect with me:

💼 GitHub – Navjotkaur-22

🔗 LinkedIn – Navjot Kaur

💬 Upwork – Navjot Kaur
