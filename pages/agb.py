# Imports 
import time
import dash
import pandas as pd 
import geopandas as gpd 
import dash_leaflet as dl 
import plotly.express as px
import plotly.graph_objects as go
import dash_loading_spinners as dls 
from dash import html, dcc, callback
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State 

gdf = gpd.read_file("data/geodata/agb_2000.shp")
gdf = gdf.to_crs(4326)
gdf = gdf.rename(columns = {'grid_code':'biomass'})

mapbox_token = 'pk.eyJ1IjoiZWR1ZHppIiwiYSI6ImNsbDRsZWp3ZDA3ZWIzZW1rdXFrbW5obmcifQ.B-oC1_9g6aKBQc6delbiiA'

# Register page 
dash.register_page(__name__, top_nav = True, name = 'Above-ground Biomass')

year_list = ['2000', '2020']

def initial_fig():
    fig = go.Figure()
    fig.layout.paper_bgcolor = '#2C3E50'
    fig.layout.plot_bgcolor = '#2C3E50'
    return fig

layout = html.Div([
    dcc.Dropdown(placeholder = 'Select Year', options = [{'label': year, 'value': year} for year in year_list],
                                id = 'year-dropdown', className = 'dropdown-list', style = {'width': '400px'}),
    dbc.Row(
        [
            dbc.Col([dbc.Spinner
                (dcc.Graph(id = 'biomass-map', figure = initial_fig(), config = {'displayModeBar': False}),
                 color = 'success', type = 'border', fullscreen = True, spinnerClassName = 'my-spinner', size = 'sm'),
                 ], width = 12)
        ]
    )
], className = 'abg-map')

@callback(Output('biomass-map', 'figure'),
          Input('year-dropdown', 'value'),
          )
def displayMap(selected_year):
    if selected_year is None:
        raise PreventUpdate
    elif selected_year == '2000':

        # Create a scattermapbox trace
        scatter_mapbox_trace = go.Scattermapbox(
            mode = "markers",
            lon = gdf.geometry.x,
            lat = gdf.geometry.y,
            marker = dict(size = 3, 
                        color = gdf['biomass'], 
                        colorscale = "Magma", 
                        colorbar = dict(title = "Biomass")),
            text = gdf['biomass'].astype(str),
        )

        # Define the layout for the map
        layout = go.Layout(
            mapbox = dict(
                style = "dark", 
                center = dict(lon = 0.843645, lat = 5.814379),
                zoom = 8,
                bearing = 0,
                pitch = 0,
                accesstoken = mapbox_token,  
            ),
        )

        # Create the figure
        biomass_fig = go.Figure(data=[scatter_mapbox_trace], layout = layout)


        # Update figure display
        biomass_fig.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0})

        # Update map projection 
        biomass_fig.layout.geo.projection.type = 'mercator'

        # Update color axis size
        biomass_fig.update_layout(coloraxis = dict(colorbar = dict(thickness = 8, len = 0.50, x = 0.5, y = 0.15)))

        return biomass_fig

    elif selected_year == '2020':
        return initial_fig()
