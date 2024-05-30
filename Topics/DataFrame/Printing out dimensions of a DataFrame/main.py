import pandas as pd


def print_dim(df):
    print('This DataFrame contains ' + str(df.shape[0]) + ' rows and ' + str(df.shape[1]) + ' columns')