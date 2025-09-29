## **Topic: Charts & Graphs in Data Visualization**

---

### **1. Introduction to Charts & Graphs**

#### **TL;DR**

Charts and graphs transform raw data into **visual representations**, making patterns, trends, and relationships easier to understand.
Each chart type is designed for specific **data types**, **analysis goals**, and **audience needs**.

---

#### **Why They Matter**

* **Simplifies complexity** – humans process visuals **60,000× faster** than text.
* **Identifies patterns & trends** that are hard to see in tables.
* **Improves decision-making** by presenting actionable insights.
* **Communicates findings clearly** to stakeholders.

---

#### **Core Chart Selection Principle**

| Goal / Task                          | Best Chart Types                    |
| ------------------------------------ | ----------------------------------- |
| Compare categories                   | Bar chart, Pie chart, Treemap       |
| Show trend over time                 | Line chart, Area chart              |
| Show distribution                    | Histogram, Boxplot, Violin plot     |
| Show relationships between variables | Scatter plot, Bubble chart, Heatmap |
| Show proportions & hierarchy         | Pie chart, Donut chart, Treemap     |

---

Now, let's go **chart-by-chart**.

---

## **2. Bar Chart**

### **Definition**

A **bar chart** uses rectangular bars to represent **quantitative data** across **categorical variables**.

---

### **Usage**

* Comparing quantities across **categories**.
  Example: Sales per region, population per country.

---

### **How It Works**

* **X-axis (horizontal)** → categories (e.g., products, months)
* **Y-axis (vertical)** → numerical values
* Height/length of the bar = magnitude of the data point.

---

### **Advantages**

1. Easy to read and interpret.
2. Works well for both small and large datasets.
3. Can show positive and negative values.
4. Supports **grouped** and **stacked** comparisons.

---

### **Disadvantages**

1. Becomes cluttered with too many categories.
2. Not ideal for **time-series trends**.
3. Doesn't show distribution within categories.

---

### **Example**

```python
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

plt.bar(categories, values)
plt.title("Simple Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
```

---

## **3. Line Chart**

### **Definition**

A **line chart** displays **data points connected by lines**, emphasizing **trends over time**.

---

### **Usage**

* Time-series analysis (e.g., stock prices, weather trends).
* Showing continuous data changes.

---

### **Advantages**

1. Perfect for trend analysis.
2. Easy to compare multiple data series.
3. Highlights fluctuations clearly.

---

### **Disadvantages**

1. Difficult to interpret with too many lines.
2. Not suitable for categorical data without order.

---

### **Example**

```python
import numpy as np

time = np.arange(1, 6)
sales = [10, 15, 12, 18, 22]

plt.plot(time, sales, marker='o')
plt.title("Line Chart - Sales Over Time")
plt.xlabel("Time")
plt.ylabel("Sales")
plt.show()
```

---

## **4. Pie Chart**

### **Definition**

A **pie chart** shows parts of a whole using slices of a circle.

---

### **Usage**

* Showing **proportions** or **percentage share**.

---

### **Advantages**

1. Visually intuitive for simple datasets.
2. Quickly shows relative contribution.

---

### **Disadvantages**

1. Hard to compare slices of similar size.
2. Poor for large category counts.
3. Doesn't show changes over time.

---

### **Example**

```python
sizes = [30, 20, 45, 5]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart Example")
plt.show()
```

---

## **5. Scatter Plot**

### **Definition**

A **scatter plot** shows the relationship between **two quantitative variables** using dots.

---

### **Usage**

* Identifying **correlations** (positive, negative, or none).
* Detecting **outliers** in data.

---

### **Advantages**

1. Excellent for showing relationships.
2. Good for outlier detection.
3. Can add a trend line.

---

### **Disadvantages**

1. Hard to interpret with too many data points.
2. Doesn't show exact distributions.

---

### **Example**

```python
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,100,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.xlabel("X Value")
plt.ylabel("Y Value")
plt.show()
```

---

## **6. Area Chart**

### **Definition**

An **area chart** is like a line chart but with the area beneath the line **filled** with color.

---

### **Usage**

* Showing **cumulative trends**.
* Comparing multiple time-series visually.

---

### **Advantages**

1. Adds emphasis on magnitude.
2. Good for showing part-to-whole over time.

---

### **Disadvantages**

1. Can overlap and become messy.
2. Difficult to interpret precisely.

---

### **Example**

```python
plt.fill_between(time, sales, color="skyblue", alpha=0.4)
plt.plot(time, sales, color="Slateblue", alpha=0.7)
plt.title("Area Chart Example")
plt.show()
```

---

## **7. Radar Chart**

### **Definition**

A **radar chart** (or spider chart) displays multivariate data on a circular grid.

---

### **Usage**

* Comparing multiple variables for a single entity.
* Example: Comparing attributes of smartphones or players.

---

### **Advantages**

1. Good for performance comparisons.
2. Displays multi-dimensional data compactly.

---

### **Disadvantages**

1. Hard to read with many variables.
2. Not suitable for precise numerical analysis.

