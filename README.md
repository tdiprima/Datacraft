## 🧰 Handy Python Libraries for Data Exploration

A curated list of Python tools that make working with Pandas and large datasets way easier — whether you're doing quick EDA or scaling up to big data.

---

### ⚡ Vaex — Out-of-Core DataFrames for Big Data

👉 [github.com/vaexio/vaex](https://www.github.com/vaexio/vaex)

Vaex handles **billions** of rows fast, all on your laptop.

* **Perk:** Lazy loading means no memory crashes on huge files.
* **Try:**

  ```python
  df = vaex.open("bigfile.csv")
  df[df.x > 0].mean(df.y)
  ```

---

### 🔗 Fugue — Distributed Computation Without Rewrites

👉 [github.com/fugue-project/fugue](http://github.com/fugue-project/fugue)

Fugue lets you mix SQL, Pandas, and Spark seamlessly.

* **Perk:** Run the same code locally or on Spark without changes.
* **Try:**

  ```python
  transform(df, custom_logic)
  ```

---

### 📈 Sweetviz — Instant Data Reports

👉 [github.com/fbdesignpro/sweetviz](https://github.com/fbdesignpro/sweetviz)

Sweetviz creates interactive HTML reports for fast dataset comparisons.

* **Perk:** Visualizes differences between train/test or before/after datasets.
* **Try:**

  ```python
  sweetviz.compare([df_train, "Train"], [df_test, "Test"])
  ```

---

### 📉 Pingouin — Easy Statistical Tests

👉 [pingouin-stats.org](https://pingouin-stats.org/index.html)

Pingouin simplifies t-tests, ANOVAs, and more with clean tables.

* **Perk:** Cleaner and more unified than `scipy`.
* **Try:**

  ```python
  pg.ttest(dv1, dv2, paired=True)
  ```

---

### 🖼️ AutoViz — One-Line Data Visualization

👉 [github.com/AutoViML/AutoViz](https://github.com/AutoViML/AutoViz)

AutoViz automatically plots distributions and outliers from any dataset.

* **Perk:** Instant visual overviews from CSVs or DataFrames.
* **I tried it:** It removed the sales column, thinking that it wasn't important!  Will not use.

---

### 🎨 Datashader — Large-Scale Data Visualization

👉 [datashader.org](https://datashader.org)

Datashader renders massive datasets (millions+ points) into beautiful, interactive visualizations.

* **Perk:** No overplotting or performance issues with huge point clouds.
* **Try:**

  ```python
  import datashader as ds
  cvs = ds.Canvas(plot_width=800, plot_height=600)
  agg = cvs.points(df, 'x', 'y')
  ```

---

### 🎵 JoyPy — Ridgeline Plots Made Easy

👉 [github.com/leotac/joypy](https://github.com/leotac/joypy)

JoyPy creates beautiful ridgeline plots (stacked density curves) for comparing distributions.

* **Perk:** Perfect for showing distributions across groups or time periods.
* **Try:**

  ```python
  import joypy
  joypy.joyplot(df, by='category', column='value')
  ```

---

### ⭕ Pycirclize — Circular Genome-Style Plots

👉 [github.com/moshi4/pycirclize](https://github.com/moshi4/pycirclize)

Pycirclize creates circular plots inspired by genomics visualizations.

* **Perk:** Unique circular layouts for hierarchical or cyclical data.
* **Try:**

  ```python
  from pycirclize import Circos
  circos = Circos(sectors={"A": 10, "B": 15, "C": 12})
  ```

---

### 🧇 PyWaffle — Waffle Charts in Python

👉 [github.com/gyli/PyWaffle](https://github.com/gyli/PyWaffle)

PyWaffle creates waffle charts (square pie charts) for intuitive proportion visualization.

* **Perk:** More readable than pie charts for showing parts of a whole.
* **Try:**

  ```python
  import matplotlib.pyplot as plt
  from pywaffle import Waffle
  plt.figure(FigureClass=Waffle, rows=5, values=[30, 16, 4])
  ```

&mdash; *README written by: claude-sonnet-4-20250514, gpt-5, and me*

<br>
