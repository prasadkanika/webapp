import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly import tools
import dash
import dash_core_components as dcc
import dash_html_components as html
import base64

wheels = pd.read_csv("wheels.csv")

def encode_img(img):
    encoded = base64.b64encode(open(img,'rb').read())
    return f"data:image/png;base64,{encoded.decode()}"

options = [{'label':k , 'value':k} for k in wheels['wheels'].unique()]
options1 = [{'label':k , 'value':k} for k in wheels['color'].unique()]

app.layout = html.Div([
    dcc.RadioItems(id='wheels' , options=options , value=1) ,
    html.Div(id='wheelsop'),
    html.Hr() , #horizontal row line
    dcc.RadioItems(id='colors' , options=options1 , value='blue') ,
    html.Div(id='colorsop'),
    html.Img(id='img' , src='children' , height=300)
],style={'padding':'15px','font-size':'18px' ,'font-family':'helvetica'})

@app.callback(Output('wheelsop','children') , [Input('wheels','value')])
def callback_a(wheels_val):
    return f'you choose {wheels_val}'

@app.callback(Output('colorsop','children') , [Input('colors','value')])
def callback_b(colors_val):
    return f"you choose {colors_val}"

@app.callback(Output('img','src') , [ Input('wheels','value') , Input('colors','value')])
def image(wheel,color):
    path='/Users/guruprasadkanika/Downloads/datascience/Plotly-Dashboards-with-Dash-master/Data/Images/'
    img_df = wheels[ (wheels['wheels']==wheel) & (wheels['color']==color) ]
    return encode_img(path+ img_df['image'].values[0] )
    

if __name__=="__main__":
    app.run_server()
