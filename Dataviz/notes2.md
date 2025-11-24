# 📘 Data Visualization Exam Master Guide

**Course Code:** BCSE 0713 / BCSE 0743  
**Target:** Theory Exam, Lab Exam, Viva, and MCQs  

---

# ✅ SECTION 1: ULTRA-DETAILED NOTES

## 🔹 MODULE I: FUNDAMENTALS & ADVANCED TECHNIQUES

### 1. Introduction to Data Visualization
*   **Definition:** The graphical representation of information and data using visual elements like charts, graphs, and maps.
*   **Importance:**
    *   **Pattern Detection:** Humans process visual data 60,000x faster than text. Helps spot trends, outliers, and correlations.
    *   **Communication:** Simplifies complex data for stakeholders (storytelling).
    *   **Decision Making:** Enables data-driven decisions by making insights accessible.
*   **Applications:** Business Intelligence (Sales dashboards), Healthcare (Patient vitals monitoring), Finance (Stock trends), AI (Model performance).
*   **Tools:**
    *   **Code-based:** Python (Matplotlib, Seaborn, Plotly), R (ggplot2).
    *   **GUI-based:** Tableau, Power BI, Excel.

### 2. Visual Perception & Cognitive Load
*   **Visual Perception:** How the brain processes visual information.
    *   **Preattentive Attributes:** Visual properties we notice immediately without conscious effort.
        *   *Examples:* Color, Size, Orientation, Shape, Enclosure, Position (Position is the most accurate attribute for quantitative data).
*   **Cognitive Load:** The amount of mental effort required to understand a visualization.
    *   **Intrinsic Load:** Complexity of the data itself (cannot be removed, must be managed).
    *   **Extraneous Load:** Useless clutter (chartjunk) that confuses the user. **Goal: Minimize this.**
    *   **Germane Load:** Effort used to actually learn/understand the pattern. **Goal: Maximize this.**
*   **Gestalt Principles:**
    *   **Proximity:** Objects close together are perceived as a group.
    *   **Similarity:** Objects with same color/shape are perceived as related.
    *   **Enclosure:** Objects with a border around them are a group.
    *   **Continuity:** Eyes follow smooth paths (lines) over abrupt changes.

### 3. Principles of Good Visualization
*   **Clarity:** The message should be unambiguous. Avoid 3D charts for 2D data.
*   **Accuracy:** Representation must match the data. Avoid truncated axes (starting Y-axis at 50 instead of 0 to exaggerate differences).
*   **Aesthetics:** Pleasing design engages users but shouldn't compromise clarity.
*   **Tufte’s Principles:**
    *   **Data-Ink Ratio:** $\frac{\text{Data-Ink}}{\text{Total Ink}}$. Maximize this. Remove backgrounds, borders, and redundant labels.
    *   **Chartjunk:** Useless decorations (3D effects, patterns) that add no information.
    *   **Lie Factor:** $\frac{\text{Size of effect in graphic}}{\text{Size of effect in data}}$. Should be ~1.

### 4. Chart Types & Use Cases

| Chart Type | Best Use Case | Key Features |
| :--- | :--- | :--- |
| **Bar Chart** | Comparing categories (nominal/ordinal). | Length represents value. Vertical (Column) or Horizontal (Bar). |
| **Line Chart** | Trends over time (Time Series). | Connects data points. Good for continuous data. |
| **Pie Chart** | Part-to-whole composition. | **Avoid** if >5 categories. Hard to compare slice angles. |
| **Scatter Plot** | Relationship/Correlation between 2 numerical variables. | Shows clusters, outliers, linear/non-linear trends. |
| **Histogram** | Distribution of a single numerical variable. | Bins data into ranges. Bars touch each other (unlike bar charts). |
| **Boxplot** | Statistical summary (Min, Q1, Median, Q3, Max). | Shows spread and **outliers** (dots outside whiskers). |
| **Heatmap** | Matrix data, correlation matrices. | Uses color intensity to represent values. |
| **Bubble Chart** | Relationship between 3 variables. | X-axis, Y-axis, and Bubble Size (3rd variable). |
| **Area Chart** | Cumulative totals over time. | Like a line chart but filled. Stacked area shows part-to-whole over time. |

### 5. Advanced Visualization Techniques
*   **Interactive Plots:** Allow users to explore data (Zoom, Pan, Hover, Filter).
    *   **Libraries:** Plotly (Python/JS), Bokeh.
*   **Advanced Seaborn:**
    *   **Pairplot:** Plots pairwise relationships in a dataset. (Scatter plots for joint, histograms for diagonal).
    *   **FacetGrid:** "Small Multiples". Creating the same chart for different subsets of data (e.g., Sales vs Time for each *Region*).
    *   **Catplot:** Figure-level interface for drawing categorical plots.
*   **Dashboards:**
    *   **Plotly Dash / Streamlit:** Python frameworks to build web-based data apps.
    *   **Structure:** Input controls (Sidebar) -> Callbacks (Logic) -> Output Graphs.

### 6. Multidimensional & Time Series Data
*   **Multidimensional:** Visualizing >3 variables.
    *   *Techniques:* Color, Size, Shape, Faceting (Subplots), Interactive drilling.
    *   *Parallel Coordinates:* Good for high-dimensional data.
*   **Time Series:**
    *   *Components:* Trend (Long-term), Seasonality (Repeating pattern), Noise (Random).
    *   *Viz:* Line charts, Area charts, Horizon plots.

### 7. Geo-Visualization
*   **Tools:** Folium (Leaflet wrapper), Plotly Mapbox.
*   **Choropleth Map:** Regions colored based on a value (e.g., GDP by country).
*   **Symbol Map:** Bubbles/markers on specific lat/long coordinates.

### 8. AI/ML Model Interpretability
*   **Black Box Problem:** Complex models (Neural Nets) are hard to explain.
*   **SHAP (SHapley Additive exPlanations):** Game theory based. Explains the contribution of each feature to a specific prediction.
*   **Partial Dependence Plots (PDP):** Shows the marginal effect of one or two features on the predicted outcome (Global interpretation).

### 9. Ethical & Cultural Aspects
*   **Ethics:**
    *   **Misleading Axes:** Truncating Y-axis to exaggerate growth.
    *   **Cherry-picking:** Showing only data that supports a bias.
    *   **Inverted Axes:** Flipping axes to hide trends.
*   **Cultural:** Color meanings vary (Red = Danger in West, Luck in China). Reading direction (LTR vs RTL).
*   **Accessibility:** Design for Color Blindness (Avoid Red-Green combinations, use textures/labels).

---

## 🔹 MODULE II: BUSINESS INTELLIGENCE (POWER BI & TABLEAU)

### 1. Introduction to BI
*   **Business Intelligence (BI):** Technologies to analyze data and deliver actionable information.
*   **Power BI:** Microsoft product. Good integration with Excel/Azure. Uses DAX.
*   **Tableau:** Salesforce product. Stronger visual capabilities. Uses VizQL.

