import os
import requests
import sys
import pandas as pd


house_class = pd.read_csv('../Data/house_class.csv')

print(house_class.info())

rows = house_class.shape[0]
columns = len(house_class.columns)
nan = house_class.isnull().values.any()
max_rooms = house_class.Room.max()
mean_area = round(house_class.Area.mean(), 1)
zip_loc_unique = house_class.Zip_loc.nunique()

print(rows)
print(columns)
print(nan)
print(max_rooms)
print(mean_area)
print(zip_loc_unique)