---

## **8. Histogram**

### **Definition**

A **histogram** shows the **frequency distribution** of a dataset.

---

### **Usage**

* Understanding **data distribution**.
* Detecting skewness or outliers.

---

### **Advantages**

1. Highlights data shape.
2. Useful for statistical analysis.

---

### **Disadvantages**

1. Bin size affects interpretation.
2. Not ideal for exact value comparison.

---

### **Example**

```python
data = [1,1,2,2,2,3,3,4,4,4,4,5,5,5,5,5]
plt.hist(data, bins=5, edgecolor='black')
plt.title("Histogram Example")
plt.show()
```

---

## **9. Treemap**

### **Definition**

A **treemap** shows hierarchical data using **nested rectangles**.

---

### **Usage**

* Visualizing **part-to-whole relationships**.
* Example: Company revenue by department.

---

### **Advantages**

1. Compact for large hierarchical data.
2. Easy to compare proportions.

---

### **Disadvantages**

1. Hard to read labels in small rectangles.
2. Not good for trend analysis.

---

## **10. Pairplot (Seaborn Specific)**

### **Definition**

A **pairplot** shows pairwise relationships in a dataset.

---

### **Usage**

* Exploring relationships between multiple variables.

---

### **Advantages**

1. One command gives a comprehensive view.
2. Combines scatter plots and histograms.

---

### **Disadvantages**

1. Performance issue with large datasets.

---

### **Example**

```python
import seaborn as sns
import pandas as pd

df = sns.load_dataset('iris')
sns.pairplot(df, hue='species')
plt.show()
```

---

## **11. Boxplot**

### **Definition**

A **boxplot** shows data distribution using **five-number summary** (min, Q1, median, Q3, max).

---

### **Usage**

* Detecting **outliers** and **spread of data**.

---

### **Advantages**

1. Highlights outliers clearly.
2. Great for comparing distributions.

---

### **Disadvantages**

1. Does not show exact counts.
2. Can be confusing for beginners.

---

## **12. Bubble Chart**

### **Definition**

A **bubble chart** extends a scatter plot by adding a **third variable** as bubble size.

---

### **Usage**

* Showing three-dimensional relationships.

---

### **Advantages**

1. Displays additional data dimension.
2. Useful for correlation + magnitude.

---

### **Disadvantages**

1. Hard to compare bubble sizes precisely.
2. Can become cluttered.

---

## **13. Heatmap**

### **Definition**

A **heatmap** uses colors to represent data values in a matrix.

---

### **Usage**

* Correlation matrices.
* Highlighting intensity or frequency.

---

### **Advantages**

1. Visually appealing.
2. Excellent for spotting patterns.

---

### **Disadvantages**

1. Color choice can mislead.
2. Hard to read with too many variables.

---

### **Example**

```python
import numpy as np

data = np.random.rand(6,6)
sns.heatmap(data, annot=True)
plt.title("Heatmap Example")
plt.show()
```

---

## **Comparison Table**

| Chart Type   | Data Type    | Best For                | Strength      | Weakness               |
| ------------ | ------------ | ----------------------- | ------------- | ---------------------- |
| Bar Chart    | Cat vs Num   | Comparing categories    | Simple, clear | Clutter with many bars |
| Line Chart   | Time vs Num  | Trends over time        | Shows trends  | Too many lines confuse |
| Pie Chart    | Cat vs Whole | Proportions             | Easy to grasp | Not precise            |
| Scatter Plot | Num vs Num   | Relationships, outliers | Correlation   | Overlapping points     |
| Histogram    | Numerical    | Data distribution       | Shape clarity | Bin size sensitive     |
| Heatmap      | Matrix       | Intensity patterns      | Visual appeal | Overload risk          |

---

Let's **categorize each chart type** based on whether it's **better for small datasets, large datasets, or both**, and **why**.

This will help you choose the **right visualization** based on dataset **size** and **complexity**.

---

# **Chart Selection Based on Dataset Size**

---

## **1. Core Concept**

| **Dataset Size**   | **Typical Characteristics**                        | **What to Look for in a Chart**                            |
| ------------------ | -------------------------------------------------- | ---------------------------------------------------------- |
| **Small Dataset**  | < 100 data points, few categories                  | Clear, simple charts to highlight details                  |
| **Medium Dataset** | 100–10,000 data points, moderate categories        | Charts that balance clarity and complexity                 |
| **Large Dataset**  | > 10,000 data points, many categories or variables | Aggregated visualizations that prevent clutter and overlap |

---

## **2. Chart Classification**

We'll categorize into:

* 🟢 **Best for Small Datasets**
* 🟡 **Works for Both Small & Large (Scalable)**
* 🔴 **Best for Large Datasets**

---

### **A. Charts Best for Small Datasets (Clear & Simple)**

These charts **shine with fewer categories or data points** because they:

* Show exact values clearly.
* Focus on direct comparisons.
* Avoid visual clutter.

