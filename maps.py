import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go

gdf = gpd.read_file("data/geodata/agb_2000.shp")
gdf = gdf.to_crs(4326)
gdf = gdf.rename(columns = {'grid_code':'biomass'})

mapbox_token = 'pk.eyJ1IjoiZWR1ZHppIiwiYSI6ImNsbDRsZWp3ZDA3ZWIzZW1rdXFrbW5obmcifQ.B-oC1_9g6aKBQc6delbiiA'
# Calculate min and max values
min_value = gdf['biomass'].min()
max_value = gdf['biomass'].max()
# Create a scattermapbox trace
scatter_mapbox_trace = go.Scattermapbox(
    mode = "markers",
    lon = gdf.geometry.x,
    lat = gdf.geometry.y,
    marker = dict(size = 3, 
                  color = gdf['biomass'], 
                  colorscale = "Magma", 
                  colorbar = dict(title = "Biomass",
                                #    tickvals=[min_value, (min_value + max_value) / 2, max_value],  # Set tick values
                                #    ticktext=[f'{min_value:.2f}', f'{(min_value + max_value) / 2:.2f}', f'{max_value:.2f}'],
                                #    tickmode='array',
                                #    coloraxis='coloraxis'
                                  )),
    text = gdf['biomass'].astype(str),
)

# Define the layout for the map
layout = go.Layout(
    mapbox = dict(
        style = "dark", 
        center = dict(lon = 0.843645, lat = 5.814379),
        zoom = 12,
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
biomass_fig.update_layout(coloraxis=dict(colorbar=dict(thickness=8, len=0.50, x=0.5, y=0.15)))

# Show the figure
# biomass_fig.show()
