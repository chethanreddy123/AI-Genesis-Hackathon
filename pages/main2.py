import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_data(x, y):
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot')
    st.pyplot()

def main():
    st.title('Simple Plot App')
    
    # Sidebar inputs
    x_start = st.sidebar.number_input('X Start', value=0)
    x_end = st.sidebar.number_input('X End', value=10)
    num_points = st.sidebar.number_input('Number of Points', value=50, min_value=2)
    
    # Generate data
    x = np.linspace(x_start, x_end, num_points)
    y = np.sin(x)
    
    # Plot the data
    plot_data(x, y)

if __name__ == '__main__':
    main()

