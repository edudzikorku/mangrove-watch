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

from graph import feature_plots
# Register page 
dash.register_page(__name__, path = '/', top_nav = True)

layout = html.Div([
    dbc.Row(className = 'home-rows', children = [
        dbc.Col([
                dcc.Markdown("""
                        Mangroves, vital coastal ecosystems teeming with biodiversity, are facing unprecedented degradation, posing a 
                        significant threat to the well-being of both the environment and the communities dependent on them. Human 
                        activities, ranging from urbanization and aquaculture expansion to climate change-induced phenomena, are accelerating 
                        mangrove loss, compromising the ecological integrity of these critical zones. As mangroves decline, the repercussions 
                        extend beyond environmental concerns to encompass socio-economic aspects, affecting the well-being of coastal populations
                        that rely on these ecosystems for sustenance, livelihoods, and protection against natural hazards. Urgent attention is 
                        required to address this multifaceted challenge, safeguarding not only the biodiversity and resilience of mangrove 
                        ecosystems but also the well-being of the communities intricately linked to their existence""",
                    )
                ]),
        dbc.Col([
            dcc.Markdown(
                    dangerously_allow_html=True,
                    children = """ 
                            Remote sensing, coupled with machine learning algorithms, has emerged as a potent tool in estimating 
                            above-ground biomass (AGB) with unprecedented accuracy. Numerous studies have explored this intersection, leveraging datasets from platforms like Landsat and Sentinel-2, 
                            and employing algorithms such as 
                            [Random Forest (RF)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html), 
                            [Extreme Gradient Boosting (XGBoost)](https://xgboost.readthedocs.io/en/stable/index.html), 
                            and [Support Vector Regression (SVR)](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html).
                                    """),
            dcc.Markdown(
                    children = """This project employs Remote Sensing and Machine Learning to address urgent mangrove degradation. Focusing on 
                                AGB, it integrates advanced technologies like [Landsat](https://landsat.gsfc.nasa.gov/) imagery and 
                                [SAR](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/overview) data with field inventory. The aim is 
                                to provide accurate insights into mangrove health, guiding targeted interventions and contributing to sustainable 
                                resource management. Utilizing machine learning, specifically the Random Forest model from 
                                [Google Earth Engine](https://earthengine.google.com/), the 
                                project accurately estimates AGB, carbon stock, and carbon sequestration potential of mangroves. 
                                This information is crucial for identifying and addressing degradation, ultimately safeguarding the well-being 
                                of communities reliant on these essential coastal ecosystems.""")
])
]),

dcc.Graph(id = 'mangrove-graph', className = 'mangrove-graph-component', figure = feature_plots),
])