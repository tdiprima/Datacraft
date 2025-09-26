### Tools for cleaning pandas DataFrames
https://github.com/pyjanitor-devs/pyjanitor

**PyJanitor** 🧹 Cleans messy dataframes easily, like a friendly Pandas upgrade.
  
* Key perk: Chain simple methods to rename, drop empties, or filter.  
* Tip: `df.clean_names().remove_empty()` – no more endless code!

### Data Analysis Baseline Library
https://github.com/dabl/dabl

**Dabl** 📊 Auto-analyzes data for lazy exploration.

* Key perk: Plots visuals, preps data, and suggests models instantly.  
* Tip: `dabl.plot(df, target_col)` – quick EDA without thinking hard. 

### Out-of-Core DataFrames to visualize and explore big tabular datasets
https://www.github.com/vaexio/vaex

**Vaex** ⚡ Handles huge datasets (billions of rows) super fast on your laptop.

* Key perk: Lazy loading, no memory crashes for big files.  
* Tip: `df = vaex.open('bigfile.csv'); df[df.x > 0].mean(df.y)` – explore 10GB data easily. 

### An abstraction layer for distributed computation
http://github.com/fugue-project/fugue

**Fugue** 🔗 Mixes SQL, Pandas, and Spark without rewriting code.

* Key perk: Applies custom functions across local or big-data setups.  
* Tip: Use `transform(df, custom_logic)` – seamless for any scale.  

### A pandas-based library to visualize and compare datasets.
https://github.com/fbdesignpro/sweetviz

**Sweetviz** 📈 Creates instant, interactive HTML reports on your data.
  
* Key perk: Compares datasets, spots patterns with zero effort.  
* Tip: `sweetviz.compare([df_train, "Train"], [df_test, "Test"])` – open in browser for insights.

### Build animated charts in Jupyter Notebook and similar environments with a simple Python syntax.
https://ipyvizzu.vizzuhq.com

**Ipyvizzu** 🎥 Makes animated charts in Jupyter for storytelling.

* Key perk: Animates data changes over time, great for presentations.  
* Tip: `chart.animate(Config({"x": "year", "y": "sales"}))` – impress non-tech folks!

### A Python API for Intelligent Data Discovery
https://github.com/lux-org/lux

**Lux** 🔍 Auto-suggests smart charts right in your Pandas dataframe.

* Key perk: Generates insights and visuals with no extra code.  
* Tip: Just load `df` in a notebook – it toggles on magic views.

### Pingouin: statistical package for Python
https://pingouin-stats.org/index.html

**Pingouin** 📉 Simple stats tests like t-tests or ANOVA, in clean tables.

* Key perk: Unified, easy API – less clunky than scipy.  
* Tip: `pg.ttest(dv1, dv2, paired=True)` – get readable results fast.

### Automatically Visualize any dataset, any size with a single line of code
https://github.com/AutoViML/AutoViz

**Autoviz** 🖼️ Auto-plots your data to explore distributions and outliers.

* Key perk: Fire-and-forget for quick overviews from CSV or dataframe.  
* Tip: `AV.AutoViz("your_data.csv")` – instant visuals, no setup.

### bamboolib - a GUI for pandas
https://bamboolib.8080labs.com

**Bamboolib** 🖱️ GUI for Pandas in Jupyter – drag/drop like Excel, but generates code.

* Key perk: No typing for data tweaks; great for teams or quick edits.  
* Tip: `import bamboolib as bam` – click to build, code appears automatically.

<br>
