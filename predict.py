import math

# -------- PRE-TRAINED LOGISTIC REGRESSION MODEL --------

intercept = -8.40479

weights = {
    "Pregnancies": 0.12318,
    "Glucose": 0.03516,
    "BloodPressure": -0.01329,
    "SkinThickness": 0.00061,
    "Insulin": -0.00011,
    "BMI": 0.08970,
    "DiabetesPedigree": 0.94518,
    "Age": 0.01486
}


# -------- Prediction Function --------

def predict_diabetes(patient_data):

    z = intercept

    for feature, value in patient_data.items():
        z += weights[feature] * value

    # Logistic Regression Sigmoid Function
    probability = 1 / (1 + math.exp(-z))

    return probability



# -------- Main Program --------

print("====================================")
print("     Diabetes Prediction System")
print("====================================")
print("Model Status: Ready")
print()


try:

    print("Enter Patient Details:")

    patient_data = {

        "Pregnancies": float(input("Pregnancies: ")),

        "Glucose": float(input("Glucose Level: ")),

        "BloodPressure": float(input("Blood Pressure: ")),

        "SkinThickness": float(input("Skin Thickness: ")),

        "Insulin": float(input("Insulin Level: ")),

        "BMI": float(input("BMI: ")),

        "DiabetesPedigree": float(
            input("Diabetes Pedigree Function: ")
        ),

        "Age": float(input("Age: "))
    }


    probability = predict_diabetes(patient_data)


    print("\n=========== RESULT ===========")

    print(
        f"Diabetes Risk Probability: {probability*100:.2f}%"
    )


    if probability >= 0.5:
        print("⚠️ ALERT: Diabetes Risk Detected")
        print("Patient may have diabetes.")

    else:
        print("✅ SAFE: No Diabetes Risk Detected")
        print("Patient is likely not diabetic.")


    print("==============================")



except ValueError:

    print("Error: Please enter only numerical values.")

except Exception as e:

    print("Unexpected Error:", e)