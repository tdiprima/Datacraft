import pandas as pd
import sweetviz

# Sample usage with generated train/test CSVs
df_train = pd.read_csv("data/train_data.csv")
df_test = pd.read_csv("data/test_data.csv")
report = sweetviz.compare([df_train, "Train"], [df_test, "Test"])
report.show_html("report.html")  # This generates an HTML file
