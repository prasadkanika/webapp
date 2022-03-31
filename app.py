import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly import tools
import dash
from dash import Dash, dcc, html, Input, Output , State
import base64
from datetime import datetime
from datetime import timedelta


app =Dash(__name__)
server = app.server
#======================

df = pd.read_csv("Select.csv")
df.set_index(keys='Issuer Name', inplace=True)

options=[]
for s in df.index:
    di={}
    di['label']=df.loc[s].get(0)
    di['value']=s
    options.append(di)
options


    
mi= datetime.today() - timedelta(days=730)
ma= datetime.today() 
sd,ed=str(datetime.today()-timedelta(days=60))[:10] , str(datetime.today())[:10]
    
app.layout = html.Div([
    
    html.H1("Stock ticker") ,
    html.Div([
         html.H3("Enter stock symbol" , style={'paddingRight':'30px'}) ,
    dcc.Dropdown(id='stock_name' , options=options, value=['TITAN'],multi=True )]
        , style={'display':'inline-block' , 'verticalAlign':'top','width':"30%"}) ,
    
    
     html.Div([
         html.H3("Select date range" ) ,
         
    dcc.DatePickerRange(id='date_range' ,min_date_allowed =mi ,max_date_allowed = ma ,start_date =sd, end_date=ed)
        
    ], style={'display':'inline-block'}) ,
    
    html.Div([
        html.Button(id='submit_btn' , n_clicks=0 , children='Submit' , style={'fontSize':24 , 'marginLeft':"30px"})
    ], style={'display':'inline-block'}) ,
    
    dcc.Graph(id='graph' , figure={
        'data':[{'x':[1,2] , 'y':[3,1]}] , 'layout':{'title':'default title'}
    }),
    
])

@app.callback(Output('graph','figure'),[Input('submit_btn','n_clicks')],[State('stock_name','value') ,
                                        State('date_range','start_date') , State('date_range','end_date')])

def update_graph(n_clicks , stock_name , start_date , end_date):
#    start_date = str(mi)[:10]
#    end_date =str(ma)[:10]
    traces=[]
    for k in stock_name:
        df = web.DataReader(name=k+".BO"  , data_source='yahoo', start = start_date ,end = end_date)
        traces.append({'x':df.index , 'y':df['Close'], 'name':k})
    
    fig = {'data':traces , 'layout':{'title': stock_name }}
    return fig

#===================================

if __name__=="__main__":
    app.run_server(debug=True)
