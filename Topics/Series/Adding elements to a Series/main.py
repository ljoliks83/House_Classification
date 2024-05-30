import pandas as pd


list = [7, 4, 1, 1, 3, 2, 1, 9]
series = pd.Series(list)
print(series)
print(series.mean())
print(series.mode())
print(series.median())