### 2. Connecting to Data
*   **Sources:** Excel, CSV, SQL Server, Web, Cloud (AWS/Azure).
*   **Tableau Connection Types:**
    *   **Live:** Direct connection to DB. Real-time data. Slow if DB is slow.
    *   **Extract:** Snapshot of data saved locally (.hyper). Faster performance. Needs scheduled refresh.
*   **Power BI Connection Types:**
    *   **Import:** Data loaded into Power BI cache. Fast. Size limit.
    *   **Direct Query:** Data stays in source. Queries sent on fly. Always current. Slower.

### 3. Data Preparation (ETL)
*   **Power BI:** Uses **Power Query Editor**.
    *   **M Language:** The formula language behind Power Query.
    *   **Operations:** Remove top rows, Use first row as headers, Change types, Replace values, Pivot/Unpivot.
*   **Tableau:** Uses **Data Interpreter** (Auto-cleans messy Excel) or **Tableau Prep**.

### 4. Data Modeling
*   **Schema:** Organizing tables. **Star Schema** is best for BI (Fact table in center, Dimension tables around).
*   **Cardinality:**
    *   **1-to-1:** One row in Table A matches one in Table B.
    *   **1-to-Many:** One row in A matches many in B (e.g., Customer -> Orders). Most common.
    *   **Many-to-Many:** Avoid if possible (requires bridge table).

### 5. Calculations
*   **Power BI (DAX - Data Analysis Expressions):**
    *   **Calculated Column:** Computed row-by-row, stored in RAM. (e.g., `Profit = Sales - Cost`). Used for filtering/slicing.
    *   **Measure:** Computed on the fly based on context (aggregation). (e.g., `Total Sales = SUM(Sales)`). Used in values area.
*   **Tableau:**
    *   **Calculated Fields:** `SUM([Sales]) - SUM([Cost])`.
    *   **LOD Expressions (Level of Detail):** `{FIXED [Region]: SUM([Sales])}`. Computes values at a specific level independent of the view.

### 6. Core BI Features
*   **Filters:** Restrict data.
    *   *Visual Level:* Only one chart.
    *   *Page Level:* All charts on a page.
    *   *Report Level:* All pages.
*   **Slicers (Power BI):** On-canvas visual filters for user interaction.
*   **Parameters (Tableau):** Dynamic values users can change (e.g., "Top N" customers, "What-if" analysis).
*   **Sets (Tableau):** Custom fields that define a subset of data based on conditions (e.g., "High Profit Customers").
*   **Groups:** Combining dimension members (e.g., Grouping "USA", "Canada", "Mexico" as "North America").
*   **Drill-down:** Moving from high-level (Year) to detailed (Month -> Day) data.

### 7. Dashboards & Storytelling
*   **Dashboard:** Collection of views (charts) to compare data simultaneously.
*   **Story (Tableau):** Sequence of visualizations that work together to convey information (Narrative flow).
*   **Interactivity:**
    *   **Filter Actions:** Clicking a bar in Chart A filters Chart B.
    *   **Highlight Actions:** Dimming non-selected data.
    *   **URL Actions:** Opening external links.
*   **Publishing:**
    *   **Power BI Service:** Cloud platform to share reports.
    *   **Tableau Server / Public:** Sharing platform.

---

#  SECTION 2: 50 THEORY QUESTIONS (WITH MODEL ANSWERS)

##  Short Answer Questions (2-3 Marks)

**1. Define Data Visualization.**
**Ans:** Data visualization is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data.

**2. What is the difference between Information and Data?**
**Ans:** Data is raw, unorganized facts (e.g., 34, 55, 60). Information is data processed, organized, or structured to make it useful (e.g., Average score of the class is 49.6).

**3. Explain 'Preattentive Attributes' with examples.**
**Ans:** Visual properties that we notice immediately without conscious effort. Examples:
*   **Color:** Red dot in a sea of blue dots.
*   **Size:** A large bubble among small ones.
*   **Orientation:** A tilted line among vertical lines.

**4. What is Cognitive Load in the context of visualization?**
**Ans:** It is the mental effort required to interpret a visualization. Good design minimizes *extraneous load* (clutter) and manages *intrinsic load* (complexity) to maximize *germane load* (understanding).

**5. Define 'Data-Ink Ratio'.**
**Ans:** Coined by Edward Tufte, it is the proportion of a graphic's ink devoted to the non-redundant display of data-information.
d:\B.Tech\ProjeX\PublicFiles\Dataviz \text{Data-Ink Ratio} = \frac{\text{Data-Ink}}{\text{Total Ink used in Graphic}} d:\B.Tech\ProjeX\PublicFiles\Dataviz
Goal: Maximize this ratio.

**6. What is 'Chartjunk'?**
**Ans:** Visual elements in charts and graphs that are not necessary to comprehend the information represented on the graph, or that distract the viewer from this information (e.g., heavy grid lines, 3D effects, background images).

**7. Differentiate between Categorical and Numerical data.**
**Ans:**
*   **Categorical (Qualitative):** Describes qualities or characteristics (e.g., Name, Gender, City).
*   **Numerical (Quantitative):** Measures of values or counts (e.g., Age, Salary, Height).

**8. When should you use a Bar Chart vs. a Line Chart?**
**Ans:**
*   **Bar Chart:** For comparing values across distinct categories (e.g., Sales by Product).
*   **Line Chart:** For showing trends over continuous time intervals (e.g., Stock price over a year).

**9. What is a Histogram?**
**Ans:** A graphical representation of the distribution of numerical data. It groups data into bins (ranges) and displays the frequency of data points in each bin.

**10. What is the purpose of a Boxplot?**
**Ans:** To display the distribution of data based on a five-number summary: minimum, first quartile (Q1), median, third quartile (Q3), and maximum. It is excellent for detecting outliers.

**11. Define 'Lie Factor'.**
**Ans:** A measure of how much a graphic distorts the data it represents.
d:\B.Tech\ProjeX\PublicFiles\Dataviz \text{Lie Factor} = \frac{\text{Size of effect shown in graphic}}{\text{Size of effect in data}} d:\B.Tech\ProjeX\PublicFiles\Dataviz
A value close to 1 is ideal.

**12. What is a Heatmap?**
**Ans:** A data visualization technique that shows magnitude of a phenomenon as color in two dimensions. Often used for correlation matrices.

**13. What is the difference between Tableau Live and Extract connections?**
**Ans:**
*   **Live:** Connects directly to the data source; data is real-time but performance depends on the database.
*   **Extract:** Creates a local snapshot (.hyper file); faster performance but requires scheduled refreshes.

**14. What is a Dashboard?**
**Ans:** A visual display of the most important information needed to achieve one or more objectives, consolidated and arranged on a single screen so the information can be monitored at a glance.

