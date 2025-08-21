# Customer Churn Prediction 📉

## Business Problem Overview 🎯

In the highly competitive telecom industry, providers face an average annual churn rate of 15-25%. Acquiring a new customer costs 5-10 times more than retaining an existing one, making **customer retention** a top priority. For many operators, retaining high-profitability customers is the number one business goal.

This project aims to help a leading telecom firm reduce customer churn by building a predictive model to identify customers at high risk of leaving. The model will also identify the main indicators of churn, allowing the company to take proactive steps to retain valuable customers.

## Understanding and Defining Churn 🤔

### Postpaid vs. Prepaid Models

* **Postpaid**: Customers are billed after using services. Churn is explicit, as users must terminate their contracts.
* **Prepaid**: Customers pay in advance. Churn is harder to define, as users can simply stop using the service without notice. This is the more common model in the Indian and Southeast Asian markets, which are the focus of this project.

### Definitions of Churn
Churn can be defined in several ways:
* **Revenue-based churn**: Customers who don't generate revenue over a given period.
* **Usage-based churn**: Customers who have no incoming or outgoing usage (calls, internet, etc.).

This project will use the **usage-based definition** to identify churners.

## Project Goals 🚀

The primary objectives of this project are:
1.  **Predict Churn**: Build a model to predict whether a high-value customer will churn in the near future.
2.  **Identify Churn Indicators**: Use a separate, interpretable model to identify the key variables that are strong predictors of churn.
3.  **Recommend Retention Strategies**: Suggest actionable strategies to manage and reduce customer churn based on the model's findings.

### High-Value Churn

Since approximately 80% of revenue comes from the top 20% of customers, this project will focus exclusively on predicting churn for **high-value customers**.

## Customer Behavior During Churn 🚶‍♂️

Customer churn is typically a gradual process with three distinct phases:

1.  **The 'Good' Phase**: The customer is satisfied with the service and exhibits normal usage patterns.
2.  **The 'Action' Phase**: The customer's experience declines due to competitor offers, service quality issues, or billing problems. Their behavior may change, signaling a high risk of churn. This is the crucial phase for intervention.
3.  **The 'Churn' Phase**: The customer stops using the service and is officially considered churned.

```mermaid
graph TD
    A[Good Phase] --> B(Action Phase);
    B --> C{Churn Phase};
    subgraph Customer Lifecycle
        A
        B
        C
    end
    style A fill:#d4edda,stroke:#c3e6cb
    style B fill:#fff3cd,stroke:#ffeeba
    style C fill:#f8d7da,stroke:#f5c6cb