| **Chart Type**           | **Why Small Dataset is Ideal**                                    | **Max Recommended Data Points** | Example Use Case                         |
| ------------------------ | ----------------------------------------------------------------- | ------------------------------- | ---------------------------------------- |
| **Pie Chart**            | Easy to see proportions but breaks with many categories.          | 5–8 slices                      | Budget breakdown for 5 departments       |
| **Bar Chart**            | Excellent for category comparison, gets messy with too many bars. | ~20 categories                  | Sales by 10 products                     |
| **Radar Chart (Spider)** | Good for comparing few entities across attributes.                | 3–8 attributes                  | Comparing 5 players’ stats               |
| **Bubble Chart**         | Works only when a few points need emphasis.                       | 20–30 bubbles                   | Visualizing market share of 10 companies |
| **Boxplot**              | Small group comparisons are clearer.                              | 10–15 groups                    | Salary distribution across 5 departments |

**Takeaway:**
For small datasets, **precise detail > general trends**.
Avoid using too many categories or overlapping visuals.

---

### **B. Charts That Scale Well (Both Small & Large Datasets)**

These charts can handle **both small and large datasets** because they:

* Summarize data effectively.
* Support **aggregation or zooming**.
* Provide **multiple levels of insight**.

| **Chart Type**         | **Why Scalable**                                                       | **When to Use Small Data**            | **When to Use Large Data**                                 |
| ---------------------- | ---------------------------------------------------------------------- | ------------------------------------- | ---------------------------------------------------------- |
| **Line Chart**         | Handles continuous data well, supports zooming.                        | Tracking 12 months of sales.          | Showing stock prices over years (thousands of points).     |
| **Histogram**          | Uses bins to aggregate data, scalable by bin size.                     | Showing 50 test scores.               | Showing distribution of millions of customer transactions. |
| **Heatmap**            | Summarizes complex matrices with colors.                               | Comparing 5×5 variable relationships. | Showing 100×100 correlation matrix.                        |
| **Area Chart**         | Similar to line chart, works for both with aggregation.                | Small product sales trends.           | Website traffic trends with thousands of daily visits.     |
| **Treemap**            | Hierarchically scalable by grouping levels.                            | Company revenue by 5 departments.     | Revenue by 500 products in nested categories.              |
| **Pairplot (Seaborn)** | Automatically scales with variables but gets heavy for large datasets. | Iris dataset (150 rows).              | Sampled data of 1,000 rows only.                           |

---

### **C. Charts Best for Large Datasets (Summarizing & Aggregating)**

These charts **aggregate and simplify** huge amounts of data to prevent clutter.

| **Chart Type**               | **Why Large Dataset is Ideal**                              | **Min Recommended Data Points** | Example Use Case                         |
| ---------------------------- | ----------------------------------------------------------- | ------------------------------- | ---------------------------------------- |
| **Histogram**                | Bins condense thousands of data points into clear patterns. | 500+                            | Customer age distribution (50,000 users) |
| **Heatmap**                  | Colors encode thousands of values efficiently.              | 500+                            | Correlation between 50 stock returns     |
| **Treemap**                  | Nested rectangles handle hundreds of categories.            | 100+                            | Revenue breakdown for 2000 SKUs          |
| **Density Plot** *(Seaborn)* | Smoothly visualizes massive data distributions.             | 500+                            | Sensor readings from IoT devices         |

---

## **3. Full Categorization Table**

| **Chart Type**         | **Best For**               | **Small Dataset?** | **Large Dataset?**                |
| ---------------------- | -------------------------- | ------------------ | --------------------------------- |
| **Pie Chart**          | Simple proportions         | 🟢 Excellent       | 🔴 Poor                           |
| **Bar Chart**          | Comparing categories       | 🟢 Excellent       | 🟡 Moderate (use grouped/stacked) |
| **Line Chart**         | Trends over time           | 🟢 Good            | 🟡 Good (aggregate or smooth)     |
| **Area Chart**         | Trends + magnitude         | 🟢 Good            | 🟡 Good (aggregate)               |
| **Radar Chart**        | Multi-attribute comparison | 🟢 Excellent       | 🔴 Poor                           |
| **Scatter Plot**       | Correlations, outliers     | 🟢 Good            | 🔴 Poor unless sampled            |
| **Bubble Chart**       | 3D relationships           | 🟢 Good            | 🔴 Poor                           |
| **Histogram**          | Distribution summary       | 🟡 Moderate        | 🟢 Excellent                      |
| **Boxplot**            | Spread and outliers        | 🟢 Good            | 🟡 Good                           |
| **Treemap**            | Hierarchical breakdown     | 🟢 Good            | 🟢 Excellent                      |
| **Pairplot**           | Pairwise relationships     | 🟢 Good            | 🔴 Poor unless subsetted          |
| **Heatmap**            | Intensity patterns         | 🟡 Moderate        | 🟢 Excellent                      |
| **Density Plot (KDE)** | Smooth distributions       | 🟡 Moderate        | 🟢 Excellent                      |

---

