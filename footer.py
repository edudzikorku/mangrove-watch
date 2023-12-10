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
                    dbc.Col([html.A([
                        html.Img(src = "assets/hen-mpoano.png", height='30px', width='90px'),
                            ], href="https://henmpoano.org/", target='_blank')], width = 1, className = "git", id='hen-mpoano-logo'),
                   dbc.Col([html.A([
                        html.Img(src = "assets/github-seeklogo.com.svg", height='30px', width = '30px'),
                            ], href="https://github.com/edudzikorku", target='_blank')], width = 1, className = "git", id='git-logo'),
                   dbc.Col([html.A([
                        html.Img(src = "assets/earthengine.png", height='30px', width='30px'),
                            ], href="https://earthengine.google.com/", target='_blank')], className = "git", width=1), 
                   dbc.Col([html.P('© 2023 Mangrove Watcher. All rights reserved.')], width = 8, className = 'rights'),
                   dbc.Col([]),
                   dbc.Col([]),
                   dbc.Col([]),
                   dbc.Col([]),
               ]
           )