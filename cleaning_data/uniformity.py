import pandas as pd
import datetime as dt

def main():
    # Read dataset
    banking_df = pd.read_csv('../datasets/cleaning_datasets/banking_dirty.csv')

    # Understand avg account size - skeleton code
    # bank_account_size(banking_df)

    # Understand customer age group
    bank_customer_age_group(banking_df)

    # Impute missing customer and fill accounts with missing account data
    impute_missing_cust_account(banking_df)

def bank_account_size(banking):
    # -----------------------------------------------------------
    # Understand average account size and how it varies
    # -----------------------------------------------------------
    # Find values of acct_cur that are equal to 'euro'
    acct_eu = banking['acct_cur'] == 'euro'

    # Convert acct_amount where it is in euro to dollars
    banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1

    # Unify acct_cur column by changing 'euro' values to 'dollar'
    banking.loc[acct_eu, 'acct_cur'] = 'dollar'

    # Print unique values of acct_cur
    assert banking['acct_cur'].unique() == 'dollar'

    # Print the header of account_opened
    print(banking['account_opened'].head())


def bank_customer_age_group(banking):
    # ------------------------------------------------------------
    # Understand how customer differ in age group
    # --------------------------------------------------------------
    # Store fund columns to sum against
    fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']

    # Find rows where fund_columns row sum == inv_amount
    inv_equ = banking[fund_columns].sum(axis=1) == banking['inv_amount']

    # Store consistent and inconsistent data
    consistent_inv = banking[inv_equ]
    inconsistent_inv = banking[~inv_equ]

    # Store consistent and inconsistent data
    print("Number of inconsistent investments: ", inconsistent_inv.shape[0])


def impute_missing_cust_account(banking):
    # ------------------------------------------------------------
    # Understand how customer differ in age group
    # --------------------------------------------------------------

    # Drop missing values of cust_id
    banking_fullid = banking.dropna(subset=['cust_id'])

    # Compute estimated acct_amount
    acct_imp = banking_fullid['inv_amount'] * 5

    # Impute missing acct_amount with corresponding acct_imp
    banking_imputed = banking_fullid.fillna({'acct_amount': acct_imp})

    # Print number of missing values
    print(banking_imputed.isna().sum())


if __name__ == "__main__":
    main()