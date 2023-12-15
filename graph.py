# imports 

import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

predictors_2000 = 'data/predictors_2000.csv'
predictors_2020 = 'data/predictors_2020.csv'

# Load data
variable_importance_2000 = pd.read_csv(predictors_2000)
variable_importance_2020 = pd.read_csv(predictors_2020)

# Create function to remove irrelevant columns from data
def removeUnwantedColumns(df1, df2):
  cols_to_remove = ['system:index', '.geo']
  df1 = df1.drop(columns = cols_to_remove)
  df2 = df2.drop(columns = cols_to_remove)
  return df1, df2

variable_importance_2000, variable_importance_2020 = removeUnwantedColumns(variable_importance_2000, variable_importance_2020)

# Create function to melt dataframes
def meltDataframe(df1, df2):
  # Reshape the DataFrame using melt

  # 2000
  variable_importance_2000_melt = pd.melt(df1, var_name = 'Feature', value_name = 'Importance')

  # 2020
  variable_importance_2020_melt = pd.melt(df2, var_name = 'Feature', value_name = 'Importance')

  # Sort the DataFrame by feature importance
  # 2000
  variable_importance_2000_sorted = variable_importance_2000_melt.sort_values(by = 'Importance', ascending = True)
  # 2020
  variable_importance_2020_sorted = variable_importance_2020_melt.sort_values(by = 'Importance', ascending = True)

  # Get the length of the dataframe
  # 2000
  n_items_2000 = len(variable_importance_2000_sorted['Feature'])

  # 2020
  n_items_2020 = len(variable_importance_2020_sorted['Feature'])

  return variable_importance_2000_sorted, variable_importance_2020_sorted, n_items_2000, n_items_2020

variable_importance_2000_sorted, variable_importance_2020_sorted, n_items_2000, n_items_2020 = meltDataframe(variable_importance_2000, variable_importance_2020)

# Create subplots using make_subplots
feature_plots = make_subplots(rows = 1,
                    cols = 3,
                    subplot_titles = ['Random Forest Feature Importance (2000)', ' ', 'Random Forest Feature Importance (2020)'],
                    column_widths = [0.5, 0.05, 0.5]
                    )

# Plot for 2000
fig1 = px.bar(variable_importance_2000_sorted,
              x = 'Importance',
              y = 'Feature',
              orientation = 'h',
              labels = {'Feature': 'Feature Importance'},
              color_discrete_sequence = ["#40916c"],
              height = 100 + (20 * n_items_2000), 
              )
# Update x-axis and y-axis title font size
fig1.update_xaxes(title_font = {'size': 20})
fig1.update_yaxes(title_font = {'size': 20})
# Update font
fig1.layout.font.family = 'Montserrat'

# Plot for 2020
fig2 = px.bar(variable_importance_2020_sorted,
              x = 'Importance',
              y = 'Feature',
              orientation = 'h',
              labels = {'Feature': 'Feature Importance'},
              color_discrete_sequence = ["#40916c"],
              height = 100 + (20 * n_items_2020),
              )

# Update font
fig2.layout.font.family = 'Montserrat'
# Update x-axis and y-axis title font size
fig2.update_xaxes(title_font = {'size': 20})
fig2.update_yaxes(title_font = {'size': 20})

# Add traces to subplots
feature_plots.add_trace(fig1.data[0], row = 1, col = 1)
feature_plots.add_trace(fig2.data[0], row = 1, col = 3)

# Update layout
feature_plots.update_layout(showlegend = False, 
                            paper_bgcolor = '#4a4e69',
                            font = dict(
                                        family='Montserrat', 
                                        size=12,
                                        color='#ffffff' 
                                        ))

# Display the plot
# feature_plots.show()