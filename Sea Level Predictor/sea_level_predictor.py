import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (10,8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.5,label='CSIRO Sea Level')
  
    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    pred = np.arange(1880,2051)
    ax.plot(pred, res.intercept + res.slope*pred, 'r', label='1880-2050')
    
    # Create second line of best fit
    x_res = df.loc[df['Year']>=2000]
    res2 = linregress(x_res['Year'], x_res['CSIRO Adjusted Sea Level'])
    pred2 = np.arange(2000,2051)
    ax.plot(pred2, res2.intercept + res2.slope*pred2, 'g', label='2000-2050')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()