🎯 Feature Selection Report

This report documents the feature selection process performed before training the Logistic Regression model on the Pima Indians Diabetes Dataset. Features were evaluated and categorized based on their correlation strength and potential contribution to diabetes prediction.

1️⃣ Feature Selection Summary
Feature Name	Correlation with Outcome	Selection Status	Reason / Insight
Glucose	0.466	⭐ MAIN FEATURE	Shows the strongest positive linear relationship with diabetes outcome, making it the most influential predictor in the dataset.
BMI	0.293	⭐ MAIN FEATURE	Higher Body Mass Index is associated with an increased risk of diabetes.
Age	0.238	⭐ MAIN FEATURE	Diabetes risk generally increases with age, showing a positive relationship with the outcome variable.
Pregnancies	0.222	⭐ MAIN FEATURE	Shows a meaningful positive correlation with diabetes outcome.
DiabetesPedigreeFunction	0.174	🔹 MEDIUM FEATURE	Family history information provides additional predictive value for diabetes risk.
Insulin	0.131	🔹 LOW CORRELATION	Shows a weak positive relationship but may still contribute during model training.
BloodPressure	0.065	✖ LOW IMPACT	Shows a very weak linear relationship with the target variable.
SkinThickness	0.057	✖ LOW IMPACT	Shows low correlation and contains zero values representing missing measurements.

📌 Selection Criterion: Features with higher correlation values (|Correlation| ≥ 0.20) were considered important predictors. However, other medically relevant features were also retained and evaluated during Logistic Regression training.

2️⃣ Conclusion
🎯 Primary Feature: Glucose shows the strongest linear relationship with the diabetes outcome and plays an important role in prediction.
📈 Major Predictors: BMI, Age, and Pregnancies show significant positive relationships and form the core predictive features.
🔍 Supporting Features: DiabetesPedigreeFunction and Insulin provide additional medical context but have lower individual correlation strength.
⏳ Lower Correlation Features: BloodPressure and SkinThickness show weaker relationships with the outcome variable.

Based on this Pearson Correlation analysis, the selected features were considered during the training of the Logistic Regression model for diabetes prediction.
