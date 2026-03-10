# Customer Engagement & Product Utilization Analytics for Retention Strategy

## Overview
Banks increasingly recognize that customer behavior and engagement—not just demographics—determine long-term retention. Customers may appear financially strong (high balance or salary) but still churn due to low engagement, limited product adoption, or weak relationship depth with the bank.

This project evaluates retention through the lens of customer behavior and relationship strength using a dataset of 10,000 European bank customers. By focusing on engagement and product utilization, this project provides actionable insights for retention strategy design, product optimization, and customer loyalty enhancement.

## Objectives
*   Evaluate the relationship between engagement and churn.
*   Measure retention impact of product count and product mix.
*   Identify disengaged yet high-value customers ("Silent Churners").
*   Define custom Retention Key Performance Indicators (KPIs).

## Key Discoveries
- **Engagement Retention Ratio:** Inactive customers are nearly twice as likely to churn compared to active users.
- **Product Depth Anchor:** Single-product users churn heavily (27.7%), while transitioning to a second product drastically reduces churn (7.5%).
- **High-Balance Disengagement:** High account balances do not guarantee loyalty. Nearly 31.2% of high-balance, inactive customers leave the bank.

## Repository Contents
*   **`DA_project.ipynb`**: The interactive Jupyter Notebook containing the full Exploratory Data Analysis (EDA).
*   **`eda.py`**: A Python script summarizing the findings and generating the processed dataset.
*   **`app.py`**: A live interactive Streamlit web dashboard visualizing the generated KPIs and retention insights.
*   **`research_paper.md`**: A comprehensive academic deep-dive into the methodology and analytics.
*   **`executive_summary.md`**: A top-level summary tailored for stakeholders with strategic recommendations.
*   **`European_Bank.csv`**: The raw customer dataset used for the project.
*   **`processed_bank_data.csv`**: The cleaned and classified dataset utilized by the Streamlit application.

## How to Run the Dashboard
1. Ensure you have Python installed.
2. Install the necessary dependencies (Pandas, NumPy, Plotly, Streamlit):
   ```bash
   pip install pandas numpy plotly streamlit
   ```
3. Run the Streamlit application from the root directory:
   ```bash
   streamlit run app.py
   ```
4. Access the interactive web app in your browser at `http://localhost:8501`.

## Strategic Recommendations
1.  **Prioritize the "Second Product":** Shifting single-product users to a second product is the most effective defense against churn.
2.  **Launch Premium Reactivation:** High-value customers who are inactive must be identified and engaged with immediately to prevent catastrophic deposit flight.
3.  **Use the Dashboard:** Continuously monitor the retention strength panels within the application to identify low-engagement assets and proactively deploy loyalty interventions.
