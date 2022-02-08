import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv

def test():
    print("hey")
    df = pd.read_csv('data.csv')
    #print(df.head(n=10))

    #corr = df.corr(method='pearson')
    #c = corr.head()
    #print(c)

    data = df[['word count','state']]
    print(data)
    corr = data.corr(method='pearson')
    c = df['word count'].corr(df['state'])
    print(c)

    # TODO: Convert successful = 0, failed = 1, canceled = 2

def generate_formatted_csv():
    #========== Read from raw csv file ==========#
    raw_data = pd.read_csv('data.csv')
    column_vals = raw_data.values

    #========== Convert states to binary ==========#
    states = raw_data['state'].values
    word_count = raw_data['word count'].values

    # canceled = 0, failed = 1, successful = 2
    states_binary = []
    for state in states:
        if state == "canceled":
            states_binary.append(0)
        elif state == "failed":
            states_binary.append(1)
        elif state == "successful":
            states_binary.append(2)

    #========== Format raw data ==========#
    formatted_states = states_binary
    formatted_word_count = word_count.tolist()

    formatted_combined = [formatted_states, formatted_word_count]

    #========== Write new formatted csv file ==========#
    f = open('data_formatted.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(['state', 'word count'])
    writer.writerow(np.transpose(formatted_combined)[0])

    f.close()

generate_formatted_csv()