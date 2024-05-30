#  write your code here 
import pandas as pd

students = pd.read_csv('/Users/alexeysobolev/PycharmProjects/House Classification/Topics/Working with missing values/Count NaNs/data/dataset/input.txt')

print(students.isnull().sum())