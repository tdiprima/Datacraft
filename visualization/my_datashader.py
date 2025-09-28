# Mercy me! We're about to shade data faster than kudzu spreads in Georgia!
import datashader as ds
import datashader.transfer_functions as tf
import numpy as np
import pandas as pd

n = 1_000_000
df = pd.DataFrame({"x": np.random.randn(n), "y": np.random.randn(n)})

canvas = ds.Canvas(plot_width=600, plot_height=600)
agg = canvas.points(df, "x", "y")
img = tf.shade(agg, cmap=["lightblue", "darkblue"])
img.to_pil().show()
