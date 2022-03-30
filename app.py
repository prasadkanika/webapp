import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly import tools
import dash
from dash import Dash, dcc, html, Input, Output
import base64


app =Dash(__name__)
server = app.server
#======================
dff = pd.read_csv("gapminderDataFiveYear.csv")
year_options = []
for year in dff['year'].unique():
    year_options.append({'label':str(year) , 'value':year})


app.layout = html.Div([
    dcc.Graph(id='graph') , 
    dcc.Dropdown(id='year-picker' , options=year_options , value=dff['year'].min())
])

@app.callback(Output('graph','figure') , [Input('year-picker' , 'value')])
#graph - id , property = graph for output and for input id is year-picker and property value
def update_figure(selected_year):
    filtered_df = dff[ dff['year']== selected_year]
    traces =[]
    for continent in filtered_df['continent'].unique():
        df_by_continents = filtered_df[filtered_df['continent']==continent]
        traces.append( go.Scatter(x=df_by_continents['gdpPercap'] , y=df_by_continents['lifeExp'] , mode='markers' , opacity=0.7 , marker={'size':15},name=continent) )
    
    return {'data':traces , 'layout':go.Layout(title='My plot' , xaxis={'title':'GDP per Capita','type':'log'} , yaxis={'title':'Life Expectancy'})}

#===================================

if __name__=="__main__":
    app.run_server(debug=True)
