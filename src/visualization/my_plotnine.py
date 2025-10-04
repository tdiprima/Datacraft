# Lord have mercy! This plotnine's finer than Sunday dinner at mama's house!
# TODO: Notebook
import pandas as pd
from plotnine import aes, geom_point, ggplot, theme_minimal

df = pd.DataFrame(
    {"x": [1, 2, 3, 4, 5], "y": [5, 3, 6, 2, 7], "category": ["A", "A", "B", "B", "C"]}
)

ggplot(df, aes("x", "y", color="category")) + geom_point(size=5) + theme_minimal()
