import pandas as pd
from fugue import transform

df = pd.read_csv("data/data.csv")


def custom_logic(df: pd.DataFrame) -> pd.DataFrame:
    df["z"] = (
        df["x"] + df["y"]
    )  # Assumed 'x' and 'y' columns from sample data
    return df


# Transform with schema
transformed_df = transform(df, custom_logic, schema="*,z:int")
print(transformed_df.head())
