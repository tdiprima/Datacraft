## 🧰 Handy Python Libraries for Data Cleaning & Exploration

A curated list of Python tools that make working with Pandas and large datasets way easier — whether you're cleaning messy data, doing quick EDA, or scaling up to big data.

---

### 🧹 PyJanitor — Clean Pandas DataFrames Effortlessly

👉 [github.com/pyjanitor-devs/pyjanitor](https://github.com/pyjanitor-devs/pyjanitor)

PyJanitor extends Pandas with a simple, chainable API for cleaning messy data.

* **Perk:** Rename columns, drop empties, or filter with one-liners.
* **Try:**

  ```python
  df.clean_names().remove_empty()
  ```

---

### 📊 Dabl — Baseline Data Analysis

👉 [github.com/dabl/dabl](https://github.com/dabl/dabl)

Dabl automates exploratory data analysis and quick modeling.

* **Perk:** Generates plots, preps data, and suggests models instantly.
* **Try:**

  ```python
  dabl.plot(df, target_col)
  ```

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

### 🎥 Ipyvizzu — Animated Charts in Jupyter

👉 [ipyvizzu.vizzuhq.com](https://ipyvizzu.vizzuhq.com)

Ipyvizzu brings storytelling flair to your notebooks with animations.

* **Perk:** Animate data over time to make presentations pop.
* **Try:**

  ```python
  chart.animate(Config({"x": "year", "y": "sales"}))
  ```

---

### 🔍 Lux — Auto-Generated Visual Insights

👉 [github.com/lux-org/lux](https://github.com/lux-org/lux)

Lux automatically suggests smart visualizations as you explore dataframes.

* **Perk:** Just display your `df` in a notebook — Lux does the rest.
* **Try:**

  ```python
  df  # Lux magic activates automatically
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
* **Try:**

  ```python
  AV.AutoViz("your_data.csv")
  ```

---

### 🖱️ Bamboolib — GUI for Pandas

👉 [bamboolib.8080labs.com](https://bamboolib.8080labs.com)

Bamboolib gives you a drag-and-drop interface for Pandas inside Jupyter.

* **Perk:** No typing — make edits visually and it writes the code for you.
* **Try:**

  ```python
  import bamboolib as bam
  ```

<br>