## **4. Decision Tree for Choosing a Chart by Data Size**

```
START
│
├── Is dataset SMALL (<100 data points)?
│   ├── Comparing categories → Bar Chart / Pie Chart
│   ├── Showing proportions → Pie Chart
│   ├── Relationship between 2 variables → Scatter Plot / Bubble Chart
│   └── Multi-attribute comparison → Radar Chart
│
├── Is dataset MEDIUM (100–10,000 data points)?
│   ├── Trend over time → Line Chart / Area Chart
│   ├── Distribution → Histogram / Boxplot
│   └── Matrix data → Heatmap / Treemap
│
└── Is dataset LARGE (>10,000 data points)?
    ├── Summarizing distributions → Histogram / Density Plot
    ├── Relationships → Heatmap
    ├── Categories → Treemap
    └── Time-series → Aggregated Line Chart
```

---

## **5. Quick Recommendations**

| **Scenario**                      | **Best Chart Types**             |
| --------------------------------- | -------------------------------- |
| Small survey (50 responses)       | Pie, Bar, Radar                  |
| Quarterly sales by product        | Bar, Line, Area                  |
| Huge transaction log (1M rows)    | Histogram, Heatmap, Density Plot |
| Comparing 500 products by revenue | Treemap                          |
| Website traffic over 2 years      | Line (aggregated) or Area Chart  |

---

## **Summary**

* **Small datasets** → Focus on clarity, exact values.
  *Best:* Pie, Bar, Radar, Bubble, Scatter, Boxplot.
* **Large datasets** → Focus on aggregation and patterns.
  *Best:* Histogram, Heatmap, Treemap, Density Plot.
* **Scalable charts** → Line, Area, Boxplot work across both depending on aggregation.

---

**comprehensive set of scenario-based questions**

We'll cover **all the charts** you studied:
Bar, Line, Pie, Scatter, Area, Radar, Histogram, Treemap, Pairplot, Boxplot, Bubble, Heatmap, and others like Density plots.

Each question will include:

* **Scenario** *(realistic problem statement)*
* **What you need to do** *(analysis goal)*
* **Think Hint** *(to help you reason)*

At the end, I'll give **answers with explanations**, but let's keep them hidden first so you can self-test.

---

# **Scenario-Based Chart Selection Questions**

---

## **1. Sales Trends Over Time**

Your company has **monthly sales data for the past 5 years** across **four product categories**.
You need to show **overall growth trends** and also **compare category performance**.

* **Goal:** Show trend over time with comparisons.
* **Hint:** Which chart type works best for continuous, time-based data?

---

## **2. Customer Age Distribution**

You have **10,000 customer records** with their ages.
The marketing team wants to understand **age group patterns** to design better promotions.

* **Goal:** Display **frequency distribution** to see which age group dominates.
* **Hint:** Bins and grouping are important here.

---

## **3. Department Budget Allocation**

A company wants to present how its **annual budget (100%)** is distributed across **5 departments** to senior management.

* **Goal:** Show **part-to-whole relationship** clearly.
* **Hint:** It must be simple and visually appealing.

---

## **4. Comparing Employee Performance**

You are comparing **5 employees** based on **6 performance metrics** like communication, technical skills, teamwork, etc.

* **Goal:** Compare multiple attributes at once for each employee.
* **Hint:** You need a compact, circular view.

---

## **5. Outlier Detection in Salaries**

Your HR team wants to **detect unusual salary values** among different job roles.

* **Goal:** Identify **spread of data and outliers**.
* **Hint:** A chart that shows median, quartiles, and extremes.

---

## **6. Product Sales by Region**

You need to visualize **sales data** across **20 regions** and **4 product categories**.
The management wants to see which region contributes most and how categories differ within them.

* **Goal:** Compare categories and groups together.
* **Hint:** Consider both grouping and stacking techniques.

---

## **7. Detecting Correlations Between Variables**

You have a dataset with **height, weight, exercise hours, and calorie intake** for 500 people.
You want to **explore relationships** between all variables at once.

* **Goal:** Show pairwise relationships and detect correlations.
* **Hint:** Seaborn has a special plot for this.

---

## **8. Website Traffic by Day**

The marketing team wants to **visualize website visits** for each day of the past 6 months to find **seasonal patterns** and **growth trends**.

* **Goal:** Show **continuous time-series data**.
* **Hint:** Smooth, continuous visualization needed.

---

## **9. Detecting Market Share Changes**

You have data for **market share percentages** of 10 smartphone companies across **3 consecutive years**.
The management wants to see how market share has changed over time.

* **Goal:** Compare part-to-whole relationships over multiple time points.
* **Hint:** Regular pie chart won’t be enough for three years.

---

## **10. Call Center Analysis**

You have **500,000 call records** with variables like **call duration, wait time, and customer rating**.
The task is to **find patterns and group behavior** without overwhelming the viewer.

* **Goal:** Summarize large, complex data visually.
* **Hint:** Which chart can show intensity using colors?

---

## **11. Comparing Product Revenues**

