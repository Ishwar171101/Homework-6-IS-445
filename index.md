---
layout: default
title: Building Inventory Visualizations
---

# Building Inventory Visualizations

## Visualization 1: Bar Chart - Top 20 Agencies by Total Square Footage
This bar chart shows the top 20 agencies with the largest total square footage.


Description:
This bar chart visualizes the top 20 agencies with the largest total square footage of buildings. Each bar represents an agency, and the length of the bar corresponds to the total square footage aggregated across all buildings managed by the agency.

Design Choices:

The x-axis encodes total square footage as a quantitative variable, while the y-axis encodes agency names as categorical variables.
A dark blue color scheme was chosen to maintain simplicity and focus on the bar lengths, which are the most important aspect of the visualization.
Text labels were added to display the exact square footage for each bar, formatted with commas for clarity.
Data Transformations:
The dataset was filtered to include the top 5000 rows by square footage. Data was then grouped by agency, summing the square footage to determine each agency's total.

<iframe src="bar.html" width="800" height="600" frameborder="0"></iframe>

---

## Visualization 2: Line Chart - Square Footage Over Time
This interactive line chart shows how square footage changes over time for selected agencies.
Plot 2: Interactive Line Chart - Square Footage Over Time
Description:
This line chart shows the total square footage of buildings constructed over time for the selected agency. Users can interactively select an agency from a dropdown menu to filter the visualization.

Design Choices:

The x-axis encodes the year constructed as a quantitative variable, ensuring years are displayed without commas.
The y-axis encodes total square footage as a quantitative variable.
Agencies are color-coded to distinguish data points, but only one agency is displayed at a time for clarity.
Interactive selection via a dropdown menu allows users to explore specific agencies of interest.
Data Transformations:
The dataset was filtered to include only the top 20 agencies by square footage. Data was grouped by the year of construction and agency to calculate yearly totals.


Interactivity Discussion:
The dropdown menu enables users to focus on one agency at a time, making it easier to identify trends in square footage over time. This interactivity adds value by reducing clutter and improving the interpretability of the visualization.


<iframe src="line.html" width="800" height="600" frameborder="0"></iframe>


