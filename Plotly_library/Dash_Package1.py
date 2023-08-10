import pandas as pd
from dash import Dash, dcc, html,Output,Input
import plotly.express as px
import plotly.graph_objects as go

app=Dash(__name__)
df = pd.read_csv("data.csv")
df=df.groupby(["Observation Date","Series Display Name"])[["Observation Value"]].mean()
df.reset_index(inplace=True)
print(df[:5])


app.layout=html.Div([
    html.H1("Web Application Dashboard with Dash",style={'text-align':'center'}),
    dcc.Dropdown(id="my_dropdown",
                 options=[
                     {"label":"Observation Date","value":"Observation Date"},
                     {"label":"Series Display Name","value":"Series Display Name"}],
                 multi=False,
                 value=2015,
                 style={'width':"40%"}
                 ),
    html.Div(id='output_container',children=[]),
    html.Br(),
    dcc.Graph(id='my_dropdown',figure={})
])
@app.callback(
    [Output(component_id='Series Display Name', component_property='children')]
           [Input(component_id='Observation Value', component_property='value')]
)
def update_graph(SeriesDisplayName):
    print(SeriesDisplayName)
    print(type(SeriesDisplayName))

    container = "The year chosen by user was: {}".format(SeriesDisplayName)

    dff = df.copy()
    dff = dff[dff["Observation Value"] == SeriesDisplayName]

    fig = px.bar(
        data_frame=dff,
        x='Observation Date',
        y='Observation Value',
        labels={"Observation of education"},
    )
    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)

