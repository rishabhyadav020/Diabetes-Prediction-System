📊 Preprocessing Report: Correlation Matrix & Feature Selection

This report presents the preprocessing analysis performed on the Pima Indians Diabetes Dataset before training the prediction model. Pearson Correlation was used to identify the relationship between each feature and the target variable (Outcome).

1️⃣ Feature Selection Summary
Feature Name	Correlation with Outcome	Selection Status	Reason
Glucose	0.466	⭐ Main Feature	Strongest positive correlation with diabetes outcome. Blood glucose level is the most influential predictor.
BMI	0.293	⭐ Main Feature	Higher BMI increases the risk of diabetes.
Age	0.238	⭐ Main Feature	Diabetes risk generally increases with age.
Pregnancies	0.222	⭐ Main Feature	Shows a significant positive relationship with the target variable.
DiabetesPedigreeFunction	0.174	🔹 Medium Feature	Family history has a moderate influence on diabetes prediction.
Insulin	0.131	🔹 Low Feature	Weak positive relationship with the outcome.
BloodPressure	0.065	✖ Low Impact	Very weak correlation with diabetes outcome.
SkinThickness	0.057	✖ Low Impact	Minimal influence due to weak correlation and missing values.

Selection Criterion: Features having |Correlation| ≥ 0.20 were selected as the most important predictors.

2️⃣ Correlation Matrix
Features	Glucose	BMI	Age	Pregnancies	BloodPressure	Outcome
Glucose	1.000	0.221	0.264	0.129	0.153	0.466
BMI	0.221	1.000	0.036	0.018	0.282	0.293
Age	0.264	0.036	1.000	0.544	0.240	0.238
Pregnancies	0.129	0.018	0.544	1.000	0.141	0.222
BloodPressure	0.153	0.282	0.240	0.141	1.000	0.065
Outcome	0.466	0.293	0.238	0.222	0.065	1.000
3️⃣ Conclusion
Glucose is the most significant feature for predicting diabetes.
BMI, Age, and Pregnancies also show strong positive relationships with the target variable.
BloodPressure, SkinThickness, and Insulin have relatively low correlation and contribute less to prediction.
Based on Pearson Correlation analysis, the selected features were used in the Logistic Regression model for diabetes prediction.
