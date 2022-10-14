import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=0, parse_dates=True)

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] <df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize=(12,8))
    ax.plot(df.index, df['value'], linewidth=1.0, color='red')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['months'] = df_bar['date'].dt.month
    df_bar['years'] = df_bar['date'].dt.year
    
    months = ['January','February','March','April', 'May','June','July','August','September', 'October','November','December']
    
    df_bar = df_bar[['years','months', 'value']].groupby(['years','months']).mean()
    
    df_bar = df_bar.unstack()
    # Draw bar plot

    fig, ax = plt.subplots(figsize = (14,10))
    df_bar.plot(kind='bar',ax=ax)
    ax.set_ylabel('Average Page Views')
    ax.set_xlabel('Years')
    ax.legend(labels=months, title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig ,(ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(22,10))

    sns.boxplot(ax=ax1, orient='v', data=df_box, x=df_box['year'], y=df_box['value'])
    sns.boxplot(ax=ax2, orient='v', data=df_box, x=df_box['month'], y=df_box['value'], order=['Jan','Feb','Mar','Apr', 'May','Jun','Jul','Aug','Sep', 'Oct','Nov','Dec'])

    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_ylabel('Page Views')
    ax1.set_xlabel('Year')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_ylabel('Page Views')
    ax2.set_xlabel('Month')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
