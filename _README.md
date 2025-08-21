# 📡 Telecom Customer Churn Prediction

## 🚀 Project Overview
In the telecom industry, **customer churn** (when customers leave one operator for another) is a major challenge, with annual churn rates of **15–25%**.  
Since it costs **5–10x more** to acquire a new customer than to retain an existing one, predicting churn is critical for business sustainability.  

This project uses **machine learning** to:
- Predict which **high-value customers** are likely to churn.
- Identify the **key factors driving churn**.
- Provide actionable insights for **customer retention strategies**.

---

## 🏷️ Business Problem
- **Objective**: Predict churn in the 9th month using customer data from the first 3 months.  
- **Focus**: High-value customers (top 30% by recharge amount).  
- **Definition of churn**: No outgoing/incoming calls **AND** no mobile internet usage in the 9th month.  

---

## 📊 Dataset
- **Source**: Telco customer-level dataset  
- **Time span**: June – September (4 months)  
- **Features**: Call usage, recharge patterns, internet usage, customer demographics  
- **Target variable**: Churn (1 = churned, 0 = not churned)  

---

## 🔄 Workflow

```mermaid
flowchart TD
    A[📂 Load Data] --> B[🧹 Data Cleaning & Preprocessing]
    B --> C[📊 Exploratory Data Analysis]
    C --> D[⚙️ Feature Engineering]
    D --> E[📉 PCA for Dimensionality Reduction]
    E --> F[🤖 Model Training <br/> (Logistic, RF, XGBoost)]
    F --> G[📈 Model Evaluation <br/> (ROC, Recall, AUC)]
    G --> H[🔍 Feature Importance & Insights]
    H --> I[💡 Business Recommendations]
