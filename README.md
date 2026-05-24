# Task2_ML_Pipeline_Churn

## End-to-End Machine Learning Pipeline for Customer Churn Prediction

This project demonstrates a complete production-ready machine learning pipeline using Scikit-learn for predicting customer churn.

---

##  Project Objective

The objective of this project is to build a reusable and production-ready ML pipeline that predicts whether a telecom customer will churn or not.

The pipeline integrates:
- Data preprocessing
- Feature engineering
- Model training
- Hyperparameter tuning
- Model evaluation
- Deployment using Gradio

---

##  Dataset

This project uses the **IBM Telco Customer Churn Dataset**.

Target variable:
- **Churn**
  - Yes → 1
  - No → 0

Features include:
- Gender
- Tenure
- Contract type
- Monthly charges
- Total charges
- Services used

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Gradio

---

## 📁 Project Structure

Task2_ML_Pipeline_Churn/
│
├── notebook.ipynb
├── app.py
├── requirements.txt
├── README.md
├── churn_pipeline.joblib
├── screenshots/


---

## 🔄 Workflow

Dataset → Data Cleaning → Train/Test Split → Preprocessing Pipeline → Model Training → GridSearchCV → Evaluation → Save Pipeline → Gradio Deployment

---

## 🧹 Data Preprocessing

Steps performed:
- Removed `customerID`
- Converted `TotalCharges` to numeric
- Encoded target variable (`Churn` → 0/1)
- Handled missing values

---

## 🧪 Train-Test Split

- Training data: 80%
- Testing data: 20%

---

## ⚙️ Preprocessing Pipeline

### Numerical Features:
- Missing value imputation (median)
- StandardScaler

### Categorical Features:
- Missing value imputation (most frequent)
- OneHotEncoding

Implemented using:
- Pipeline
- ColumnTransformer

---

## 🤖 Models Used

### 1. Logistic Regression
- Baseline model
- Fast and interpretable

### 2. Random Forest Classifier
- Ensemble model
- Better accuracy
- Handles non-linearity

---

## 🔍 Hyperparameter Tuning

Used GridSearchCV:

- Parameter tuned: `C` for Logistic Regression
- Cross-validation: 3-fold
- Metric: Accuracy

Best model selected automatically.

---

## 📈 Evaluation Metrics

- Accuracy Score
- Classification Report
- Confusion Matrix

---

## 💾 Model Saving

The final trained pipeline is saved using Joblib:

- Includes preprocessing + model
- Fully reusable for inference

File:
churn_pipeline.joblib


---

## 🌐 Deployment (Gradio App)

A Gradio web app is built for real-time predictions.

### Inputs:
- Gender
- Senior Citizen (0/1)
- Tenure
- Monthly Charges
- Total Charges
- Contract Type

### Output:
- Customer churn prediction

Run app:

python app.py

Installation
pip install -r requirements.txt

How to Run
- Open notebook in Google Colab
- Run all preprocessing + training cells
- Save model (churn_pipeline.joblib)

Run Gradio app using:

python app.py

# Future Improvements

- Try XGBoost / LightGBM
- Add feature importance visualization
- Deploy on Hugging Face Spaces
- Add probability score output in UI
- Improve UI design

# Author

Musfira Zainab

AI/ML intern

DevelopersHub Corporation

This project was built as part of an End-to-End Machine Learning Pipeline assignment using Scikit-learn and Gradio.
