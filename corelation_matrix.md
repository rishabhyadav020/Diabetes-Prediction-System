#  Preprocessing Report: Correlation Matrix Analysis

This report presents the statistical analysis performed on the **Pima Indians Diabetes Dataset** using **Pearson Correlation**. It measures the linear relationship between each pair of variables and highlights how they correlate with the target variable (`Outcome`).

---

# Correlation Matrix (Key Features)

Below is the filtered matrix showing the relationships between the features that carry significant statistical weight for diabetes prediction.

| Features | Glucose | BMI | Age | Pregnancies | BloodPressure | Outcome |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Glucose** | **1.000** | 0.221 | 0.264 | 0.129 | 0.153 | **0.466** |
| **BMI** | 0.221 | **1.000** | 0.036 | 0.018 | 0.282 | **0.293** |
| **Age** | 0.264 | 0.036 | **1.000** | 0.544 | 0.240 | **0.238** |
| **Pregnancies** | 0.129 | 0.018 | 0.544 | **1.000** | 0.141 | **0.222** |
| **BloodPressure** | 0.153 | 0.282 | 0.240 | 0.141 | **1.000** | **0.065** |
| **Outcome** | **0.466** | **0.293** | **0.238** | **0.222** | **0.065** | **1.000** |

> ** Note:** The complete correlation matrix was generated during preprocessing. For better readability and focused analysis, only the key features with higher relevance to diabetes prediction are presented here.

---

#  Key Observations

* **Direct Predictor:** `Glucose` shares the highest linear trend with the `Outcome` variable at **0.466**.
* **Inter-feature Dependency:** A notable correlation of **0.544** exists between `Age` and `Pregnancies`, which is biologically expected. 
* **Independent Features:** `BloodPressure` shows an extremely weak correlation (**0.065**) across the dataset.
