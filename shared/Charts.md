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
