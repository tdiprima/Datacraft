# TODO: Notebook
from autoviz.AutoViz_Class import AutoViz_Class

AV = AutoViz_Class()
# %matplotlib inline
# dft = AV.AutoViz("../../data/your_data.csv")

dfte = AV.AutoViz(
    "../../data/your_data.csv",
    sep=",",
    depVar="",
    dfte=None,
    header=0,
    verbose=1,
    lowess=False,
    chart_format="svg",
    max_rows_analyzed=150000,
    max_cols_analyzed=30,
    save_plot_dir=None,
)
