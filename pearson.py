import os
import numpy as np
import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

input_file = 'data/data_cleaned.csv'

def show_plot():
    df = pd.read_csv(input_file)
    df = df.drop(columns=['steam', 'handdrawn', 'pixel'])
    corr = df.corr(method='pearson')
    corr.pop('funding')
    print(corr)

    print('Words: ', pearsonr(df['funding'], df['words']))
    print('Images: ', pearsonr(df['funding'], df['images']))
    print('Gifs: ', pearsonr(df['funding'], df['gifs']))
    print('Videos: ', pearsonr(df['funding'], df['videos']))
    print('Stretch goals: ', pearsonr(df['funding'], df['stretch goals']))
    print('Backers: ', pearsonr(df['funding'], df['backers']))
    print('Campaign duration: ', pearsonr(df['funding'], df['campaign dur']))
    print('Twitter followers: ', pearsonr(df['funding'], df['twitter followers']))
    print('Platforms: ', pearsonr(df['funding'], df['platforms']))
    print('Developers: ', pearsonr(df['funding'], df['developers']))
    print('Previous campaigns: ', pearsonr(df['funding'], df['prev campaigns']))

    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    ax = sns.heatmap(
        corr.loc[['funding']], 
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
    ax.set_yticklabels([])
    ax.set_title("Influences on funding")
    plt.show()

show_plot()