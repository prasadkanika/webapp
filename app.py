import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly import tools
import dash
from dash import dcc
from dash import html
import base64


markdown= '''\n
 
 [my meat website](https://meatweb.s3.ap-south-1.amazonaws.com/meat/index.html) \n
 [my crypto website](https://mycryptoweb.s3.ap-south-1.amazonaws.com/arsha/index.html)
 
'''

app =dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    dcc.Markdown(children=markdown)
])

if __name__=="__main__":
    app.run_server(debug=True)
