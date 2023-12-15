# Imports 
import dash
import pandas as pd 
import geopandas as gpd 
import dash_leaflet as dl 
import plotly.express as px
from dash import html, dcc
import dash_loading_spinners as dls 
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output 

# Register page 
dash.register_page(__name__, top_nav = True, name = 'Carbon Sequestration')

year_list = ['2000', '2020']


layout = html.Div([
    html.H3("Above-ground Biomass"),
    'Select Year: ',
    dcc.Dropdown(placeholder = 'Year', options = [{'label': year, 'value': year} for year in year_list],
                                id = 'year-dropdown'),                               
])