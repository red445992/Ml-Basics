
# 📉 Plotting with Missing Data in Pandas

Pandas tries to be pragmatic about plotting `DataFrame`s or `Series` that contain missing data.  
Missing values are **dropped**, **left out**, or **filled**, depending on the plot type.

## 📊 NaN Handling by Plot Type

| **Plot Type**     | **NaN Handling**                       |
|-------------------|----------------------------------------|
| Line              | Leave gaps at NaNs                     |
| Line (stacked)    | Fill 0’s                               |
| Bar               | Fill 0’s                               |
| Scatter           | Drop NaNs                              |
| Histogram         | Drop NaNs (column-wise)                |
| Box               | Drop NaNs (column-wise)                |
| Area              | Fill 0’s                               |
| KDE               | Drop NaNs (column-wise)                |
| Hexbin            | Drop NaNs                              |
| Pie               | Fill 0’s                               |

> ℹ️ If any of these defaults are not what you want, or if you want to be **explicit** about how missing values are handled, consider using `fillna()` or `dropna()` before plotting.
"""


# 📊 Chart Visualization with Pandas

This guide summarizes the key visualization functions and tools covered from the [Pandas Visualization Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#), including essential chart types and advanced plotting tools.

---

## 📈 Basic Plotting Functions

- **`.plot()`**  
  The foundation for all plots in pandas. Automatically selects the best plot type based on data.

- **`.bar()` / `.barh()`**  
  Vertical and horizontal bar charts. Ideal for comparing discrete categories.

- **`.hist()`**  
  Histogram for frequency distribution of numerical data.

- **`.box()`**  
  Box-and-whisker plot for visualizing the distribution, median, and outliers.

- **`.area()`**  
  Area chart, useful for visualizing part-to-whole relationships over time.

- **`.scatter()`**  
  Scatter plot for visualizing relationships between two continuous variables.

- **`.hexbin()`**  
  Hexagon bin plot for visualizing density of points in scatter plots (ideal for large datasets).

- **`.pie()`**  
  Pie chart for visualizing proportions of a whole. Best used with a small number of categories.

---

## 🧰 Advanced Visualization Tools

- **`pd.plotting.scatter_matrix()`**  
  Matrix of scatter plots to visualize pairwise relationships between numerical features.

- **`pd.plotting.andrews_curves()`**  
  Uses Fourier transforms to visualize structure in high-dimensional data.

- **`pd.plotting.parallel_coordinates()`**  
  Visualizes individual data points across multiple features using parallel axes.

- **`pd.plotting.lag_plot()`**  
  Helps identify autocorrelation in time series data.

- **`pd.plotting.autocorrelation_plot()`**  
  Plots autocorrelation of a time series across lags.

- **`pd.plotting.bootstrap_plot()`**  
  Visualizes the distribution of the sample mean through resampling (bootstrapping).

- **`pd.plotting.radviz()`**  
  Projects multidimensional data onto 2D space in a circular layout for pattern discovery.

---

## 🛠️ Plotting Tools & Formatting

- **Matplotlib Integration**:  
  Pandas uses Matplotlib under the hood. You can access the Matplotlib axes object via `ax=` parameter for customization.

- **Backends**:  
  Pandas supports multiple plotting backends (e.g., Matplotlib, Plotly). You can set the backend using:
  ```python
  pd.options.plotting.backend = "matplotlib"  # or "plotly"