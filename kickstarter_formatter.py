import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
from datetime import datetime

def format_date(d):
    return datetime.strptime(d, '%Y-%m-%d %H:%M:%S')

def generate_formatted_csv():
    #========== Read from raw csv file ==========#
    raw_data = pd.read_csv('data.csv')
    column_vals = raw_data.values

    #========== Convert states to binary ==========#
    states = raw_data['state'].values

    # canceled = 0, failed = 1, successful = 2
    states_binary = []
    for state in states:
        if state == "canceled":
            states_binary.append(0)
        elif state == "failed":
            states_binary.append(1)
        elif state == "successful":
            states_binary.append(2)

    #========== Funding gained: pledged / goal ==========#
    #goal = raw_data['goal'].values
    #pledged = raw_data['pledged'].values
    #funding_gained = []

    #i = 0
    #while i < len(goal) and i < len(pledged):
    #    funding_gained.append(pledged[i] / goal[i])
    #    i += 1

    #========== Funding period: deadline - launched at ==========#
    deadline = raw_data['deadline'].values
    launched_at = raw_data['launched at'].values
    funding_period = []

    i = 0
    while i < len(deadline) and i < len(launched_at):
        funding_period.append((format_date(deadline[i]) - format_date(launched_at[i])).days)
        i += 1

    #========== Format raw data ==========#
    formatted_word_count = raw_data['word count'].values.tolist()
    formatted_audio_count = raw_data['audio count'].values.tolist()
    formatted_gif_count = raw_data['gif count'].values.tolist()
    formatted_img_count = raw_data['img count'].values.tolist()
    formatted_links_count = raw_data['links count'].values.tolist()
    formatted_backers_count = raw_data['backers count'].values.tolist()

    formatted_combined = [states_binary, formatted_word_count, formatted_audio_count, formatted_gif_count, formatted_img_count, formatted_links_count, formatted_backers_count, funding_period]
    formatted_transposed = np.transpose(formatted_combined)

    #========== Write new formatted csv file ==========#
    f = open('data_formatted.csv', 'w')
    writer = csv.writer(f)

    # Write header
    writer.writerow(['state', 'word count', 'audio count', 'gif count', 'img count', 'links count', 'backers count', 'funding period'])

    # Write rows
    for vals in formatted_transposed:
        writer.writerow(vals)

    f.close()

generate_formatted_csv()