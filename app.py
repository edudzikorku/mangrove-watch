# Imports 
import dash
import pandas as pd 
import geopandas as gpd 
import dash_leaflet as dl 
import plotly.express as px
from dash import Dash, html, dcc
import dash_loading_spinners as dls 
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output 

# Self-defined 
from graph import feature_plots
from maps import biomass_fig
meta_tags = [
            {"name": "viewport",
            "content": "width=device-width, initial-scale=1"}
    ]

# Set up stylesheets 
static_css = 'assets/style.css'
stylesheets = [static_css, dbc.themes.DARKLY, dbc.icons.FONT_AWESOME]

# Create list of years 
year_list = ['2000', '2020']

# Instantiate app 
app = Dash(__name__, meta_tags = meta_tags, external_stylesheets = stylesheets, use_pages = True, pages_folder = 'pages')

# Set up favicon 
app._favicon = 'assets/tracking.ico'

server = app.server 

footer = html.Footer(
    className = "footer-distributed",
    children = [
        html.Div(
            className = "footer-left",
            children = [
                html.H3("Hɛn Mpoano"),
                html.P(
                    className = "footer-links",
                    children = [
                        html.A("Home", href = "https://henmpoano.org/", className="link-1", target = '_blank'),
                        html.A("About", href = "https://henmpoano.org/what-we-do/", target = '_blank'),
                        html.A("Projects", href = "https://henmpoano.org/projects/", target = '_blank'),
                        html.A("News", href = "https://henmpoano.org/publications/", target = '_blank'),
                        html.A("Contact", href = "https://henmpoano.org/contact-2/", target = '_blank'),
                    ],
                ),
                html.P("Hɛn Mpoano © 2023", className = "footer-company-name"),
                html.Br(),
                html.P(className = 'source-code', 
                      children = [
                          html.Div(
                              children = [
                                  html.P(children = [
                                      html.Span("Source Code:")
                                  ]),
                                  html.A(html.I(className = "fa-brands fa-github", id = 'git-icon'), href="https://github.com/edudzikorku/mangrove-watch.git", target = '_blank'),
                              ],
                          ), 
                          ])
            ],
        ),
        html.Div(
            className = "footer-center",
            children = [
                html.Div(
                    children = [
                        html.I(className = "fas fa-location"),
                        html.P(
                            children = [
                                html.Span("38 J. Cross Cole Street"),
                                "Takoradi, Western Region, Ghana",
                            ]
                        ),
                    ]
                ),
                html.Div(
                    children = [
                        html.I(className = "fa-solid fa-phone"),
                        html.P("031 229 3869"),
                    ]
                ),
                html.Div(
                    children = [
                        html.I(className = "fa-solid fa-envelope"),
                        html.P(
                            children = [
                                html.A(
                                    "info@henmpoano.org",
                                    href="mailto:info@henmpoano.org",
                                )
                            ]
                        ),
                    ]
                ),
            ],
        ),
        html.Div(
            className = "footer-right",
            children = [
                html.P(
                    className = "footer-company-about",
                    children = [
                        html.Span("About Hɛn Mpoano"),
                        html.P("Hen Mpoano is a not-for-profit organization legally registered in Ghana since 2013 and based in Takoradi", className = 'about-hm'),
                        
                    ],
                ),
                html.A('Read More', href = "https://henmpoano.org/"),
                html.Div(
                    className = "footer-icons",
                    children = [
                        html.A(html.I(className = "fa-brands fa-facebook"), href="https://www.facebook.com/HenMpoano/", target = '_blank'),
                        html.A(html.I(className = "fa-brands fa-twitter"), href="https://twitter.com/henmpoano", target = '_blank'),
                        html.A(html.I(className = "fa-brands fa-youtube"), href="https://www.youtube.com/channel/UCOpHzD15In9hfz5rAwhY2Bw", target = '_blank'),
                        html.A(html.I(className = "fa-brands fa-linkedin"), href="https://www.linkedin.com/company/hen-mpoano/about/", target = '_blank'),
                    ],
                ),
            ],
        ),
    ],
)



# Define navbar 
navbar = dbc.NavbarSimple(
    dbc.Nav(
        
        [
            dbc.NavLink(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page.get("top_nav")
        ],
    ),
   brand = dbc.Row([
       dbc.Col(html.Img(src = 'assets/globe.png', height = "50px", className = 'logo')),
       dbc.Col(html.H3("Mangrove Watcher", className = 'watcher')),      
                                    ]), 
    color = "#001d3d",
    dark = True,
    className = "mb-2",
)

# Define the layout of the app
app.layout = html.Div([
    navbar, dash.page_container, footer
])

if __name__ == '__main__':
    app.run()
