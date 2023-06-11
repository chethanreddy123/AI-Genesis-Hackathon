
import streamlit as st
import pandas as pd
import plotly.graph_objs as go

# load the data
data = pd.read_csv('data.csv')

# create a line plot
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=data['Latest_Launch'],
    y=data['Sales_in_thousands'],
    mode='lines',
    name='Sales'
))

fig.update_xaxes(title_text='Latest Launch')
fig.update_yaxes(title_text='Sales in thousands')

st.plotly_chart(fig, use_container_width=True)
