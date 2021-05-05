import pandas as pd 
import plotly.express as px
df=pd.read_csv("height-weight.csv")
fig=px.bar(df,x="Weight(Pounds)",y="Height(Inches)", size_max=100)
fig.show()