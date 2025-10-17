# This script demonstrates three ways to implement pyjanitor for data cleaning:
# 1. Native pandas extension, 2. Functional API, 3. Pipe method.
# It uses clean_names (to snake_case column names) and remove_empty (to remove empty rows/columns).

import numpy as np
import pandas as pd
from janitor import clean_names, remove_empty  # For functional API

# Shared dataframe for all examples - quarterly sales data
dataframe = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Region North": [15000.0, 18500.0, 22000.0, 19500.0],
    "Region South": [12500.0, np.nan, 14800.0, 16200.0],
    "Region East": [20000.0, 21500.0, 23000.0, 24500.0],
}

# 1. Native pandas extension
df_native = pd.DataFrame.from_dict(dataframe).clean_names().remove_empty()
print("Native:\n", df_native.head())

# 2. Functional API
df_functional = pd.DataFrame.from_dict(dataframe)
df_functional = clean_names(df_functional)
df_functional = remove_empty(df_functional)
print("Functional:\n", df_functional.head())

# 3. Pipe method
df_pipe = pd.DataFrame.from_dict(dataframe).pipe(clean_names).pipe(remove_empty)
print("Pipe:\n", df_pipe.head())
