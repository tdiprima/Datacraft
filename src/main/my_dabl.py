# https://pypi.org/project/dabl/
import dabl
import pandas as pd

# Sample usage with generated 'your_data.csv'
dataframe = pd.read_csv("../../data/your_data.csv")
dabl.plot(dataframe, target_col="sales")