You need to show **hierarchical revenue data**, where each **main product category** has **subcategories** and each subcategory has **products**.

* **Goal:** Show hierarchy and proportions.
* **Hint:** Nested structure visualization needed.

---

## **12. Comparing Three Variables**

You want to visualize:

* **Revenue (X-axis)**

* **Profit (Y-axis)**

* **Market size (bubble size)**
  for 25 companies.

* **Goal:** Show relationship among **three quantitative variables**.

* **Hint:** Scatter plot isn't enough here.

---

## **13. Daily Sales with Emphasis on Total Volume**

You want to show **daily sales numbers** for one year, highlighting **both the daily trend and the cumulative magnitude**.

* **Goal:** Focus on both **individual data points and overall volume**.
* **Hint:** Think of a filled version of a line chart.

---

## **14. Large Sensor Dataset Distribution**

You have **1 million temperature readings** from IoT devices.
You need to see **how the readings are distributed** without plotting every single point.

* **Goal:** Summarize large data distribution clearly.
* **Hint:** Which chart uses bins to group values?

---

## **15. Customer Segmentation Clusters**

You are analyzing customer behavior using **income** and **spending score** to **find clusters** of similar customers.

* **Goal:** Show clusters and relationships visually.
* **Hint:** Which chart shows two-variable relationships clearly?

---

## **16. Finding Correlation Between 15 Variables**

You have a financial dataset with 15 variables.
You need to **see which variables are strongly correlated**.

* **Goal:** Quickly identify positive and negative correlations.
* **Hint:** Use colors to encode strength of relationships.

---

## **17. Comparing Many Categories**

Your dataset contains **sales data for 500 products** in 30 different categories.
You need to visualize which **categories are the biggest contributors**.

* **Goal:** Show many part-to-whole relationships at once.
* **Hint:** Normal bar chart will become unreadable.

---

## **18. Tracking Multiple Stocks**

You have daily closing prices for **5 different stocks over the past year**.
The goal is to **compare their performance trends**.

* **Goal:** Show multiple trends clearly on one graph.
* **Hint:** Avoid clutter but allow comparisons.

---

## **19. Employee Skill Improvement Over 6 Months**

You want to show how each employee improved in **3 skill areas** over a 6-month training program.

* **Goal:** Compare performance changes for individuals and overall.
* **Hint:** Circular format may work, or small multiples.

---

## **20. Detecting Distribution Shape**

You have exam scores for 1,000 students.
The education team wants to know whether the distribution is **normal, skewed, or bimodal**.

* **Goal:** Focus on **shape of data distribution**.
* **Hint:** Histogram is good, but what about a smoother option?

---

# **Answer Key with Explanations**

<details>
<summary>Click to reveal answers</summary>

| **Scenario**                          | **Best Chart(s)**              | **Reason**                                       |
| ------------------------------------- | ------------------------------ | ------------------------------------------------ |
| 1. Sales Trends Over Time             | Line Chart / Area Chart        | Time-series, clear trends over time              |
| 2. Customer Age Distribution          | Histogram                      | Shows distribution using bins                    |
| 3. Department Budget Allocation       | Pie Chart / Donut Chart        | Small, simple proportions                        |
| 4. Comparing Employee Performance     | Radar Chart                    | Multi-attribute, compact view                    |
| 5. Outlier Detection in Salaries      | Boxplot                        | Shows spread and outliers                        |
| 6. Product Sales by Region            | Grouped Bar / Stacked Bar      | Compare regions + categories                     |
| 7. Detecting Correlations             | Pairplot                       | Pairwise relationships visualized                |
| 8. Website Traffic by Day             | Line Chart                     | Continuous data trend                            |
| 9. Market Share Changes               | Stacked Area Chart             | Shows part-to-whole over time                    |
| 10. Call Center Analysis              | Heatmap                        | Color-coded large dataset                        |
| 11. Comparing Product Revenues        | Treemap                        | Hierarchical relationships                       |
| 12. Comparing Three Variables         | Bubble Chart                   | Third variable shown by size                     |
| 13. Daily Sales & Total Volume        | Area Chart                     | Emphasizes cumulative magnitude                  |
| 14. Large Sensor Dataset Distribution | Histogram / Density Plot       | Efficient for large data                         |
| 15. Customer Clusters                 | Scatter Plot                   | Two-variable relationships clearly               |
| 16. Correlation Between Variables     | Heatmap                        | Correlation matrix visualization                 |
| 17. Many Categories                   | Treemap                        | Summarizes hundreds of categories                |
| 18. Multiple Stocks                   | Multi-line Chart               | Easy to compare multiple trends                  |
| 19. Employee Skill Improvement        | Radar Chart or Small Multiples | Compare growth in skill areas                    |
| 20. Exam Score Distribution Shape     | Histogram or Density Plot      | Histogram shows bins, density shows smooth shape |

</details>

---

# **How to Use This for Exam Prep**

