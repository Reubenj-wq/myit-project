import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Task 2.1 - Create Dash App with Title
app = dash.Dash(__name__)
app.title = "Australian Wildfire Dashboard"
app.config.suppress_callback_exceptions = True

# Load wildfire data
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv")
df['Month'] = pd.to_datetime(df['Date']).dt.month_name()
df['Year'] = pd.to_datetime(df['Date']).dt.year

# Task 2.2 - Add Dropdowns and Radio Buttons
app.layout = html.Div(children=[
    html.H1("Australian Wildfire Analysis Dashboard", style={'textAlign': 'center', 'color': '#003366', 'font-size': 30}),

    html.Div([
        html.Div([
            html.H2("Select Region:"),
            dcc.RadioItems([
                {"label": "New South Wales", "value": "NSW"},
                {"label": "Victoria", "value": "VIC"},
                {"label": "Queensland", "value": "QLD"},
                {"label": "Western Australia", "value": "WA"},
                {"label": "South Australia", "value": "SA"},
                {"label": "Tasmania", "value": "TAS"},
                {"label": "Northern Territory", "value": "NT"}
            ], value='NSW', id='region-dropdown', inline=True, className='dropdown-radio'),

            html.Div([
                html.H2('Select Year:', style={'marginTop': 20}),
                dcc.Dropdown(id='year-dropdown',
                             options=[{'label': i, 'value': i} for i in sorted(df['Year'].unique())],
                             value=2019,
                             className='dropdown-select')
            ])
        ], className='input-container'),

        # Task 2.3 - Output Divisions
        html.Div([
            html.Div([], id='plot1', style={'width': '48%', 'display': 'inline-block'}, className='output-graph'),
            html.Div([], id='plot2', style={'width': '48%', 'display': 'inline-block'}, className='output-graph')
        ], style={'marginTop': 40}, className='output-container')
    ])
])

# Task 2.4 - Callback Setup
@app.callback([
    Output('plot1', 'children'),
    Output('plot2', 'children')
],
    [Input('region-dropdown', 'value'),
     Input('year-dropdown', 'value')])

def reg_year_display(input_region, input_year):
    # Filter by region and year
    region_data = df[df['Region'] == input_region]
    y_r_data = region_data[region_data['Year'] == input_year]

    # Task 2.5 - Pie Chart: Monthly Average Estimated Fire Area
    est_data = y_r_data.groupby('Month')['Estimated_fire_area'].mean().reset_index()
    fig1 = px.pie(est_data, names='Month', values='Estimated_fire_area', 
                  title=f"{input_region} : Monthly Average Estimated Fire Area in year {input_year}")

    # Task 2.6 - Bar Chart: Average Count of Presumed Vegetation Fires
    veg_data = y_r_data.groupby('Month')['Count'].mean().reset_index()
    fig2 = px.bar(veg_data, x='Month', y='Count', 
                  title=f'{input_region} : Average Count of Pixels for Presumed Vegetation Fires in year {input_year}')

    return [dcc.Graph(figure=fig1), dcc.Graph(figure=fig2)]

if __name__ == '__main__':
    app.run_server(debug=False)
