# https://pyjanitor-devs.github.io/pyjanitor/
import pandas as pd

# Read 'data.csv' (has messy column names, empty rows, and a useless column)
df = pd.read_csv("../../data/data.csv")
df = df.clean_names().remove_empty().remove_columns(["useless_col"])

print(df.head())