1. **Try answering without looking at the key** to test understanding.
2. Think about:

   * Data type (categorical, numerical, mixed)
   * Analysis goal (trend, comparison, proportion, distribution, relationship)
   * Dataset size (small vs large)
3. Cross-check your answers with the key to reinforce concepts.
4. Redo questions where you struggled.


---

**advanced visualization tools and techniques**
We'll cover:

1. **Interactive Plots with Plotly**
2. **Interactive Plots with Bokeh**
3. **Advanced Seaborn Techniques**
4. **Pairplot in Seaborn**
5. **Catplot in Seaborn**
6. **FacetGrid in Seaborn**

For each topic, I’ll explain:

* **Definition** – what it is
* **Use Cases** – why and when to use it
* **Simple Code Snippet** – so you can practice hands-on

---

# **1. Interactive Plots with Plotly**

---

### **Definition**

[Plotly](https://plotly.com/python/) is a **Python visualization library** that creates **interactive, browser-based graphs**.
Unlike static matplotlib charts, Plotly allows:

* Zooming, panning
* Hover tooltips
* Exporting directly to HTML for sharing.

Plotly has two main APIs:

* **Plotly Express** → High-level, easy-to-use.
* **Graph Objects** → Low-level, fully customizable.

---

### **Use Cases**

| **Scenario**                      | **Why Plotly**                   |
| --------------------------------- | -------------------------------- |
| Presenting to stakeholders        | Interactive, user-friendly       |
| Financial data exploration        | Zoom in/out of stock trends      |
| Live dashboards (e.g., Dash apps) | Real-time visualization          |
| Large datasets                    | Filter and hover to inspect data |

---

### **Simple Example: Interactive Line Chart**

```python
import plotly.express as px
import pandas as pd

# Sample dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 120, 150, 170, 200]
}
df = pd.DataFrame(data)

# Create interactive line chart
fig = px.line(df, x="Month", y="Sales", title="Monthly Sales Trend")
fig.show()
```

**Features:**

* Hover to see exact values
* Drag to zoom
* Download plot as PNG directly

---

### **Other Plotly Chart Types**

* `px.scatter()` → Interactive scatter plots
* `px.bar()` → Interactive bar charts
* `px.choropleth()` → Maps
* `px.pie()` → Pie charts

---

# **2. Interactive Plots with Bokeh**

---

### **Definition**

[Bokeh](https://docs.bokeh.org/) is another **interactive visualization library** that generates plots for web browsers.

* Focused on **real-time streaming data** and **dashboards**.
* Lightweight and faster than Plotly for certain use cases.

---

### **Use Cases**

| **Use Case**              | **Why Bokeh**                   |
| ------------------------- | ------------------------------- |
| Real-time IoT monitoring  | Can stream live updates         |
| Web dashboard integration | Embeds easily into web apps     |
| Large dataset handling    | Better performance on huge data |
| Custom interactivity      | Widgets like sliders, buttons   |

---

### **Simple Example: Interactive Line Chart**

```python
from bokeh.plotting import figure, show, output_notebook

# To display in Jupyter Notebook
output_notebook()

# Create a figure
p = figure(title="Sales Over Months",
           x_axis_label='Month',
           y_axis_label='Sales')

months = [1, 2, 3, 4, 5]
sales = [100, 120, 150, 170, 200]

# Add line and points
p.line(months, sales, line_width=2, color="green")
p.circle(months, sales, size=8, color="blue")

show(p)
```

**Features:**

* Hover and zoom tools by default.
* Can add sliders, dropdowns, and widgets.

---

# **3. Advanced Seaborn Techniques**

---

### **Definition**

[Seaborn](https://seaborn.pydata.org/) is a **statistical data visualization library** built on top of Matplotlib.
While basic Seaborn plots are straightforward, **advanced techniques** allow:

* Complex, multi-variable plots
* Statistical overlays (confidence intervals, regression lines)
* Grid-based layouts like FacetGrid and Pairplot
* Categorical plots like Catplot

---

### **Use Cases**

| **Scenario**                    | **Advanced Feature to Use** |
| ------------------------------- | --------------------------- |
| Compare distributions           | Violin plots, Boxplots      |
| Regression analysis             | `sns.lmplot()`              |
| Comparing multiple categories   | `sns.catplot()`             |
| Multiple plots in a grid layout | `FacetGrid`                 |
| Explore pairwise relationships  | `Pairplot`                  |

---

### **Example: Advanced Scatter Plot with Regression**

```python
import seaborn as sns
import pandas as pd

# Load built-in dataset
df = sns.load_dataset("tips")

# Scatter plot with regression line
sns.lmplot(x="total_bill", y="tip", data=df, hue="sex", height=5)
```

**Features:**

* Automatically fits a regression line.
* Separates data by gender (`hue="sex"`).
* Perfect for statistical exploration.

---

### **Other Advanced Seaborn Features**

* `sns.violinplot()` → Shows data distribution and density
* `sns.swarmplot()` → Shows individual points
* `sns.lmplot()` → Linear regression
* `sns.jointplot()` → Combine scatter + histogram/density

---

# **4. Pairplot in Seaborn**

---

### **Definition**

`Pairplot` is a **Seaborn function** that plots **pairwise relationships** between multiple numerical variables in a dataset.

* Diagonal shows **distribution plots (histogram or KDE)**.
* Off-diagonal shows **scatter plots**.

---

### **Use Cases**

| **When to Use Pairplot**        | **Why**                                           |
| ------------------------------- | ------------------------------------------------- |
| Explore multi-variable datasets | See relationships between every pair of variables |
| Detect correlations quickly     | Visual, pairwise correlation                      |
| Identify clusters and outliers  | Easy to spot unusual patterns                     |

---

### **Example: Pairplot**

```python
import seaborn as sns

# Load Iris dataset
df = sns.load_dataset("iris")

# Create pairplot
sns.pairplot(df, hue="species")
```

**Features:**

* Colors separate species (`hue="species"`).
* Helps detect which flower features distinguish species best.

---

# **5. Catplot in Seaborn**

---

### **Definition**

`Catplot` is a **high-level Seaborn function** for creating **categorical plots** like bar plots, box plots, strip plots, etc., **in a single function call**.

---

### **Use Cases**

| **Goal**                              | **Best Catplot Kind**  |
| ------------------------------------- | ---------------------- |
| Compare category means                | Bar (`kind="bar"`)     |
| Show distribution spread per category | Box (`kind="box"`)     |
| Visualize individual points           | Strip (`kind="strip"`) |

---

### **Example: Catplot - Bar Chart**

```python
import seaborn as sns

# Load dataset
df = sns.load_dataset("tips")

# Create bar chart for average tip per day
sns.catplot(x="day", y="tip", data=df, kind="bar", hue="sex")
```

**Features:**

* Aggregates automatically (default = mean).
* Adds grouping via `hue`.

---

# **6. FacetGrid in Seaborn**

---

### **Definition**

`FacetGrid` is a **Seaborn class** that allows you to **create multiple subplots** based on **category combinations**.
It’s perfect for:

* Comparing the same visualization across subsets of data.
* Creating multi-panel plots efficiently.

---

### **Use Cases**

| **Scenario**                             | **FacetGrid Benefit**     |
| ---------------------------------------- | ------------------------- |
| Compare male vs female tips per day      | Separate plots per gender |
| Visualize trends across multiple regions | Grid layout by region     |
| Multi-category comparisons               | Automated faceting        |

---

### **Example: FacetGrid**

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("tips")

# Create a grid by 'sex' and 'time'
g = sns.FacetGrid(df, col="sex", row="time")

# Add scatter plot inside each facet
g.map(sns.scatterplot, "total_bill", "tip")

plt.show()
```

**Features:**

* Rows = Time (`Lunch/Dinner`)
* Columns = Gender (`Male/Female`)
* Helps visualize differences clearly.

---

# **Comparison Table**

| **Feature**        | **Plotly**                | **Bokeh**           | **Seaborn Advanced**  |
| ------------------ | ------------------------- | ------------------- | --------------------- |
| **Type**           | Interactive, Web          | Interactive, Web    | Static (High-quality) |
| **Ease of Use**    | High (Plotly Express)     | Medium              | High                  |
| **Real-time Data** | Yes                       | Yes (Better)        | No                    |
| **Customization**  | High                      | Very High           | Moderate              |
| **Best Use**       | Dashboards, Presentations | IoT, Live Data, Web | Statistical Analysis  |

---

# **Summary**

| **Topic**            | **What It Solves**               | **Key Function**                   |
| -------------------- | -------------------------------- | ---------------------------------- |
| **Plotly**           | Interactive, browser-ready plots | `px.line()`, `px.scatter()`        |
| **Bokeh**            | Live streaming dashboards        | `figure()`, `.line()`, `.circle()` |
| **Advanced Seaborn** | Complex statistical plots        | `sns.lmplot()`, `sns.violinplot()` |
| **Pairplot**         | Pairwise relationships           | `sns.pairplot()`                   |
| **Catplot**          | Categorical plotting             | `sns.catplot(kind=...)`            |
| **FacetGrid**        | Multi-panel subplots             | `sns.FacetGrid()`                  |

---

# Popular charts codes in seaborn and matplotlib

**syntax generic**:

* `df` → DataFrame
* `x` → column name for x-axis
* `y` → column name for y-axis
* `hue` → column for categorical grouping (if needed)

Each chart is given **separately** for clarity.

---

## **1. Bar Graph (Vertical & Horizontal)**

```python
import matplotlib.pyplot as plt

# Vertical Bar Chart
plt.bar(df['x'], df['y'])
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Vertical Bar Chart')
plt.show()

# Horizontal Bar Chart
plt.barh(df['x'], df['y'])
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Horizontal Bar Chart')
plt.show()
```

---

## **2. Line Graph**

```python
plt.plot(df['x'], df['y'], marker='o')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Line Graph')
plt.grid(True)
plt.show()
```

---

## **3. Pie Chart**

```python
plt.pie(df['y'], labels=df['x'], autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')
plt.show()
```

---

## **4. Scatter Plot**

```python
plt.scatter(df['x'], df['y'])
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Scatter Plot')
plt.show()
```

---

## **5. Area Chart**

```python
plt.fill_between(df['x'], df['y'], alpha=0.5)
plt.plot(df['x'], df['y'], color='blue')  # line on top
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Area Chart')
plt.show()
```

---

## **6. Radar Chart (Spider Chart)**

> Matplotlib doesn't have a direct API, we use `polar` projection.

```python
import numpy as np

categories = df['x']
values = df['y']

# Angles for each axis
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
values = np.concatenate((values, [values[0]]))  # Close the circle
angles += angles[:1]

fig, ax = plt.subplots(subplot_kw={'polar': True})
ax.plot(angles, values, color='blue')
ax.fill(angles, values, color='blue', alpha=0.25)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
plt.title('Radar Chart')
plt.show()
```

---

## **7. Histogram**

```python
plt.hist(df['x'], bins=10, edgecolor='black')
plt.xlabel('X Label')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
```

---

## **8. Tree Map** (Requires `squarify` library)

> Matplotlib doesn't have built-in support.

```python
import squarify

sizes = df['y']
labels = df['x']

squarify.plot(sizes=sizes, label=labels, alpha=0.7)
plt.axis('off')
plt.title('Tree Map')
plt.show()
```

---

## **9. Pairplot (Seaborn)**

> No direct Matplotlib equivalent, must use Seaborn.

```python
import seaborn as sns

sns.pairplot(df)
plt.show()
```

---

## **10. Boxplot**

```python
plt.boxplot(df['y'])
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Boxplot')
plt.show()

# With categories
plt.boxplot([df[df['x'] == category]['y'] for category in df['x'].unique()],
            labels=df['x'].unique())
plt.title('Boxplot by Category')
plt.show()
```

---

## **11. Bubble Chart**

```python
# Assuming 'size' column for bubble sizes
plt.scatter(df['x'], df['y'], s=df['size'], alpha=0.5)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Bubble Chart')
plt.show()
```

---

## **12. Heatmap (Seaborn for simplicity)**

> Matplotlib can do with `imshow()`, but Seaborn is easier.

```python
import seaborn as sns

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap')
plt.show()
```

---

## **13. Catplot (Seaborn)**

> Specialized for categorical data visualizations.

```python
sns.catplot(x='x', y='y', hue='hue', kind='bar', data=df)
plt.title('Catplot - Bar')
plt.show()
```

---

## **14. FacetGrid (Seaborn)**

```python
g = sns.FacetGrid(df, col='hue')
g.map_dataframe(sns.scatterplot, x='x', y='y')
g.add_legend()
plt.show()
```

---

## **15. Stack Plot (Stacked Area Chart)**

```python
# Multiple series stacked
plt.stackplot(df['x'], df['y1'], df['y2'], df['y3'], labels=['Y1', 'Y2', 'Y3'])
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Stacked Area Chart')
plt.legend(loc='upper left')
plt.show()
```

---

## **16. Step Plot**

```python
plt.step(df['x'], df['y'], where='mid')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Step Plot')
plt.show()
```

---

## **17. Violin Plot (Seaborn)**

```python
sns.violinplot(x='x', y='y', data=df)
plt.title('Violin Plot')
plt.show()
```

---

## **18. KDE Plot (Seaborn or Matplotlib)**

```python
sns.kdeplot(df['x'], fill=True)
plt.title('KDE Plot')
plt.show()
```

---

## **19. Donut Chart**

> A Pie Chart variation.

```python
wedges, texts, autotexts = plt.pie(df['y'], labels=df['x'], autopct='%1.1f%%', startangle=90)
# Create center circle for donut
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Donut Chart')
plt.show()
```

---

## **20. Polar Plot**

```python
theta = np.linspace(0, 2*np.pi, len(df['x']))
r = df['y']

plt.subplot(projection='polar')
plt.plot(theta, r)
plt.title('Polar Plot')
plt.show()
```

---

## **21. Error Bar Plot**

```python
# Assuming 'error' column
plt.errorbar(df['x'], df['y'], yerr=df['error'], fmt='o', ecolor='red', capsize=5)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Error Bar Plot')
plt.show()
```

---

## **22. Horizontal Stacked Bar**

```python
plt.barh(df['x'], df['y1'], label='Y1')
plt.barh(df['x'], df['y2'], left=df['y1'], label='Y2')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Horizontal Stacked Bar Chart')
plt.legend()
plt.show()
```

---

## **23. Hexbin Plot**

```python
plt.hexbin(df['x'], df['y'], gridsize=20, cmap='Blues')
plt.colorbar(label='count')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Hexbin Plot')
plt.show()
```

---

## **24. Density Contour Plot (Seaborn)**

```python
sns.kdeplot(x='x', y='y', data=df, fill=True, cmap='mako')
plt.title('Density Contour Plot')
plt.show()
```

---