import os
import numpy as np
import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

input_file = 'data/data_cleaned.csv'

def show_plot():
    df = pd.read_csv(input_file)
    df = df.drop(columns=['words', 'images', 'gifs', 'videos', 'stretch goals', 'backers', 'campaign dur', 'twitter followers', 'platforms', 'developers', 'prev campaigns'])

    funding = df['funding']
    steam = df['steam']
    hand_drawn = df['handdrawn']
    pixel = df['pixel']

    corr_steam = stats.pointbiserialr(steam, funding)
    corr_hand_drawn = stats.pointbiserialr(hand_drawn, funding)
    corr_pixel = stats.pointbiserialr(pixel, funding)

    print('Steam: ', corr_steam)
    print('Hand-drawn: ', corr_hand_drawn)
    print('Pixel-art: ', corr_pixel)
    
    # assign data of lists.  
    data = {'steam': corr_steam[0], 'handdrawn': corr_hand_drawn[0], 'pixel': corr_pixel[0]}
    
    # Creates pandas DataFrame.  
    df_corr = pd.DataFrame(data, index =['funding', 'steam', 'handdrawn', 'pixel'])
    
    # print the data  
    print(df_corr)

    mask = np.zeros_like(df_corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    ax = sns.heatmap(
        df_corr.loc[['funding']], 
        annot=True,
        vmin=None, vmax=None, center=0,
        cmap=sns.diverging_palette(255, 0, as_cmap=True),
        square=True,
    )
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=35,
        horizontalalignment='right'
    )
    ax.set_yticklabels(
        ax.get_yticklabels(),
        rotation=0
    )
    ax.set_title("Influences on funding")
    plt.show()

show_plot()