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

## 💻 How To Run

1. Download the project files.
2. Open terminal in the project folder.
3. Run:

```bash
python diabetes_prediction.py
