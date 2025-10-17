# This script provides a template for contributing a custom data cleaning function to pyjanitor.
# It uses pandas_flavor to register the function as a pandas DataFrame method.
# The example function standardizes currency columns and handles outliers.

import pandas as pd
import pandas_flavor as pf
import numpy as np


@pf.register_dataframe_method
def standardize_currency_columns(
    dataframe: pd.DataFrame, currency_cols=None, remove_outliers=True
) -> pd.DataFrame:
    """
    Custom cleaning function that:
    1. Removes currency symbols and converts to float
    2. Optionally removes outliers using IQR method
    3. Rounds values to 2 decimal places
    """
    df = dataframe.copy()
    
    if currency_cols is None:
        currency_cols = df.select_dtypes(include=['object']).columns
    
    for col in currency_cols:
        if col in df.columns:
            # Remove currency symbols and convert to float
            df[col] = df[col].str.replace('$', '').str.replace(',', '').astype(float)
            
            # Remove outliers using IQR method if specified
            if remove_outliers:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                df[col] = df[col].where((df[col] >= lower_bound) & (df[col] <= upper_bound), np.nan)
            
            # Round to 2 decimal places
            df[col] = df[col].round(2)
    
    return df


# Example usage with product pricing data
df = pd.DataFrame({
    "product": ["Widget A", "Widget B", "Widget C", "Widget D", "Widget E"],
    "price": ["$45.99", "$52.50", "$48.75", "$250.00", "$51.20"],  # Note: $250 is an outlier
    "cost": ["$25.50", "$30.00", "$28.90", "$29.50", "$31.00"]
})

print("Original DataFrame:")
print(df)

df_modified = df.standardize_currency_columns(currency_cols=["price", "cost"])
print("\nCleaned DataFrame:")
print(df_modified)
