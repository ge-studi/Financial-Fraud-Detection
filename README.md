# Financial Fraud Detection System using Machine Learning & Streamlit

This project is a **Streamlit web app** that detects fraudulent financial transactions using machine learning models like Logistic Regression, Decision Trees, and XGBoost.


## 📊 Dataset

We use a synthetic financial transactions dataset (`financial_fraud_detection.csv`) with the following features:

- `step`: Hour of transaction
- `type`: Type of transaction
- `amount`: Amount involved
- `oldbalanceOrg`: Sender’s balance before
- `newbalanceOrig`: Sender’s balance after
- `oldbalanceDest`: Receiver’s balance before
- `newbalanceDest`: Receiver’s balance after
  

> Source: [Kaggle - Fraud Detection Dataset](https://www.kaggle.com/datasets/sriharshaeedala/financial-fraud-detection-dataset)


## 🧠 Model Training

- Preprocessing: Label encoding, feature scaling (StandardScaler)
- Models used: 
  - Logistic Regression
  - Decision Tree Classifier
  - XGBoost Classifier
- Best model selected based on F1-score using cross-validation
- Models and scaler are saved using `joblib`

🛠️ Dependencies
    
    pandas
    
    numpy
    
    scikit-learn
    
    xgboost
    
    streamlit
    
    joblib
    
    matplotlib


## 🚀 Streamlit App

A user-friendly UI allows input of transaction data and predicts whether it's fraudulent or legitimate.


## ▶️ Run the App

To run the Streamlit app locally:

```bash
streamlit run app.py



