
# Import packages
import dash
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash_spinner import DashSpinner as spinner
from dash.dependencies import Input, Output, State
from dash import Dash, html, dash_table, dcc, callback

from graph import feature_plots
from footer import footer
from styles import (
    h3_style,
    footer_style, 
    header_styles,item_styles,
    spin_animation, 
    spinners,
    text_style)

from maps import biomass_fig

style_list = [dbc.themes.DARKLY]

spinner =  dbc.Spinner(
    html.Div(id = "loading-output",
             children = [
                 dcc.Graph(
                     id = 'base-map',
                     figure = biomass_fig,
                     config = {'displayModeBar': False}
                            )    
                    ]), size = '30', color = "success", type = 'border', fullscreen = True
            ),
# Instantiate app
app = dash.Dash(__name__, external_stylesheets = style_list, assets_folder='assets')
app._favicon = 'assets/tracking.ico'
server = app.server
# Define the layout of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh = False),   
        dbc.NavbarSimple(
                         brand = dbc.Row([
                             dbc.Col(html.Img(src='assets/globe.png', height="50px", className = 'logo')),
                             dbc.Col(html.H3("Mangrove Watcher", className = 'watcher')),
                                    ]),     
            children = [  
                dbc.NavItem(dbc.NavLink("Home", href="/", className = 'local-nav-items', style = {'color':'white', 'fontFamily':
                                                                                     'Roboto, sans-serif', 'fontSize':'16px'})),
                dbc.NavItem(dbc.NavLink("Above-Ground Biomass", href = "/page-1", className = 'local-nav-items', style = {'color':'white', 'fontFamily':
                                                                                     'Roboto, sans-serif', 'fontSize':'16px'})),
                dbc.NavItem(dbc.NavLink("Carbon Stock", href = "/page-2", className = 'local-nav-items', style = {'color':'white', 'fontFamily':
                                                                                     'Roboto, sans-serif', 'fontSize':'16px'})),
                dbc.NavItem(dbc.NavLink("Carbon Sequestration", href = "/page-3", className = 'local-nav-items', style = {'color':'white', 'fontFamily':
                                                                                     'Roboto, sans-serif', 'fontSize':'16px'})),
                dbc.NavItem(dbc.DropdownMenu(
                                [dbc.DropdownMenuItem('2000'), dbc.DropdownMenuItem('2020')],
                                label = 'Year',
                                nav = True,
                                className = 'dropdown-item-year'
                            )
),
        ],
        brand_href = "/",
        color = "#001d3d",
        # dark = True,
        # expand = 'lg',
    ),
    html.Div(id='page-content')
])

# Define the callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/page-1':
        return html.Div([
            html.Div(spinner),
            html.Footer([footer], className = 'footers')
        ])
    elif pathname == '/page-2':
        return html.Div([
            html.Div(spinner),
            html.Footer([footer], className = 'footers')
        ])
    elif pathname == '/page-3':
        return html.Div([
            html.Div(spinner),
            html.Footer([footer], className = 'footers')
        ]),
    else:
        return html.Div([
            # html.Img(src='assets/mangrove-3.jpg', height='500px'),
            dbc.Row(className = 'home-rows', children = [
                dbc.Col([            
                       html.Div("""
                        Mangroves, vital coastal ecosystems teeming with biodiversity, are facing unprecedented degradation, posing a 
                        significant threat to the well-being of both the environment and the communities dependent on them. Human 
                        activities, ranging from urbanization and aquaculture expansion to climate change-induced phenomena, are accelerating 
                        mangrove loss, compromising the ecological integrity of these critical zones. As mangroves decline, the repercussions 
                        extend beyond environmental concerns to encompass socio-economic aspects, affecting the well-being of coastal populations
                        that rely on these ecosystems for sustenance, livelihoods, and protection against natural hazards. Urgent attention is 
                        required to address this multifaceted challenge, safeguarding not only the biodiversity and resilience of mangrove 
                        ecosystems but also the well-being of the communities intricately linked to their existence.""",
                     style = text_style
                    ),   
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.A("Figure 1: Contribution of features to Above-ground biomass prediction", className = 'figure-desc'),
                    ]
                    ),
                    dbc.Col(children =
                                    [
                                        html.Div("""
                                            Remote sensing, coupled with machine learning algorithms, has emerged as a potent tool in estimating 
                                            above-ground biomass (AGB) with unprecedented 
                                            accuracy. Numerous studies have explored this intersection, leveraging datasets from platforms like Landsat and Sentinel-2, 
                                            and employing algorithms such as Random Forest (RF), Extreme Gradient Boosting (XGBoost), and Support Vector Regression (SVR).""", 
                                            style = text_style),
                                        html.Div("""
                                            This project employs Remote Sensing and Machine Learning to address urgent mangrove degradation. Focusing on 
                                            AGB, it integrates advanced technologies like Landsat imagery and SAR data with field inventory. The aim is 
                                            to provide accurate insights into mangrove health, guiding targeted interventions and contributing to sustainable 
                                            resource management. Utilizing machine learning, specifically the Random Forest model from Google Earth Engine, the 
                                            project accurately estimates AGB, carbon stock, and carbon sequestration potential of mangroves. 
                                            This information is crucial for identifying and addressing degradation, ultimately safeguarding the well-being 
                                            of communities reliant on these essential coastal ecosystems.""",
                                            style = text_style),
                                        
                                            
                                    ]
                        )        
           ]),
           dcc.Graph(id = 'mangrove-graph', className = 'mangrove-graph-component', figure = feature_plots),
           html.Footer([footer], className = 'footers')
        ])

if __name__ == '__main__':
    app.run()
