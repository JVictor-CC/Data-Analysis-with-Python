import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column

df['overweight'] = (df['weight']/((df['height']/100)**2)).transform(lambda x: 0 if x <= 25 else 1)
     
# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

#print(df[['cholesterol','gluc']].head(10))
df['cholesterol'] = df['cholesterol'].transform(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].transform(lambda x: 0 if x == 1 else 1)
#print(df[['cholesterol','gluc']].head(10))

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars = ['cardio'], value_vars = ['cholesterol','gluc','smoke','alco','active','overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    
    #print(df_cat)
    df_cat = df_cat.groupby(['cardio','variable','value'], as_index=False).value_counts()
    df_cat.rename(columns={"count": "total"}, inplace=True)
  
    # Draw the catplot with 'sns.catplot()'
    plot = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", col = 'cardio', hue = 'value')

    # Get the figure for the output
    fig = plot.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    
    clean = df[
      (df['ap_lo'] > df['ap_hi']) | 
      (df['height'] < df['height'].quantile(0.025)) | 
      (df['height'] > df['height'].quantile(0.975)) | 
      (df['weight'] < df['weight'].quantile(0.025)) | 
      (df['weight'] > df['weight'].quantile(0.975))].index
  
    df_heat = df.drop(clean)
    
  
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(9, 9))
    

    # Draw the heatmap with 'sns.heatmap()'

    ax = sns.heatmap(corr, mask=mask, vmax=.5, square=True, annot=True, fmt='.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