**15. What is DAX?**
**Ans:** Data Analysis Expressions (DAX) is a formula language used in Power BI, SSAS, and Power Pivot to create custom calculations (measures and calculated columns).

**16. What is the difference between a Measure and a Calculated Column in Power BI?**
**Ans:**
*   **Calculated Column:** Computed row-by-row and stored in the table (increases file size).
*   **Measure:** Computed on the fly based on the filter context (dynamic aggregation).

**17. What is a Slicer in Power BI?**
**Ans:** An on-canvas visual filter that allows users to segment the data displayed in other visualizations on the report page.

**18. What is 'Drill-down'?**
**Ans:** A capability that allows users to navigate from a high-level view of data to a more granular level (e.g., Year -> Quarter -> Month).

**19. What is a Choropleth Map?**
**Ans:** A thematic map where geographical areas are shaded or patterned in proportion to the value of an aggregate variable (e.g., Population density by state).

**20. What is SHAP in AI interpretability?**
**Ans:** SHapley Additive exPlanations. It assigns each feature an importance value for a particular prediction, explaining how much each feature contributed to the result.

---

##  Long Answer Questions (5 Marks)

**21. Explain the Gestalt Principles of Visual Perception with examples.**
**Ans:**
Gestalt principles describe how the human eye perceives visual elements as a unified whole.
1.  **Proximity:** Elements close to each other are perceived as a group. *Example:* Dots clustered together represent a single category.
2.  **Similarity:** Elements with similar characteristics (color, shape) are grouped. *Example:* All red bars in a chart are seen as related.
3.  **Enclosure:** Elements enclosed in a boundary are seen as a group. *Example:* A box around a set of points.
4.  **Continuity:** The eye follows smooth paths. *Example:* Line charts are easier to follow than scattered dots.
5.  **Closure:** The brain fills in missing information to create a complete image.

**22. Discuss the ethical issues in Data Visualization.**
**Ans:**
Visualization can be manipulated to mislead. Common unethical practices:
1.  **Truncated Axes:** Starting the Y-axis at a non-zero value to exaggerate small differences.
2.  **Cherry-picking:** Selecting only specific timeframes or data points that support a biased narrative.
3.  **Inverted Axes:** Flipping the axis to make a decline look like an increase (or vice versa).
4.  **Improper Scaling:** Using area/volume (3D) to represent linear data, distorting perception.
5.  **Color Bias:** Using colors that imply 'good' or 'bad' inappropriately (e.g., Red for profit).

**23. Compare Power BI and Tableau.**
**Ans:**
| Feature | Power BI | Tableau |
| :--- | :--- | :--- |
| **Owner** | Microsoft | Salesforce |
| **Learning Curve** | Easier (similar to Excel) | Steeper (more complex features) |
| **Data Engine** | VertiPaq (highly compressed) | Hyper (fast in-memory) |
| **Language** | DAX, M | VizQL |
| **Cost** | Cheaper (Pro version) | More expensive |
| **Customization** | Good, but structured | Extremely flexible |

**24. Explain the process of Data Cleaning (ETL) in Power BI.**
**Ans:**
Data cleaning is done in the **Power Query Editor**. Steps include:
1.  **Connect:** Import data from source (Excel, SQL).
2.  **Transform:**
    *   **Remove Rows:** Remove top/bottom rows or errors.
    *   **Promote Headers:** Use first row as headers.
    *   **Change Type:** Ensure numbers are numeric, dates are dates.
    *   **Replace Values:** Fix typos or nulls.
    *   **Pivot/Unpivot:** Reshape data for analysis.
3.  **Load:** Apply changes and load clean data into the model.

**25. What are the different types of Dashboards?**
**Ans:**
1.  **Strategic:** High-level overview for executives. Focuses on KPIs and long-term goals. (e.g., Annual Revenue Report).
2.  **Operational:** Real-time monitoring for junior management. Focuses on daily tasks. (e.g., Server Status Monitor).
3.  **Analytical:** Detailed data for analysts to explore. Heavy use of drill-downs and filters. (e.g., Sales Trends Analysis).

**26. Explain the concept of 'Storytelling with Data'.**
**Ans:**
It is the art of combining data, visuals, and narrative to communicate insights effectively.
*   **Context:** Who is the audience? What do they need to know?
*   **Visuals:** Choosing the right chart to show the pattern.
*   **Narrative:** Guiding the user through the data (Beginning, Middle, End).
*   **Call to Action:** What should the user do with this info?

**27. Describe the Star Schema in Data Modeling.**
**Ans:**
A mature modeling technique used in Data Warehousing and Power BI.
*   **Fact Table:** Central table containing quantitative data (metrics) and foreign keys (e.g., Sales table with SalesAmount, DateID, ProductID).
*   **Dimension Tables:** Surrounding tables containing descriptive attributes (e.g., Product table with ProductName, Category).
*   **Relationship:** One-to-Many relationship from Dimension to Fact.
*   **Benefit:** Optimized for query performance and simplicity.

**28. What is the difference between Import and Direct Query in Power BI?**
**Ans:**
*   **Import:**
    *   Data is copied into the Power BI file (.pbix).
    *   Very fast performance (uses in-memory engine).
    *   Supports all DAX functions.
    *   Data is only as fresh as the last refresh.
*   **Direct Query:**
    *   No data is stored in Power BI; queries are sent to the source.
    *   Slower performance.
    *   Limited DAX support.
    *   Data is always real-time.

**29. Explain the use of 'FacetGrid' and 'Pairplot' in Seaborn.**
**Ans:**
*   **FacetGrid:** Used to create a grid of charts based on a categorical variable. For example, plotting 'Tips vs Total Bill' separately for 'Smokers' and 'Non-Smokers' side-by-side. It helps in comparing subsets of data.
*   **Pairplot:** Creates a matrix of scatter plots for every pair of numerical variables in a dataset. The diagonal often shows histograms. It is used for exploratory data analysis to spot correlations quickly.

**30. What are the best practices for designing a Dashboard?**
**Ans:**
1.  **Know your audience:** Design for their specific needs.
2.  **5-Second Rule:** Key info should be understood in 5 seconds.
3.  **Layout:** Most important info goes top-left (F-pattern reading).
4.  **Simplicity:** Remove clutter, use consistent colors.
5.  **Interactivity:** Use slicers and tooltips wisely, don't overwhelm.
6.  **Context:** Provide titles, labels, and definitions.

---

##  Very Long Answer Questions (10 Marks)

**31. Detailed Guide on Choosing the Right Chart.**
**Ans:**
Choosing the right chart depends on the nature of the data and the question you want to answer.
1.  **Comparison:**
    *   *Among items:* **Bar Chart** (Column for few items, Bar for many).
    *   *Over time:* **Line Chart** (many periods), **Column Chart** (few periods).
