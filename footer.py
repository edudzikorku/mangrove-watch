import dash
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash_spinner import DashSpinner as spinner
from dash.dependencies import Input, Output, State
from dash import Dash, html, dash_table, dcc, callback

footer = dbc.Row(
               children = [
                    dbc.Col(html.Div([html.A([
                        html.Img(src = "assets/hen-mpoano.png", height='30px', width='90px'),
                            ], href="https://henmpoano.org/", target='_blank')], id='hen-mpoano-logo'), className = "d-flex align-items-stretch git"),
                   dbc.Col(html.Div([html.A([
                        html.Img(src = "assets/github-seeklogo.com.svg", height='30px', width = '30px'),
                            ], href="https://github.com/edudzikorku", target='_blank')], id='git-logo'), className = "d-flex align-items-stretch git"),
                   dbc.Col(html.Div([html.A([
                        html.Img(src = "assets/earthengine.png", height='30px', width='30px'),
                            ], href="https://earthengine.google.com/", target='_blank', id = 'earth-engine-logo')]), className = "d-flex align-items-stretch git"), 
                   dbc.Col(html.Div([html.P('© 2023 Mangrove Watcher. All rights reserved.')]), className = "d-flex justify-content-around"),
                #    dbc.Col([]),
                #    dbc.Col([]),
                #    dbc.Col([]),
                #    dbc.Col([]),
               ]
           )