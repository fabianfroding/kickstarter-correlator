import os
import numpy as np
import pandas as pd
import csv
from datetime import datetime

def format_csv(csv_file):
    raw_data = pd.read_csv(csv_file)

    #========== Get fields ==========#
    states = raw_data['state'].values.tolist()
    words = raw_data['words'].values.tolist()
    images = raw_data['images'].values.tolist()
    gifs = raw_data['gifs'].values.tolist()
    vids = raw_data['videos'].values.tolist()
    stretch_goals = raw_data['stretch goals'].values.tolist()
    backers = raw_data['backers'].values.tolist()
    campaign_dur = raw_data['campaign dur'].values.tolist()
    twitter_followers = raw_data['twitter followers'].values.tolist()
    steam = raw_data['steam'].values.tolist()
    platforms = raw_data['platforms'].values.tolist()
    developers = raw_data['developers'].values.tolist()
    prev_campaigns =  raw_data['prev campaigns'].values.tolist()
    handdrawn = raw_data['handdrawn'].values.tolist()
    pixel = raw_data['pixel'].values.tolist()

    formatted_combined = [states, words, images, gifs, vids, stretch_goals, backers, campaign_dur, twitter_followers, steam, platforms, developers, prev_campaigns, handdrawn, pixel]
    formatted_transposed = np.transpose(formatted_combined)

    #========== Write new formatted csv file ==========#
    f = open('data/data_formatted.csv', 'w')
    writer = csv.writer(f)

    # Write header
    writer.writerow(['state', 'words', 'images', 'gifs', 'videos', 'stretch goals', 'backers', 'campaign dur', 'twitter followers', 'steam', 'platforms', 'developers', 'prev campaigns', 'handdrawn', 'pixel'])

    # Write rows
    for vals in formatted_transposed:
        writer.writerow(vals)

    f.close()

format_csv('data/data.csv')
