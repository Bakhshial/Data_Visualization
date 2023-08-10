import numpy as np
import pandas as pd
import plotly.express as px

melb=pd.read_csv("melb_data.csv")
train1=pd.read_csv("train.csv")
melb=melb[0:1000]
fig = px.scatter(melb, x="Lattitude", y="Longtitude", marginal_x="histogram", marginal_y="rug",color="Type")
fig.show()