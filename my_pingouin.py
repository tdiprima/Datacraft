import numpy as np
import pingouin as pg

dv1 = np.random.normal(0, 1, 100)
dv2 = np.random.normal(0.5, 1, 100)
result = pg.ttest(dv1, dv2, paired=True)
print(result)
