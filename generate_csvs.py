# generate_csvs.py
import numpy as np
import pandas as pd

# data.csv (for PyJanitor, Fugue): Messy names, empty rows, useless col, x/y for calculations
data = pd.DataFrame(
    {
        "Ugly Column Name": [1, 2, np.nan, 4],
        "age": [25, 35, np.nan, 45],
        "x": [10, 20, 30, 40],
        "y": [5, 15, 25, 35],
        "useless_col": ["junk", "junk", "junk", "junk"],
    }
)
data.to_csv("data.csv", index=False)

# your_data.csv (for Dabl, Ipyvizzu, Lux, Autoviz, Bamboolib): Simple sales data
your_data = pd.DataFrame(
    {
        "year": [2019, 2020, 2021, 2022],
        "sales": [100, 150, 200, 250],
        "category": ["A", "B", "A", "B"],
    }
)
your_data.to_csv("your_data.csv", index=False)

# bigfile.csv (for Vaex): Larger dataset (1000 rows) with x/y
big_data = pd.DataFrame(
    {"x": np.random.randint(0, 100, 1000), "y": np.random.normal(50, 10, 1000)}
)
big_data.to_csv("bigfile.csv", index=False)

# train_data.csv and test_data.csv (for Sweetviz): Simple train/test split simulation
train_data = pd.DataFrame(
    {
        "feature1": np.random.normal(0, 1, 500),
        "feature2": np.random.normal(0, 1, 500),
        "target": np.random.choice([0, 1], 500),
    }
)
test_data = train_data.sample(100)  # Subset for test
train_data.to_csv("train_data.csv", index=False)
test_data.to_csv("test_data.csv", index=False)

print("All CSV files generated: data.csv, your_data.csv, bigfile.csv, train_data.csv, test_data.csv")
