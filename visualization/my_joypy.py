# Sugar, these ridge plots are gonna bring more joy than a summer cookout!
import matplotlib.pyplot as plt
import seaborn as sns
from joypy import joyplot

df = sns.load_dataset("iris")
joyplot(data=df, by="species", column="sepal_width", colormap=plt.cm.cool)
plt.show()
