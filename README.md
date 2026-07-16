# Diabetes Prediction System (Pure Python Mode)

A lightweight Machine Learning project that predicts the probability of diabetes in a patient based on medical parameters.

This project uses a **Logistic Regression classification model**. The trained model weights are implemented directly using Python mathematical formulas (Sigmoid Function), allowing the application to run without external dependencies like pandas or scikit-learn.

## 🚀 Features

- **Zero Dependencies:** Runs using standard Python only.
- **Machine Learning Based:** Uses Logistic Regression classification algorithm.
- **Mathematical Model:** Implements Logistic Regression prediction using Sigmoid function.
- **Interactive CLI:** Takes patient health parameters as input and predicts diabetes risk percentage.

## 📊 Dataset & Algorithm

- **Dataset:** Kaggle Pima Indians Diabetes Dataset (768 patient records).
- **Algorithm Used:** Logistic Regression (Classification Algorithm).
- **Model Accuracy:** Approximately 77% during testing.

## 📋 Parameters Used

The model predicts diabetes risk using these 8 parameters:

1. Pregnancies
2. Glucose Level
3. Blood Pressure
4. Skin Thickness
5. Insulin Level
6. BMI
7. Diabetes Pedigree Function
8. Age

🤖 Machine Learning Models Considered

Although several Machine Learning algorithms can be used for diabetes prediction, this project uses Logistic Regression because it is well-suited for binary classification and provides good performance on the Pima Indians Diabetes Dataset.

Machine Learning Model	Status	Reason
Logistic Regression	✅ Used	Selected because it is suitable for binary classification (Diabetic / Non-Diabetic), easy to implement, interpretable, and achieved approximately 77% accuracy.
Decision Tree	❌ Not Used	Can overfit the training data and produce less stable predictions.
Random Forest	❌ Not Used	More computationally expensive and less interpretable than Logistic Regression.
Support Vector Machine (SVM)	❌ Not Used	Requires parameter tuning and takes longer to train.
K-Nearest Neighbors (KNN)	❌ Not Used	Prediction is slower because it compares each test sample with all training samples.
Naive Bayes	❌ Not Used	Assumes feature independence, which may not hold true for medical datasets.
Artificial Neural Network (ANN)	❌ Not Used	Requires more data and computational resources for effective training.
XGBoost	❌ Not Used	Powerful but more complex to implement and tune for this project.
Linear Regression	❌ Not Used	Designed for regression problems, not binary classification.
K-Means Clustering	❌ Not Used	Unsupervised learning algorithm, whereas diabetes prediction is a supervised classification task.
