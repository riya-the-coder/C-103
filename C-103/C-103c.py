import pandas as pd
import plotly.express as px

df=pd.read_csv('data.csv')
print(df)
fig=px.bar(df,y="Country",x="InternetUsers")
fig.show()