# Lord have mercy! This plotnine's finer than Sunday dinner at mama's house!
# plotnine 0.13.6 requires pandas<3.0.0,>=2.1.0
import pandas as pd
from plotnine import aes, geom_point, ggplot, theme_minimal

df = pd.DataFrame(
    {"x": [1, 2, 3, 4, 5], "y": [5, 3, 6, 2, 7], "category": ["A", "A", "B", "B", "C"]}
)

(ggplot(df, aes("x", "y", color="category")) + geom_point(size=5) + theme_minimal()).show()
