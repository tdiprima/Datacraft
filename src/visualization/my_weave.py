# Bless your heart, we're fixin' to weave some data magic like grandmama's quilts!
# Failed building wheel for cudf
import cudf
import weave

df = cudf.DataFrame({"x": [1, 2, 3, 4], "y": [10, 20, 30, 40]})
weave.show(df)  # opens interactive browser
