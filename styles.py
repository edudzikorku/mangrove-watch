import dash_bootstrap_components as dbc
from dash import html


# Define CSS styles for the footer
footer_style = {
    'border': '1px solid #ccc',     # Add a border at the top
    'text-align': 'center',         # Center-align the text
    'padding': '10px',              # Add some padding for spacing
    'background-color': '#f2f2f2'   # Set a background color
}


header_styles = {
        'fontWeight': 'bold',
        'textAlign': 'center',
        'marginTop': '10px',
        'fontFamily': 'sans-serif',
        'font': 'Roboto'
        }
item_styles = {
        'fontWeight': 'bold',
        'textAlign': 'center',
        'marginTop': '10px',
        'fontFamily': 'sans-serif',
        'font': 'Roboto',
        'fontSize': '16px'
        }
spin_animation = {
    "animation": "spin 5s linear infinite",
    "textAlign": "center",
    'marginTop': '10px'
}

text_style = {
    'fontFamily': 'sans-serif',
    'font': 'Roboto',
    'fontSize': '15px',
    'textAlign': 'justify'
    }
h3_style =  {
    'fontFamily': 'sans-serif',
    'font': 'Roboto',
    
    }

spinners = html.Div(
    [
        dbc.Spinner(color="primary", type="grow"),
        dbc.Spinner(color="secondary", type="grow"),
        dbc.Spinner(color="success", type="grow"),
        dbc.Spinner(color="warning", type="grow"),
        dbc.Spinner(color="danger", type="grow"),
        dbc.Spinner(color="info", type="grow"),
        dbc.Spinner(color="light", type="grow"),
        dbc.Spinner(color="dark", type="grow"),
    ]
)