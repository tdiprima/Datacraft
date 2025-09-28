# Well butter my biscuit! These waffle charts are prettier than a peach!
import matplotlib.pyplot as plt
from pywaffle import Waffle

data = {"Python": 50, "Rust": 30, "Go": 20}

fig = plt.figure(
    FigureClass=Waffle,
    rows=5,
    values=data,
    colors=("#377eb8", "#4daf4a", "#ff7f00"),
    title={"label": "Language Popularity", "loc": "left"},
)
plt.show()
