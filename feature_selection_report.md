# 📊 Preprocessing Report: Correlation Matrix & Feature Selection

This report presents the preprocessing analysis performed on the **Pima Indians Diabetes Dataset** before training the Logistic Regression model. Pearson Correlation was used to measure the relationship between each feature and the target variable (**Outcome**) and to identify the most important features for diabetes prediction.

---

## 1️⃣ Feature Selection Summary

| Feature Name | Correlation with Outcome | Selection Status | Reason |
| :--- | :---: | :---: | :--- |
| **Glucose** | **0.466** | ⭐ **MAIN FEATURE** | Highest positive correlation with diabetes outcome, making it the most influential predictor. |
| **BMI** | **0.293** | ⭐ **MAIN FEATURE** | Higher Body Mass Index is associated with an increased risk of diabetes. |
| **Age** | **0.238** | ⭐ **MAIN FEATURE** | Diabetes risk generally increases with age. |
| **Pregnancies** | **0.222** | ⭐ **MAIN FEATURE** | Shows a significant positive relationship with the target variable. |
| **DiabetesPedigree** | **0.174** | 🔹 **MEDIUM FEATURE** | Family history has a moderate influence on diabetes prediction. |
| **Insulin** | **0.131** | 🔹 **LOW FEATURE** | Weak positive relationship with the target variable. |
| **BloodPressure** | **0.065** | ✖ **LOW IMPACT** | Very weak correlation with the target variable. |
| **SkinThickness** | **0.057** | ✖ **LOW IMPACT** | Minimal influence due to weak correlation and the presence of missing/zero values. |

> **📌 Selection Criterion:** Features with **|Correlation| ≥ 0.20** were selected as the primary predictors for the Logistic Regression model.

---

## 2️⃣ Correlation Matrix (Key Features)

| Features | Glucose | BMI | Age | Pregnancies | BloodPressure | Outcome |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Glucose** | **1.000** | 0.221 | 0.264 | 0.129 | 0.153 | **0.466** |
| **BMI** | 0.221 | **1.000** | 0.036 | 0.018 | 0.282 | **0.293** |
| **Age** | 0.264 | 0.036 | **1.000** | 0.544 | 0.240 | **0.238** |
| **Pregnancies** | 0.129 | 0.018 | 0.544 | **1.000** | 0.141 | **0.222** |
| **BloodPressure** | 0.153 | 0.282 | 0.240 | 0.141 | **1.000** | **0.065** |
| **Outcome** | **0.466** | **0.293** | **0.238** | **0.222** | **0.065** | **1.000** |

> **Note:** The complete correlation matrix was generated during preprocessing. For better readability, only the key features with the highest relevance to diabetes prediction are presented here.

---

## 3️⃣ Conclusion

- **Glucose** is the most important feature for predicting diabetes.
- **BMI**, **Age**, and **Pregnancies** also show significant positive correlations with the target variable.
- **DiabetesPedigree** and **Insulin** provide additional predictive information but have comparatively lower influence.
- **BloodPressure** and **SkinThickness** show weak correlations and contribute less to the prediction model.

**Based on the Pearson Correlation analysis, the selected features were used to train the Logistic Regression model for diabetes prediction.**
