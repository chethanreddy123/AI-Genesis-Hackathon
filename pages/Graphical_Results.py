
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Read the data
df = pd.read_csv('data.csv')

# Create a title for the app
st.title('Movie Data Analysis')

# Create a sidebar with options to select the features to plot
st.sidebar.subheader('Select Features')

# Create a dropdown menu to select the x-axis variable
x_axis = st.sidebar.selectbox('X-Axis', df.columns)

# Create a dropdown menu to select the y-axis variable
y_axis = st.sidebar.selectbox('Y-Axis', df.columns)

# Create a scatter plot of the data
fig = px.scatter(df, x=x_axis, y=y_axis)
st.plotly_chart(fig)

# Create a correlation matrix of the data
corr = df.corr()
st.table(corr)

# Create a heatmap of the correlation matrix
fig = px.imshow(corr)
st.plotly_chart(fig)

# Create a linear regression model to predict the gross revenue of a movie
X = df.drop('Gross', axis=1)
y = df['Gross']

model = LinearRegression()
model.fit(X, y)

# Predict the gross revenue of a movie with a budget of $100 million
X_new = np.array([[100]])
y_pred = model.predict(X_new)

st.write('The predicted gross revenue of a movie with a budget of $100 million is $', y_pred)
