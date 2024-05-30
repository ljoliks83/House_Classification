#  write your code here 
import pandas as pd

students = pd.read_csv('/Users/alexeysobolev/PycharmProjects/House Classification/Topics/Working with missing values/Drop NaNs/data/dataset/input.txt')

rows_count_initial = students.shape[0]

students.dropna(inplace=True)

rows_count_result = students.shape[0]

print(rows_count_initial, rows_count_result)

