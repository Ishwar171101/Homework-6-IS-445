#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[6]:


import pandas as pd
import altair as alt

data_url = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv"
data = pd.read_csv(data_url)

# Cleaning the dataset
data_cleaned = data.dropna(subset=['Agency Name', 'Square Footage', 'Year Constructed'])
data_cleaned['Square Footage'] = pd.to_numeric(data_cleaned['Square Footage'], errors='coerce')


data_sorted = data_cleaned.sort_values(by='Square Footage', ascending=False).iloc[:5000, :]

# Group by Agency Name to calculate total square footage
agency_square_footage = data_sorted.groupby('Agency Name')['Square Footage'].sum().reset_index()

# Select top 20 agencies
top_20_agencies = agency_square_footage.sort_values(by='Square Footage', ascending=False).iloc[:20]

# === Bar Chart for Top 20 Agencies 
bar_chart = alt.Chart(top_20_agencies).mark_bar(color='darkblue').encode(
    x=alt.X('Square Footage:Q', title='Total Square Footage'),
    y=alt.Y('Agency Name:N', title='Agency', sort=top_20_agencies['Agency Name'].tolist())  # Explicit sorting
).properties(
    title="Top 20 Agencies by Total Square Footage (Descending Order)",
    width=700,
    height=1200
)
# Add text labels for bar chart
bar_labels = alt.Chart(top_20_agencies).mark_text(
    align='left',
    baseline='middle',
    dx=5,
    fontSize=10
).encode(
    x=alt.X('Square Footage:Q'),
    y=alt.Y('Agency Name:N'),
    text=alt.Text('Square Footage:Q', format=',')  # Comma formatting for square footage
)

bar_chart_with_labels = bar_chart + bar_labels

# === Line Chart for Yearly Trends

data_top_20 = data_sorted[data_sorted['Agency Name'].isin(top_20_agencies['Agency Name'])]
data_top_20 = data_top_20[data_top_20['Year Constructed'] >= 0]

# Group by Year Constructed and Agency Name to calculate square footage
data_line = data_top_20.groupby(['Year Constructed', 'Agency Name'])['Square Footage'].sum().reset_index()


agency_selection = alt.selection_single(
    fields=['Agency Name'], 
    bind=alt.binding_select(options=top_20_agencies['Agency Name'].tolist(), name='Select Agency: ')
)

# Line chart
line_chart = alt.Chart(data_line).mark_line(point=True).encode(
    x=alt.X('Year Constructed:Q', title='Year Built'),  # Ensure no commas in years
    y=alt.Y('Square Footage:Q', title='Total Square Footage'),
    color=alt.Color('Agency Name:N', legend=None),
    tooltip=['Year Constructed:Q', 'Square Footage:Q', 'Agency Name:N']
).add_selection(
    agency_selection
).transform_filter(
    agency_selection
).properties(
    title="Total Square Footage Over Time (Filtered by Agency)",
    width=700,
    height=400
)

# Display visualizations
print("Visualization 1: Bar Chart")
bar_chart_with_labels.display()

print("\nVisualization 2: Line Chart")
line_chart.display()

line_chart.save("/Users/Hp/Downloads/line.html")
bar_chart.save("/Users/Hp/Downloads/bar.html")


# In[ ]:




