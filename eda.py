import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Load dataset
df = pd.read_csv('European_Bank.csv')

def summarize_data(df):
    print("=== Dataset Info ===")
    df.info()
    print("\n=== Missing Values ===")
    print(df.isnull().sum())
    print("\n=== Head ===")
    print(df.head())
    print("\n=== Summary Stats ===")
    print(df.describe())

    # 1. Engagement Classification
    # Active engaged customers: IsActiveMember == 1
    # Inactive disengaged customers: IsActiveMember == 0
    # Active but low-product customers: IsActiveMember == 1 & NumOfProducts == 1
    # Inactive high-balance customers: IsActiveMember == 0 & Balance > high_threshold (e.g. median of non-zero balance)
    
    non_zero_balance_median = df[df['Balance'] > 0]['Balance'].median()
    df['Profile'] = 'Other'
    df.loc[(df['IsActiveMember'] == 1) & (df['NumOfProducts'] > 1), 'Profile'] = 'Active Engaged'
    df.loc[(df['IsActiveMember'] == 0) & (df['NumOfProducts'] == 1), 'Profile'] = 'Inactive Disengaged'
    df.loc[(df['IsActiveMember'] == 1) & (df['NumOfProducts'] <= 1), 'Profile'] = 'Active Low-Product'
    df.loc[(df['IsActiveMember'] == 0) & (df['Balance'] >= non_zero_balance_median), 'Profile'] = 'Inactive High-Balance'

    print("\n=== Profile Distribution ===")
    print(df['Profile'].value_counts())
    print("\n=== Profile Churn Rate ===")
    print(df.groupby('Profile')['Exited'].mean())

    # 2. Product Utilization Analysis
    print("\n=== Churn by NumOfProducts ===")
    print(df.groupby('NumOfProducts')['Exited'].agg(['count', 'mean']))

    # 3. Financial Commitment vs Engagement
    # Salary-balance mismatch (high salary, low balance)
    high_salary_threshold = df['EstimatedSalary'].median()
    low_balance_threshold = df['Balance'].median() # mostly zero, let's say 0
    
    df['Salary_Balance_Mismatch'] = np.where((df['EstimatedSalary'] > high_salary_threshold) & (df['Balance'] == 0), 1, 0)
    print("\n=== Salary-Balance Mismatch Churn ===")
    print(df.groupby('Salary_Balance_Mismatch')['Exited'].agg(['count', 'mean']))
    
    # 4. KPIs
    # Engagement Retention Ratio: active vs inactive churn comparison
    active_churn = df[df['IsActiveMember'] == 1]['Exited'].mean()
    inactive_churn = df[df['IsActiveMember'] == 0]['Exited'].mean()
    print(f"\nEngagement Retention Ratio (Inactive Churn / Active Churn): {inactive_churn / active_churn:.2f}")

    # Product Depth Index: ratio of products used vs loyalty
    # Let's say churn for multi-product vs single product
    single_prod_churn = df[df['NumOfProducts'] == 1]['Exited'].mean()
    multi_prod_churn = df[df['NumOfProducts'] > 1]['Exited'].mean()
    print(f"Product Depth Index (Single Prod Churn / Multi Prod Churn): {single_prod_churn / multi_prod_churn:.2f}")

    # High-Balance Disengagement Rate: premium inactive churn
    high_bal_inactive_churn = df[(df['Balance'] >= non_zero_balance_median) & (df['IsActiveMember'] == 0)]['Exited'].mean()
    print(f"High-Balance Disengagement Rate: {high_bal_inactive_churn:.2%}")

    # Credit Card Stickiness Score
    cc_churn = df[df['HasCrCard'] == 1]['Exited'].mean()
    no_cc_churn = df[df['HasCrCard'] == 0]['Exited'].mean()
    print(f"Credit Card Stickiness Score (No CC churn / CC Churn): {no_cc_churn / cc_churn:.2f}")
    
    # Save the processed data for Streamlit
    df.to_csv('processed_bank_data.csv', index=False)
    print("\nSaved processed_bank_data.csv for Streamlit.")

if __name__ == '__main__':
    summarize_data(df)
