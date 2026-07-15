import math
import io

csv_data = """Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigree,Age,Outcome
6,148,72,35,0,33.6,0.627,50,1
1,85,66,29,0,26.6,0.351,31,0
8,183,64,0,0,23.3,0.672,32,1
1,89,66,23,94,28.1,0.167,21,0
0,137,40,35,168,43.1,2.288,33,1
5,116,74,0,0,25.6,0.201,30,0
3,78,50,32,88,31.0,0.248,26,1
10,115,0,0,0,35.3,0.134,29,0
2,197,70,45,543,30.5,0.158,53,1
8,125,96,0,0,0.0,0.232,54,1
4,110,92,0,0,37.6,0.191,30,0
10,168,74,0,0,38.0,0.537,34,1
1,103,30,38,83,43.3,0.183,33,0
1,189,60,23,846,30.1,0.398,59,1
5,166,72,19,175,25.8,0.587,51,1
"""

# ========================================================
# PURE PYTHON CORE MATH FUNCTIONS
# ========================================================

def calculate_correlation(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    num = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    den_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    den_y = sum((y[i] - mean_y) ** 2 for i in range(n))
    
    if den_x == 0 or den_y == 0:
        return 0
    return num / math.sqrt(den_x * den_y)

# Data Parsing
lines = csv_data.strip().split("\n")
headers = lines[0].strip().split(",")
data_rows = [line.strip().split(",") for line in lines[1:] if line.strip()]

columns = {h: [] for h in headers}
for row in data_rows:
    for i, val in enumerate(row):
        columns[headers[i]].append(float(val))
        
outcome = columns["Outcome"]

# --- DYNAMIC CORRELATION MATRIX PRINT ---
print("\n========== CORRELATION MATRIX ==========")
features = headers

# Header row display
print(f"{'Feature':<20}", end=" ")
for h in features:
    print(f"{h:<12}", end=" ")
print()

# Row values display
for f1 in features:
    print(f"{f1:<20}", end=" ")
    for f2 in features:
        corr = calculate_correlation(columns[f1], columns[f2])
        print(f"{corr:<12.3f}", end=" ")
    print()
print("=" * 130)

# --- FEATURE SELECTION REPORT ---
print("\n========== FEATURE SELECTION ==========")
rankings = []
for h in headers:
    if h != "Outcome":
        correlation = calculate_correlation(columns[h], outcome)
        rankings.append((h, correlation))

rankings.sort(key=lambda x: abs(x[1]), reverse=True)

selected_features = []
print("\nFeature Importance with Diabetes Outcome:")
for feature, value in rankings:
    if abs(value) >= 0.2:
        selected_features.append(feature)
        print(f"✔ {feature:<25} Correlation = {value:.3f} (Important)")
    else:
        print(f"✖ {feature:<25} Correlation = {value:.3f} (Less Important)")

print("\nFinal Selected Features:")
print(selected_features)
print("=" * 50)
print("\n")


# ========================================================
# PRE-TRAINED LOGISTIC REGRESSION MODEL (Prediction Logic)
# ========================================================

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

def predict_diabetes(patient_data):
    z = intercept
    for feature, value in patient_data.items():
        z += weights[feature] * value

    probability = 1 / (1 + math.exp(-z))
    return probability

# -------- Main Input Program --------
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
        "DiabetesPedigree": float(input("Diabetes Pedigree Function: ")),
        "Age": float(input("Age: "))
    }

    probability = predict_diabetes(patient_data)

    print("\n=========== RESULT ===========")
    print(f"Diabetes Risk Probability: {probability*100:.2f}%")

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
