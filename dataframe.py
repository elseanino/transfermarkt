import os
import pandas as pd
from config import config


def dataframe():
    # Get path
    dict_path = config('path.ini','path')
    path = dict_path['path']

    # Get CSV file from Directory
    dir_list = {}
    for x in os.listdir(path):
        t = ''
        if x.endswith('.csv'):
            t = path + "\\" + x
        dir_list[x[:-5]] = t

    # Read each CSV file into DataFrame
    df_list = {}
    for x in dir_list:
        df = pd.read_csv(dir_list[x])
        df_list[x] = df

    return df_list