2.  **Composition (Part-to-Whole):**
    *   *Static:* **Pie Chart** (simple), **Treemap** (hierarchical), **Stacked Bar** (absolute values).
    *   *Changing over time:* **Stacked Area Chart**, **Stacked Column Chart**.
3.  **Distribution:**
    *   *Single variable:* **Histogram** (frequency), **Density Plot**.
    *   *Two variables:* **Scatter Plot**.
    *   *Summary:* **Boxplot** (outliers).
4.  **Relationship:**
    *   *Two variables:* **Scatter Plot**.
    *   *Three variables:* **Bubble Chart**.
5.  **Geospatial:**
    *   *Values by region:* **Choropleth Map**.
    *   *Locations:* **Symbol Map**.

**32. Explain the entire workflow of a BI Project (from Data to Dashboard).**
**Ans:**
1.  **Requirement Gathering:** Understand business needs and KPIs.
2.  **Data Discovery:** Identify data sources (SQL, Excel, API).
3.  **Data Extraction & Cleaning (ETL):**
    *   Import data.
    *   Clean formatting, handle nulls, remove duplicates (Power Query).
4.  **Data Modeling:**
    *   Create relationships (Star Schema).
    *   Define cardinality (1-to-Many).
5.  **Calculations (DAX):**
    *   Create Measures for KPIs (e.g., YoY Growth, Profit Margin).
6.  **Visualization:**
    *   Build individual charts (Bar, Line, Maps).
    *   Apply formatting and colors.
7.  **Dashboarding:**
    *   Arrange charts on a canvas.
    *   Add interactivity (Slicers, Bookmarks).
8.  **Testing:** Validate numbers against source.
9.  **Deployment:** Publish to Power BI Service / Tableau Server.
10. **Maintenance:** Schedule refreshes and update as needed.

**33. Discuss 'Visual Perception' and how 'Preattentive Attributes' help in designing effective visualizations.**
**Ans:**
*   **Visual Perception** is the brain's ability to interpret light stimuli. In data viz, we exploit this to make patterns 'pop out'.
*   **Preattentive Attributes** are visual cues processed in < 200ms.
    *   **Form:** Length, Width, Orientation, Shape, Size, Enclosure.
        *   *Use:* Bar length for value, Line slope for trend.
    *   **Color:** Hue (Identity), Intensity (Value).
        *   *Use:* Red for alert, Blue for normal.
    *   **Spatial Position:** 2D position.
        *   *Use:* Scatter plot points.
*   **Application:**
    *   Use **Color** to highlight the most important data point (e.g., 'Your Sales' vs 'Market Average').
    *   Use **Length** for accurate comparisons (Bar charts are better than bubbles for precision).
    *   Use **Enclosure** to group related elements in a dashboard.
    *   *Example:* In a scatter plot of 100 points, making one point **Red** and **Large** instantly draws attention to it (Preattentive processing).

**34. Explain the architecture of Power BI.**
**Ans:**
Power BI consists of three main elements:
1.  **Power BI Desktop:** Windows application for development.
    *   *Power Query:* For ETL.
    *   *Power Pivot:* For modeling and DAX.
    *   *Power View:* For visualization.
2.  **Power BI Service (SaaS):** Cloud-based service.
    *   Used for publishing, sharing, and collaboration.
    *   Handles scheduled refreshes via **Gateways**.
    *   Allows creating Dashboards (pinning tiles from reports).
3.  **Power BI Mobile:** Apps for iOS/Android to view reports on the go.
*   **Flow:** Get Data (Desktop) -> Model & Visualize (Desktop) -> Publish (Service) -> Share (Mobile/Web).

**35. What is 'Model Interpretability'? Explain SHAP and Partial Dependence Plots.**
**Ans:**
*   **Interpretability:** The ability to explain *why* a machine learning model made a specific prediction. Crucial for trust in AI (e.g., Why was the loan rejected?).
*   **SHAP (SHapley Additive exPlanations):**
    *   Based on cooperative game theory.
    *   Calculates the marginal contribution of each feature to the prediction.
    *   *Global Interpretability:* Which features are most important overall?
    *   *Local Interpretability:* Why did *this specific* instance get this prediction?
    *   *Viz:* SHAP Summary Plot (beeswarm), SHAP Force Plot.
*   **Partial Dependence Plots (PDP):**
    *   Shows the relationship between a target feature and the predicted outcome, marginalizing over all other features.
    *   *Example:* How does 'House Price' change as 'Square Footage' increases, keeping everything else constant?
    *   *Viz:* Line graph showing the average prediction across different values of the feature.

---

##  Miscellaneous Important Questions

**36. What is the difference between Histogram and Bar Chart?**
**Ans:** Histogram is for numerical frequency distribution (bars touch), Bar Chart is for categorical comparison (bars have gaps).

**37. What is a Treemap?**
**Ans:** Displays hierarchical data using nested rectangles. Size and color represent values.

**38. What is a KPI Card?**
**Ans:** A simple visual that displays a single key metric (e.g., Total Revenue) prominently.

**39. What is a Bullet Chart?**
**Ans:** A variation of a bar chart developed by Stephen Few. It shows a primary measure (bar), a target (mark), and qualitative ranges (background shading). Great for tracking performance against goals.

**40. What is Data Granularity?**
**Ans:** The level of detail in the data. High granularity = detailed (daily sales). Low granularity = summarized (yearly sales).

**41. What is a 'Calculated Field' in Tableau?**
**Ans:** A new field created by a user using a formula to modify existing data or create new metrics.

**42. What is 'Binning'?**
**Ans:** Grouping continuous data into discrete intervals (bins). Used to create histograms.

**43. What is a 'Word Cloud'?**
**Ans:** A visual representation of text data where the size of each word indicates its frequency or importance.

**44. What is 'Overplotting' and how to fix it?**
**Ans:** When too many data points overlap in a scatter plot, making it a blob. Fixes: Decrease point size, make points transparent (alpha), or use a heatmap/contour plot.

**45. What is the difference between Discrete and Continuous fields in Tableau?**
**Ans:**
*   **Discrete (Blue):** Creates headers. Splits the view.
*   **Continuous (Green):** Creates axes. Adds a range.

**46. What is a 'Funnel Chart'?**
**Ans:** Shows values across multiple stages in a process (e.g., Sales Pipeline: Leads -> Qualified -> Closed).

**47. What is 'Z-order' in visualization?**
**Ans:** The order in which elements are stacked on top of each other (foreground vs background).

**48. What is the purpose of a 'Tooltip'?**
**Ans:** A message that appears when a cursor is positioned over an icon, image, hyperlink, or other element in a graphical user interface. Used to show details on hover.

**49. What is 'Exploratory Data Analysis' (EDA)?**
**Ans:** The initial process of analyzing data to summarize characteristics, often with visual methods, to understand the data structure before formal modeling.

