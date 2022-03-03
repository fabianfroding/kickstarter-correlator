import os
import numpy as np
import pandas as pd
import csv
from datetime import datetime

input_file = 'data/data.csv'
output_file = 'data/data_cleaned.csv'

def format_csv(csv_file):
    raw_data = pd.read_csv(csv_file)

    #========== Get fields ==========#
    funding = raw_data['funding'].values.tolist()
    words = raw_data['words'].values.tolist()
    images = raw_data['imgs'].values.tolist()
    gifs = raw_data['gifs'].values.tolist()
    vids = raw_data['vids'].values.tolist()
    stretch_goals = raw_data['stretch goals'].values.tolist()
    backers = raw_data['backers'].values.tolist()
    campaign_dur = raw_data['campaign dur'].values.tolist()
    twitter_followers = raw_data['twitter followers'].values.tolist()
    platforms = raw_data['platforms'].values.tolist()
    developers = raw_data['developers'].values.tolist()
    prev_campaigns =  raw_data['prev campaigns'].values.tolist()
    # Binary/categorical values
    #states = raw_data['state'].values.tolist()
    steam = raw_data['steam'].values.tolist()
    handdrawn = raw_data['handdrawn'].values.tolist()
    pixel = raw_data['pixel'].values.tolist()
    

    cleaned_combined = [funding, words, images, gifs, vids, stretch_goals, backers, campaign_dur, twitter_followers, platforms, developers, prev_campaigns, steam, handdrawn, pixel]
    cleaned_transposed = np.transpose(cleaned_combined)

    #========== Write new cleaned csv file ==========#
    f = open(output_file, 'w')
    writer = csv.writer(f)

    # Write header
    writer.writerow(['funding', 'words', 'images', 'gifs', 'videos', 'stretch goals', 'backers', 'campaign dur', 'twitter followers', 'platforms', 'developers', 'prev campaigns', 'steam', 'handdrawn', 'pixel'])

    # Write rows
    for vals in cleaned_transposed:
        writer.writerow(vals)

    f.close()

format_csv(input_file)
