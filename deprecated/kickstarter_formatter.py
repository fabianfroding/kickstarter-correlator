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

def is_metroidvania(val):
    return 'metroidvania' in val or '2d platformer' in val or 'sidescroller' in val

def filter_metroidvanias(vals, raw_data):
    filtered = []
    i = 0
    while i < len(vals) and i < len(raw_data):
        if is_metroidvania(raw_data['blurb'].values[i]):
            filtered.append(vals[i])
        i += 1
    return filtered

def generate_formatted_csv_2d_platformers():
    #========== Read from raw csv file ==========#
    raw_data = pd.read_csv('data.csv')

    #==========  ==========#
    #metroidvanias = []
    #stories = raw_data['blurb'].values
    #metroidvanias.append(['name', 'slug', 'url', 'word count', 'audio count', 'gif count', 'img count', 'links count', 'story, id', 'backers count', 'blurb', 'country', 'country displayable name', 'currency, category', 'converted pledged amount', 'goal', 'pledged', 'usd_pledged', 'state', 'created at', 'deadline', 'launched at', 'state_changed_at'])

    #i = 0
    #while i < len(stories) and i < len(raw_data):
    #    if ('metroidvania' in stories[i] or '2d platformer' in stories[i] or 'sidescroller' in stories[i]):
    #        metroidvanias.append(raw_data.values[i])
    #    i += 1

    #and raw_data['state'].values[i] == 'successful'
    #for val in raw_data:
        #print(val['story'])
        #if 'metroidvania' in val['story'].value:
            #metroidvanias.append(val)

    #print(len(metroidvanias))
    #print(type(raw_data))
    #print(type(metroidvanias))
    #d = pd.DataFrame(metroidvanias)
    #raw_data = d


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
    states_binary = filter_metroidvanias(states_binary, raw_data)
    

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
    funding_period = filter_metroidvanias(funding_period, raw_data)

    #========== Format raw data ==========#
    formatted_word_count = filter_metroidvanias(raw_data['word count'].values.tolist(), raw_data)

    formatted_audio_count = filter_metroidvanias(raw_data['audio count'].values.tolist(), raw_data)
    formatted_gif_count = filter_metroidvanias(raw_data['gif count'].values.tolist(), raw_data)
    formatted_img_count = filter_metroidvanias(raw_data['img count'].values.tolist(), raw_data)
    formatted_links_count = filter_metroidvanias(raw_data['links count'].values.tolist(), raw_data)
    formatted_backers_count = filter_metroidvanias(raw_data['backers count'].values.tolist(), raw_data)

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

generate_formatted_csv_2d_platformers()