**50. What is 'Data Storytelling' arc?**
**Ans:** Setup (Context) -> Conflict (The Problem/Insight) -> Resolution (The Solution/Action).


#  SECTION 3: VIVA QUESTIONS (60+ QUESTIONS)

##  Basic Conceptual Viva

1.  **What is the main goal of data visualization?**
    *   To communicate information clearly and efficiently.
2.  **Name 3 preattentive attributes.**
    *   Color, Size, Orientation.
3.  **Who is Edward Tufte?**
    *   A pioneer in data visualization, known for concepts like 'Chartjunk' and 'Data-Ink Ratio'.
4.  **What is a 'Lie Factor'?**
    *   A measure of distortion in a chart. Ideally, it should be 1.
5.  **What is the difference between a Bar chart and a Histogram?**
    *   Bar = Categories (gaps); Histogram = Distribution (no gaps).
6.  **When would you use a Pie chart?**
    *   Only for showing parts of a whole with few categories (<5).
7.  **What is a Scatter plot used for?**
    *   To show correlation between two numerical variables.
8.  **What is a Heatmap?**
    *   A matrix where values are represented by color intensity.
9.  **What is 'Chartjunk'?**
    *   Useless visual elements that distract from the data.
10. **What is a Dashboard?**
    *   A single screen consolidating key metrics and charts.
11. **What is 'Data Granularity'?**
    *   The level of detail (e.g., Daily vs Monthly).
12. **What is an Outlier?**
    *   A data point that differs significantly from other observations.
13. **Which chart is best for trends over time?**
    *   Line Chart.
14. **What is a Boxplot used for?**
    *   To show statistical distribution and outliers.
15. **What is the 'Data-Ink Ratio'?**
    *   The ratio of ink used for data vs total ink. Higher is better.

##  Medium Application-Based Viva

16. **How do you handle missing values in a dataset?**
    *   Remove rows, replace with mean/median, or keep as 'Unknown'.
17. **Why is a 3D Pie chart bad?**
    *   It distorts the angles, making it hard to compare slices accurately.
18. **What is the difference between Qualitative and Quantitative data?**
    *   Qualitative = Descriptive (Red, Blue); Quantitative = Numbers (10, 20).
19. **Explain 'Cognitive Load'.**
    *   The mental effort to understand a chart. We want to minimize extraneous load.
20. **What is a 'Dual-Axis' chart?**
    *   A chart with two Y-axes (e.g., Sales on left, Profit % on right). Can be misleading.
21. **What is 'Overplotting'?**
    *   When points overlap in a scatter plot. Fix with transparency or smaller points.
22. **What is a 'Treemap'?**
    *   Nested rectangles showing hierarchy and value (size/color).
23. **What is 'Geospatial Visualization'?**
    *   Visualizing data on maps (e.g., Choropleth).
24. **What is the difference between Correlation and Causation?**
    *   Correlation = Relationship; Causation = One causes the other. Viz shows correlation.
25. **What is 'Storytelling' in data?**
    *   Using narrative structure to guide the audience to an insight.
26. **What is 'Exploratory Data Analysis' (EDA)?**
    *   Initial investigation of data to discover patterns.
27. **What is a 'Bubble Chart'?**
    *   Scatter plot with a 3rd variable (Size).
28. **What is 'Faceting'?**
    *   Creating small multiples of the same chart for different categories.
29. **What is 'Interactive Visualization'?**
    *   Charts that allow zooming, filtering, and hovering.
30. **What is 'Color Blindness' considerations in Viz?**
    *   Avoid Red-Green combinations. Use Blue-Orange or patterns.

##  Lab-Based Viva (Power BI / Tableau)

31. **What is the difference between Power BI and Tableau?**
    *   Power BI = Microsoft ecosystem, DAX, cheaper. Tableau = Visual powerhouse, VizQL, expensive.
32. **What is 'Power Query'?**
    *   The ETL tool in Power BI for cleaning data.
33. **What is DAX?**
    *   Data Analysis Expressions. Formula language for Power BI.
34. **Difference between Measure and Calculated Column?**
    *   Measure = Dynamic (on the fly); Column = Static (stored in table).
35. **What is a 'Slicer'?**
    *   A visual filter on the canvas.
36. **What is 'Drill-down'?**
    *   Going from Year -> Quarter -> Month.
37. **What is a 'Tooltip'?**
    *   Info that pops up when you hover over a data point.
38. **What is the difference between Live and Extract in Tableau?**
    *   Live = Real-time; Extract = Snapshot (faster).
39. **What is a 'Dimension' vs 'Measure' in Tableau?**
    *   Dimension = Categorical (Blue); Measure = Numerical (Green).
40. **What is a 'Star Schema'?**
    *   Fact table in center, Dimensions around. Best for BI.
41. **What is 'Cardinality'?**
    *   Relationship type (1-to-1, 1-to-Many).
42. **What is 'M Language'?**
    *   The language behind Power Query.
43. **How do you merge queries in Power BI?**
    *   Using 'Merge Queries' (like SQL Join).
44. **What is 'Pivoting'?**
    *   Turning rows into columns.
45. **What is a 'Bookmark' in Power BI?**
    *   Saves the state of a report (filters, visibility) to create navigation.

##  Trick Viva Questions

46. **Can a Bar Chart have a non-zero baseline?**
    *   **NO.** It distorts the length comparison. Line charts can, but bar charts must start at 0.
47. **Is a higher Data-Ink ratio always better?**
    *   **Generally Yes,** but not if it removes necessary context (labels, axis lines).
48. **Can you use a Pie chart for 10 categories?**
    *   **Technically Yes, but practically NO.** It's unreadable. Use a Bar chart.
49. **Does 'Correlation imply Causation'?**
    *   **NO.** Just because ice cream sales and shark attacks correlate doesn't mean one causes the other (Summer is the cause).
50. **Is 'Red' always bad?**
    *   **No.** Context matters. In China, Red = Good/Luck. In heating, Red = Hot.
51. **What is the 'Lie Factor' of a 3D Bar chart?**
    *   Usually **High (>1)** because 3D volume exaggerates the value.
52. **If I filter a page, does it filter the underlying data source?**
    *   **No.** It only filters the *view*. The data remains in the model.
53. **Can a Measure be used in a Slicer?**
    *   **Generally No.** Slicers need categorical/discrete values (Columns).
54. **Is 'Import' mode in Power BI always faster?**
    *   **Usually Yes,** but it has a size limit. Direct Query is slower but handles massive data.
55. **What is the difference between 'Filter' and 'Highlight'?**
    *   Filter removes data; Highlight dims non-selected data but keeps it visible.
56. **Why use a Log Scale?**
    *   To visualize data with exponential growth or huge range differences.
57. **What is 'Chartjunk' again? Give a modern example.**
    *   Unnecessary animations or excessive gradients in a dashboard.
