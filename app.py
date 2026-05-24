import gradio as gr
import pandas as pd
import joblib

model = joblib.load("churn_pipeline.joblib")

# Get expected columns from trained model
expected_columns = model.feature_names_in_

def predict_churn(
    gender,
    seniorcitizen,
    tenure,
    monthlycharges,
    totalcharges,
    contract
):

    # Create empty row with ALL required columns
    input_dict = {col: 0 for col in expected_columns}

    # Fill only known fields from UI
    input_dict["gender"] = gender
    input_dict["SeniorCitizen"] = seniorcitizen
    input_dict["tenure"] = tenure
    input_dict["MonthlyCharges"] = monthlycharges
    input_dict["TotalCharges"] = totalcharges
    input_dict["Contract"] = contract

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Predict
    prediction = model.predict(input_df)[0]

    return (
        "Customer is likely to churn."
        if prediction == 1
        else "Customer is not likely to churn."
    )

interface = gr.Interface(
    fn=predict_churn,
    inputs=[
        gr.Dropdown(["Male", "Female"], label="Gender"),
        gr.Number(label="Senior Citizen (0 or 1)"),
        gr.Number(label="Tenure"),
        gr.Number(label="Monthly Charges"),
        gr.Number(label="Total Charges"),
        gr.Dropdown(["Month-to-month", "One year", "Two year"], label="Contract")
    ],
    outputs="text",
    title="Customer Churn Prediction"
)

interface.launch(share=True)
