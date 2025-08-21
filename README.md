# 📊 Telecom Customer Churn Prediction  

## 📌 Business Problem Overview  
In the telecom industry, customers can easily switch between operators. This leads to high churn rates (15–25% annually).  
Since it costs **5–10x more to acquire a new customer than to retain an existing one**, telecom companies must focus on **customer retention**.  

This project builds an **AI-driven churn prediction system** to identify high-value customers likely to churn and provides insights into why they leave.  

---

## 🎯 Objective  
- Predict which **high-value customers** will churn in the near future.  
- Identify **key drivers of churn** to support business retention strategies.  

---

## 📂 Dataset  
- Covers **4 consecutive months** (June–September).  
- Features: usage, billing, recharge, internet, calls.  
- Goal: Predict churn in **month 9** using data from months 6–8.  

---

## 🔑 Business Logic of Churn  
- **Good Phase (Months 6–7):** Customer satisfied.  
- **Action Phase (Month 8):** Customer shows unusual behavior (complaints, reduced usage, competitor offers).  
- **Churn Phase (Month 9):** Customer exits.  

---

## 🛠 Data Preparation  
1. **Feature Engineering:** Derived recharge ratios, usage drop-offs, ARPU (Average Revenue per User).  
2. **High-Value Customers:** Top 30% based on recharge amount.  
3. **Churn Tagging:** Customers with zero usage (calls + internet) in Month 9 are tagged as churners.  
4. **Data Cleaning:** Removed irrelevant columns, imputed missing values.  

---

## 🤖 Machine Learning Approach  
- **Dimensionality Reduction:** PCA (to handle 200+ features).  
- **Models Tested:** Logistic Regression, Random Forest, XGBoost.  
- **Class Imbalance Handling:** SMOTE & weighted models.  
- **Evaluation Metrics:** Precision, Recall, F1-score, ROC-AUC (focus on Recall for churners).  

---

## 📈 Insights  
- Tenure, contract type, billing method, and data usage were **strong indicators** of churn.  
- High churners often showed **declining data usage** before exiting.  

---

## 🗂 Workflow  

```mermaid
flowchart TD
    A[📥 Data Collection] --> B[🧹 Data Cleaning & Preprocessing]
    B --> C[📊 Feature Engineering]
    C --> D[🎯 Define High-Value Customers]
    D --> E[🏷 Churn Tagging]
    E --> F[⚙️ Model Training (Logistic, RF, XGBoost)]
    F --> G[📉 Model Evaluation]
    G --> H[🚀 Deployment & Insights for Retention Teams]