58. **What is the 'Z-pattern' vs 'F-pattern'?**
    *   Eye scanning patterns. Dashboards should follow these (Key info top-left).
59. **Can you create a relationship between two tables without a common column?**
    *   **No.** You need a key.
60. **What is 'Row-Level Security' (RLS)?**
    *   Restricting data access based on user roles (e.g., Manager sees only their region).


#  SECTION 5: 80 MCQs (WITH ANSWERS & EXPLANATIONS)

##  Part 1: General Concepts (1-20)

1.  **Which preattentive attribute is most accurate for quantitative data?**
    *   A) Color Intensity
    *   B) Position
    *   C) Size (Area)
    *   D) Shape
    *   **Ans: B (Position)** - Humans judge position along a scale more accurately than area or color.

2.  **What is the primary goal of minimizing 'Extraneous Cognitive Load'?**
    *   A) To make the chart look complex
    *   B) To remove clutter and distractions
    *   C) To increase data density
    *   D) To use more colors
    *   **Ans: B** - Extraneous load is useless mental effort caused by poor design.

3.  **According to Tufte, what should be maximized?**
    *   A) Chartjunk
    *   B) Data-Ink Ratio
    *   C) Lie Factor
    *   D) Grid lines
    *   **Ans: B** - More ink should be used for data, less for decoration.

4.  **Which Gestalt principle explains why we see a line graph as a continuous trend?**
    *   A) Proximity
    *   B) Closure
    *   C) Continuity
    *   D) Similarity
    *   **Ans: C** - The eye follows smooth paths.

5.  **A 'Lie Factor' of 2.0 means:**
    *   A) The graphic represents data accurately
    *   B) The graphic exaggerates the effect by 2x
    *   C) The graphic understates the effect by half
    *   D) The data is false
    *   **Ans: B** - Effect in graphic / Effect in data = 2.0.

6.  **Which chart is best for showing the distribution of a single variable?**
    *   A) Scatter Plot
    *   B) Histogram
    *   C) Line Chart
    *   D) Pie Chart
    *   **Ans: B** - Histograms show frequency distribution.

7.  **What is the main drawback of a Pie Chart?**
    *   A) It uses too much color
    *   B) Hard to compare angles/areas accurately
    *   C) Cannot show percentages
    *   D) It is 3D
    *   **Ans: B** - Humans struggle to compare angles.

8.  **Which chart is best for showing correlation between two variables?**
    *   A) Bar Chart
    *   B) Scatter Plot
    *   C) Area Chart
    *   D) Funnel Chart
    *   **Ans: B** - Scatter plots show relationship (X vs Y).

9.  **What does a Boxplot display?**
    *   A) Mean and Standard Deviation
    *   B) Five-number summary (Min, Q1, Median, Q3, Max)
    *   C) Frequency of categories
    *   D) Trends over time
    *   **Ans: B** - It summarizes distribution and outliers.

10. **What is 'Data Granularity'?**
    *   A) The size of the file
    *   B) The level of detail in the data
    *   C) The number of colors used
    *   D) The speed of the database
    *   **Ans: B** - E.g., Daily vs Monthly data.

11. **Which color palette is best for sequential data (Low to High)?**
    *   A) Red-Green-Blue
    *   B) Light Blue to Dark Blue
    *   C) Red to Green (Diverging)
    *   D) Random colors
    *   **Ans: B** - Single hue with varying intensity.

12. **What is 'Chartjunk'?**
    *   A) Useful data labels
    *   B) Unnecessary visual elements (3D, patterns)
    *   C) The title of the chart
    *   D) The legend
    *   **Ans: B** - Elements that add no information.

13. **When should you use a Dual-Axis chart?**
    *   A) Always
    *   B) Never
    *   C) With extreme caution, when variables have different scales
    *   D) To confuse the user
    *   **Ans: C** - It can be misleading if scales are manipulated.

14. **What is the 'Z-pattern' of reading?**
    *   A) Reading from bottom to top
    *   B) Scanning a page left-to-right, top-to-bottom
    *   C) Reading only the center
    *   D) Skipping text
    *   **Ans: B** - Common scanning pattern for dashboards.

15. **Which is a qualitative variable?**
    *   A) Salary
    *   B) Age
    *   C) Product Category
    *   D) Temperature
    *   **Ans: C** - It describes a quality/category.

16. **What is 'Overplotting'?**
    *   A) Plotting too many charts
    *   B) Data points overlapping in a scatter plot
    *   C) Using too many colors
    *   D) Printing the chart
    *   **Ans: B** - Makes it hard to see density.

17. **What is a 'Treemap' used for?**
    *   A) Time series analysis
    *   B) Hierarchical data and part-to-whole
    *   C) Geographic data
    *   D) Network graphs
    *   **Ans: B** - Nested rectangles.

18. **Which attribute is NOT preattentive?**
    *   A) Color
    *   B) Orientation
    *   C) Text Label Reading
    *   D) Size
    *   **Ans: C** - Reading requires conscious effort.

19. **What is 'Faceting' (Small Multiples)?**
    *   A) Splitting a chart into multiple smaller charts by category
    *   B) Using multiple colors
    *   C) Zooming in
    *   D) 3D rotation
    *   **Ans: A** - Helps compare sub-groups.

20. **What is the purpose of a 'Bullet Graph'?**
    *   A) To shoot data
    *   B) To replace gauges/meters and show performance vs target
    *   C) To show bullets
    *   D) To show time series
    *   **Ans: B** - Efficient space usage for target comparison.

##  Part 2: Tools (Power BI & Tableau) (21-40)

21. **Which language is used for calculations in Power BI?**
    *   A) SQL
    *   B) Python
    *   C) DAX
    *   D) Java
    *   **Ans: C** - Data Analysis Expressions.

22. **What is the file extension for a Tableau Packaged Workbook?**
    *   A) .twb
    *   B) .twbx
    *   C) .tde
    *   D) .hyper
    *   **Ans: B** - .twbx contains data + workbook.

23. **In Power BI, where do you clean data?**
    *   A) Report View
    *   B) Power Query Editor
    *   C) Model View
    *   D) DAX Editor
    *   **Ans: B** - The ETL tool.

24. **Which connection type in Tableau is faster for large datasets?**
    *   A) Live
    *   B) Extract
    *   C) Direct
    *   D) SQL
    *   **Ans: B** - Extract stores data locally in Hyper format.

25. **What is a 'Measure' in Power BI?**
    *   A) A static column
    *   B) A dynamic calculation based on context
    *   C) A table
    *   D) A database
    *   **Ans: B** - Aggregates on the fly.

26. **What does 'Drill Down' do?**
    *   A) Deletes data
    *   B) Moves from summary to detailed data
    *   C) Exports data
    *   D) Filters data
    *   **Ans: B** - Hierarchy navigation.

27. **Which visual is best for KPIs in Power BI?**
    *   A) Pie Chart
    *   B) Card
    *   C) Scatter Plot
    *   D) Map
    *   **Ans: B** - Shows a single big number.

