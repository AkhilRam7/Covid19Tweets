import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Assuming your dataframe is called 'df'
levels = ['Vehicles', 'Vehicle Category', 'Vehicle Subcategory']  # Levels for hierarchy
value_column = 'Sales'  # Column containing sales data

def build_hierarchical_dataframe(df, levels, value_column):
    """
    Build a hierarchy of levels for Sunburst chart.

    Levels are given starting from the bottom to the top of the hierarchy,
    ie the last level corresponds to the root.
    """
    df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value'])
    for i, level in enumerate(levels):
        df_tree = pd.DataFrame(columns=['id', 'parent', 'value'])
        dfg = df.groupby(levels[i:]).sum()
        dfg = dfg.reset_index()
        df_tree['id'] = dfg[level].copy()
        if i < len(levels) - 1:
            df_tree['parent'] = dfg[levels[i+1]].copy()
        else:
            df_tree['parent'] = 'total'
        df_tree['value'] = dfg[value_column]
        df_all_trees = df_all_trees.append(df_tree, ignore_index=True)
    total = pd.Series(dict(id='total', parent='', value=df[value_column].sum()))
    df_all_trees = df_all_trees.append(total, ignore_index=True)
    return df_all_trees

df_all_trees = build_hierarchical_dataframe(df.copy(), levels, value_column)

fig = make_subplots(1, 1, specs=[[{"type": "domain"}]])

fig.add_trace(go.Sunburst(
    labels=df_all_trees['id'],
    parents=df_all_trees['parent'],
    values=df_all_trees['value'],
    branchvalues='total',
    # Set custom widths based on a percentile range of the sales data (adjust percentile as needed)
    customdata=df_all_trees['value'].rank(pct=True).to_numpy() * 100,  
    # Use customdata to define bar width based on percentile rank
    width=df_all_trees['value'].rank(pct=True).to_numpy() * 100, 
    mincoloraxis=df_all_trees['value'].min(),  # Set minimum color based on minimum sales
    maxcoloraxis=df_all_trees['value'].max(),  # Set maximum color based on maximum sales
    colorscale='Viridis',  # Select a color scale (e.g., 'Viridis', 'Plasma')
    colorbar=dict(title='Sales'),  # Add a colorbar to display sales values
    hovertemplate='<b>%{label}</b> <br> Sales: %{value}<br> Percentile: %{customdata:.2f}%',
), 1, 1)

fig.update_layout(margin=dict(t=10, b=10, r=10, l=10))
fig.show()
