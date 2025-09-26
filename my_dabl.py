# https://pypi.org/project/dabl/
import dabl
import pandas as pd

dataframe = dabl.datasets.load_iris()
# dataframe = pd.read_csv("data/your_data.csv")
target_col = 'target'

dabl.plot(dataframe, target_col)