28. **What is 'Row-Level Security' (RLS)?**
    *   A) Password protection
    *   B) Restricting data rows based on user role
    *   C) Encrypting the file
    *   D) Hiding columns
    *   **Ans: B** - Security feature.

29. **In Tableau, Blue fields are:**
    *   A) Continuous
    *   B) Discrete
    *   C) Measures
    *   D) Dates
    *   **Ans: B** - Discrete (Headers).

30. **In Tableau, Green fields are:**
    *   A) Continuous
    *   B) Discrete
    *   C) Dimensions
    *   D) Text
    *   **Ans: A** - Continuous (Axes).

31. **What is a 'Slicer'?**
    *   A) A knife
    *   B) A visual filter on the report canvas
    *   C) A type of chart
    *   D) A DAX function
    *   **Ans: B** - User-interactive filter.

32. **Which function counts rows in DAX?**
    *   A) SUM
    *   B) COUNTROWS
    *   C) AVERAGE
    *   D) MAX
    *   **Ans: B**.

33. **What is the 'Star Schema'?**
    *   A) A constellation
    *   B) Fact table surrounded by Dimension tables
    *   C) A single flat table
    *   D) Many-to-Many relationships
    *   **Ans: B** - Best practice for BI models.

34. **What is 'M' language used for?**
    *   A) Visualization
    *   B) Data Transformation (Power Query)
    *   C) Machine Learning
    *   D) Web Scraping
    *   **Ans: B**.

35. **How do you combine two tables with different columns (append)?**
    *   A) Merge Queries
    *   B) Append Queries
    *   C) Join
    *   D) Lookup
    *   **Ans: B** - Stack rows (Union).

36. **How do you combine two tables with a common column (join)?**
    *   A) Merge Queries
    *   B) Append Queries
    *   C) Union
    *   D) Stack
    *   **Ans: A** - Join columns.

37. **What is a 'Tooltip'?**
    *   A) A hint for the tool
    *   B) Info shown on hover
    *   C) A title
    *   D) A filter
    *   **Ans: B**.

38. **Can you use Python in Power BI?**
    *   A) No
    *   B) Yes, for Viz and Transformation
    *   C) Only for games
    *   D) Only in Pro version
    *   **Ans: B**.

39. **What is a 'Dashboard' in Power BI Service?**
    *   A) A single report page
    *   B) A collection of pinned visuals from different reports
    *   C) A dataset
    *   D) An app
    *   **Ans: B**.

40. **What is 'Direct Query'?**
    *   A) Importing data
    *   B) Querying source in real-time without storing data
    *   C) Writing SQL manually
    *   D) Using Excel
    *   **Ans: B**.

##  Part 3: Python & Advanced Viz (41-60)

41. **Which library is built on top of Matplotlib?**
    *   A) NumPy
    *   B) Seaborn
    *   C) Pandas
    *   D) Scikit-learn
    *   **Ans: B** - Makes Matplotlib prettier and easier.

42. **Which library is best for interactive web-based plots?**
    *   A) Matplotlib
    *   B) Plotly
    *   C) Seaborn
    *   D) Pandas
    *   **Ans: B** - Generates HTML/JS charts.

43. **What does sns.pairplot(df) do?**
    *   A) Plots a single line
    *   B) Plots pairwise relationships for all variables
    *   C) Plots a heatmap
    *   D) Errors out
    *   **Ans: B**.

44. **What is 'Folium' used for?**
    *   A) 3D modeling
    *   B) Map visualizations (Leaflet)
    *   C) Text analysis
    *   D) Audio processing
    *   **Ans: B**.

45. **What is SHAP used for?**
    *   A) Drawing shapes
    *   B) Model Interpretability
    *   C) Data Cleaning
    *   D) Web hosting
    *   **Ans: B**.

46. **How do you handle 'NaN' values in a heatmap?**
    *   A) They are automatically hidden
    *   B) They appear as white/blank spots
    *   C) The code crashes
    *   D) They turn red
    *   **Ans: B** (Usually).

47. **What is a 'Violin Plot'?**
    *   A) A musical instrument
    *   B) Combination of Boxplot and KDE (Density)
    *   C) A line chart
    *   D) A scatter plot
    *   **Ans: B**.

48. **Which plot shows the marginal effect of a feature?**
    *   A) Scatter Plot
    *   B) Partial Dependence Plot (PDP)
    *   C) Pie Chart
    *   D) Bar Chart
    *   **Ans: B**.

49. **What is 'Streamlit'?**
    *   A) A river
    *   B) A Python framework for building data apps
    *   C) A database
    *   D) A chart type
    *   **Ans: B**.

50. **What is 'Bokeh'?**
    *   A) A photography term
    *   B) An interactive visualization library for Python
    *   C) A flower
    *   D) A color
    *   **Ans: B**.

51. **In Matplotlib, what does plt.show() do?**
    *   A) Saves the plot
    *   B) Displays the plot
    *   C) Deletes the plot
    *   D) Hides the plot
    *   **Ans: B**.

52. **What is the 'Hue' parameter in Seaborn?**
    *   A) Changes the size
    *   B) Groups data by color based on a variable
    *   C) Changes the font
    *   D) Rotates the chart
    *   **Ans: B**.

53. **What is a 'Choropleth Map'?**
    *   A) A map with pins
    *   B) A map where regions are colored by value
    *   C) A road map
    *   D) A satellite map
    *   **Ans: B**.

54. **What is 'Geocoding'?**
    *   A) Writing code
    *   B) Converting address to Lat/Long
    *   C) Drawing maps
    *   D) Measuring distance
    *   **Ans: B**.

55. **What is 'Dash' by Plotly?**
    *   A) A running game
    *   B) A framework for building analytical web apps
    *   C) A chart
    *   D) A speed test
    *   **Ans: B**.

56. **What is 'Overfitting' in a model (visualized)?**
    *   A) Smooth curve
    *   B) Curve that wiggles to hit every single point (noise)
    *   C) Straight line
    *   D) Blank plot
    *   **Ans: B**.

57. **What is a 'Word Cloud'?**
    *   A) Text viz where size = frequency
    *   B) A weather chart
    *   C) A list of words
    *   D) A cloud storage
    *   **Ans: A**.

58. **What is 'Multidimensional Scaling' (MDS)?**
    *   A) Scaling an image
    *   B) Reducing dimensions to visualize similarity
    *   C) Increasing dimensions
    *   D) Weighing data
    *   **Ans: B**.

59. **What is 'Parallel Coordinates' plot?**
    *   A) Two parallel lines
    *   B) Viz for high-dimensional data using parallel axes
    *   C) A bar chart
    *   D) A map
    *   **Ans: B**.

