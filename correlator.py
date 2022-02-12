import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
import seaborn as sns
import matplotlib.pyplot as plt

def test_correlation():
    df = pd.read_csv('data/data_formatted.csv')
    corr = df.corr(method='pearson')
    print(corr)
    corr.pop('state')

    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    ax = sns.heatmap(
        corr.loc[['state']], 
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
    ax.set_title("Success (state) correlations")
    plt.show()

test_correlation()