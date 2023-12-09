import dash
import time
# Import packages
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dash_table, dcc, callback
import dash_bootstrap_components as dbc
from dash_spinner import DashSpinner as spinner
from dash.dependencies import Input, Output, State
# import your_raster_processing_module as rast_proc 
from styles import (
    h3_style,
    footer_style, 
    header_styles,item_styles,
    spin_animation, 
    spinners,
    text_style)
mapbox_token = 'pk.eyJ1IjoiZWR1ZHppIiwiYSI6ImNsbDRsZWp3ZDA3ZWIzZW1rdXFrbW5obmcifQ.B-oC1_9g6aKBQc6delbiiA'
# Initialize app
app = Dash(__name__, external_stylesheets = [dbc.themes.DARKLY])
app._favicon = 'assets/favicon.ico'
# Define the layout of the app
app.layout = html.Div([
    html.Div([]),
    dbc.Nav([
        dbc.NavbarBrand(
            children = dbc.Col(html.Img(src = 'assets/globe.png', height= "50px", style = {**spin_animation})),
        ),
        html.H3("Mangrove Watcher", style = header_styles, className = 'nav-items', id = 'watcher'),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.NavItem(style = {'marginRight':'auto'}),
        dbc.NavItem(dbc.NavLink("Home", active = True, href = "/path", style = item_styles, className = 'nav-items')),
        dbc.NavItem(dbc.NavLink("Above-Ground Biomass", active = True, href = "/path", style = item_styles, className = 'nav-items')),
        dbc.NavItem(dbc.NavLink("Carbon Stock", href="/path", style = item_styles, className = 'nav-items')),
        dbc.NavItem(dbc.NavLink("Carbon Sequestration", href="/path", style = item_styles, className = 'nav-items')),
        dbc.DropdownMenu(
            [dbc.DropdownMenuItem('2000'), dbc.DropdownMenuItem('2020')],
            label = 'Year',
            nav = True,
            style = item_styles, 
            
        )
            ], style = {
        'backgroundColor': '#023047'
    }),
    html.Div(children = [

    ]),
    dbc.Spinner(html.Div(id = "loading-output",
                         children = [
            dcc.Graph(
                id = 'base-map',
                figure = {}
            )    
        ]), size = '30', color = "success", type = 'border', fullscreen = True
),
    html.Br(),
    # Insert maps highlighting selected areas of interest
    html.H3("Project Description", style = h3_style),
    dbc.Row([
            # Description of the project
    dbc.Col(html.P(
          """
           Mangroves, vital coastal ecosystems teeming with biodiversity, are facing unprecedented degradation, posing a 
           significant threat to the well-being of both the environment and the communities dependent on them. Human 
           activities, ranging from urbanization and aquaculture expansion to climate change-induced phenomena, are accelerating 
           mangrove loss, compromising the ecological integrity of these critical zones. As mangroves decline, the repercussions 
           extend beyond environmental concerns to encompass socio-economic aspects, affecting the well-being of coastal populations
           that rely on these ecosystems for sustenance, livelihoods, and protection against natural hazards. Urgent attention is 
           required to address this multifaceted challenge, safeguarding not only the biodiversity and resilience of mangrove 
           ecosystems but also the well-being of the communities intricately linked to their existence.""",
           style = text_style
           )),

    dbc.Col([html.P("""
                Remote sensing, coupled with machine learning algorithms, has emerged as a potent tool in estimating 
                above-ground biomass (AGB) with unprecedented 
                accuracy. Numerous studies have explored this intersection, leveraging datasets from platforms like Landsat and Sentinel-2, 
                and employing algorithms such as Random Forest (RF), Extreme Gradient Boosting (XGBoost), and Support Vector Regression (SVR)""", 
                style = text_style
           ),
           html.P("""
                  This project employs Remote Sensing and Machine Learning to address urgent mangrove degradation. Focusing on 
                  AGB, it integrates advanced technologies like Landsat imagery and SAR data with field inventory. The aim is 
                  to provide accurate insights into mangrove health, guiding targeted interventions and contributing to sustainable 
                  resource management. Utilizing machine learning, specifically the Random Forest model from Google Earth Engine, the 
                  project accurately estimates AGB, carbon stock, and carbon sequestration potential of mangroves. 
                  This information is crucial for identifying and addressing degradation, ultimately safeguarding the well-being 
                  of communities reliant on these essential coastal ecosystems.""",
                  style = text_style
                  )]),
            

    ]),
    dcc.Location(id = 'location'),
    dcc.Link(href = '/path/search?one=1&two=2', children = 'Go to search page'),
    dcc.Link(href = 'path/?hello=HELLO#hash_string', children = 'Go to page with hash'),

    # Link to explore the map
    html.A("Explore the Map", href="#", target="_blank")

    ])

@app.callback(
    Output("base-map", "figure"), 
    Input("loading-output", 'n_clicks')
)
def load_output(n):
    if n:
        time.sleep(1)
        return f"Output loaded {n} times"
    fig = {'data':[
                    go.Scattermapbox(
                        )
                    ],
                    'layout': go.Layout(
                        mapbox=dict(
                            accesstoken = mapbox_token,
                            center = dict(
                                lat = 4.9606589, 
                                lon = -1.7952544 
                            ),
                            style = 'dark',
                            zoom = 8  
                        ),
                        margin = dict(l = 0, r = 0, t = 0, b = 0)
                    )}
    return fig
@app.callback(
    Output('page-content', 'children'),
    Input('location', 'pathname'))

def multiPage():
    pass
if __name__ == '__main__':
    app.run_server(debug=True)