60. **What is 'Data Storytelling'?**
    *   A) Reading a book
    *   B) Communicating insights with narrative and visuals
    *   C) Writing code
    *   D) Selling data
    *   **Ans: B**.

##  Part 4: Scenario & Application (61-80)

61. **You want to show the stock price trend over 10 years. Best chart?**
    *   A) Bar
    *   B) Pie
    *   C) Line
    *   D) Scatter
    *   **Ans: C**.

62. **You want to compare the GDP of 5 countries. Best chart?**
    *   A) Line
    *   B) Bar
    *   C) Scatter
    *   D) Histogram
    *   **Ans: B**.

63. **You want to see if 'Study Hours' affects 'Exam Score'. Best chart?**
    *   A) Bar
    *   B) Scatter Plot
    *   C) Pie
    *   D) Map
    *   **Ans: B**.

64. **You want to show the age distribution of 1000 people. Best chart?**
    *   A) Line
    *   B) Histogram
    *   C) Pie
    *   D) Scatter
    *   **Ans: B**.

65. **You want to show the market share of 3 companies. Best chart?**
    *   A) Pie Chart
    *   B) Line Chart
    *   C) Scatter Plot
    *   D) Histogram
    *   **Ans: A** (Since categories < 5).

66. **You want to show sales by State on a map. Best chart?**
    *   A) Bar Chart
    *   B) Filled Map (Choropleth)
    *   C) Line Chart
    *   D) Pie Chart
    *   **Ans: B**.

67. **You want to show the correlation between 3 variables (X, Y, Size). Best chart?**
    *   A) Scatter
    *   B) Bubble Chart
    *   C) Bar
    *   D) Line
    *   **Ans: B**.

68. **You have hierarchical data (Region > Country > City). Best chart?**
    *   A) Scatter
    *   B) Treemap / Sunburst
    *   C) Line
    *   D) Histogram
    *   **Ans: B**.

69. **You want to compare 'Actual Sales' vs 'Target Sales'. Best chart?**
    *   A) Pie
    *   B) Bullet Chart
    *   C) Scatter
    *   D) Area
    *   **Ans: B**.

70. **You want to show cumulative profit over the year. Best chart?**
    *   A) Bar
    *   B) Area Chart (or Running Total Line)
    *   C) Scatter
    *   D) Pie
    *   **Ans: B**.

71. **A chart has a Y-axis starting at 50 instead of 0. This is:**
    *   A) Good practice
    *   B) Truncated Axis (Misleading)
    *   C) Necessary
    *   D) Standard
    *   **Ans: B**.

72. **Using a 3D Bar chart to show simple sales data is:**
    *   A) Recommended
    *   B) Bad practice (Chartjunk/Distortion)
    *   C) Mandatory
    *   D) Innovative
    *   **Ans: B**.

73. **If your dashboard is cluttered, you should:**
    *   A) Add more colors
    *   B) Remove non-essential elements (Simplify)
    *   C) Make it bigger
    *   D) Add music
    *   **Ans: B**.

74. **To show the flow of users through a website funnel. Best chart?**
    *   A) Line
    *   B) Funnel Chart
    *   C) Pie
    *   D) Map
    *   **Ans: B**.

75. **To show a correlation matrix. Best chart?**
    *   A) Heatmap
    *   B) Bar
    *   C) Line
    *   D) Pie
    *   **Ans: A**.

76. **Which color scheme is best for 'Profit' (Positive) vs 'Loss' (Negative)?**
    *   A) Sequential (Blue)
    *   B) Diverging (Green-Red)
    *   C) Categorical
    *   D) Black and White
    *   **Ans: B**.

77. **What is the best position for the most important KPI on a dashboard?**
    *   A) Bottom Right
    *   B) Top Left
    *   C) Center
    *   D) Hidden
    *   **Ans: B**.

78. **If you have 50 categories to compare, which chart is better?**
    *   A) Vertical Column Chart
    *   B) Horizontal Bar Chart (Scrollable)
    *   C) Pie Chart
    *   D) Line Chart
    *   **Ans: B** (Labels are easier to read).

79. **To visualize a project schedule (Tasks vs Time). Best chart?**
    *   A) Gantt Chart
    *   B) Pie Chart
    *   C) Scatter Plot
    *   D) Histogram
    *   **Ans: A**.

80. **To show the composition of a workforce by Department and Gender. Best chart?**
    *   A) Stacked Bar Chart
    *   B) Line Chart
    *   C) Scatter Plot
    *   D) Area Chart
    *   **Ans: A**.


#  SECTION 6: LAST-MINUTE REVISION SHEET (CHEAT SHEET)

##  Formulas & Metrics
*   **Data-Ink Ratio** = $\frac{\text{Data-Ink}}{\text{Total Ink}}$ (Maximize this)
*   **Lie Factor** = $\frac{\text{Effect in Graphic}}{\text{Effect in Data}}$ (Should be ~1)
*   **Profit Margin** = $\frac{\text{Total Profit}}{\text{Total Sales}} \times 100$
*   **YoY Growth** = $\frac{\text{Current Year - Previous Year}}{\text{Previous Year}} \times 100$

##  Key Definitions
*   **Preattentive Attributes:** Visual cues (Color, Size) processed instantly (<200ms).
*   **Cognitive Load:** Mental effort. Minimize Extraneous (clutter), Maximize Germane (learning).
*   **Gestalt Principles:** Proximity, Similarity, Enclosure, Continuity, Closure.
*   **Chartjunk:** Useless decoration (3D, patterns).
*   **ETL:** Extract, Transform, Load (Power Query).
*   **Star Schema:** Fact Table (Center) + Dimension Tables (Surround).
*   **DAX:** Data Analysis Expressions (Power BI Formulas).
*   **Measure:** Dynamic calculation (Aggregation).
*   **Calculated Column:** Static calculation (Row-by-row).

##  Chart Selection Guide
*   **Comparison:** Bar (Categories), Line (Time).
*   **Distribution:** Histogram (1 var), Scatter (2 vars), Boxplot (Summary).
*   **Composition:** Pie (<5 cats), Stacked Bar, Treemap.
*   **Relationship:** Scatter (2 vars), Bubble (3 vars), Heatmap.
*   **Geo:** Choropleth (Regions), Symbol Map (Points).

##  Viva Boosters (Don't Forget!)
*   **Power BI vs Tableau:** Power BI = DAX/Microsoft; Tableau = VizQL/Salesforce.
*   **Live vs Extract:** Live = Real-time; Extract = Fast Snapshot.
*   **Import vs Direct Query:** Import = Fast (RAM); Direct Query = Real-time (Source).
*   **Filter vs Slicer:** Slicer is on-canvas; Filter is in the pane.
*   **Dimension vs Measure:** Dimension = Text/Date (Blue); Measure = Number (Green).
*   **SHAP:** Explains AI models (Feature Importance).

---
** GOOD LUCK FOR YOUR EXAM! YOU ARE READY! **

