#  write your code here 
import pandas as pd

students = pd.read_csv('/Users/alexeysobolev/PycharmProjects/House Classification/Topics/Working with missing values/Calculate proportions of NaNs/data/dataset/input.txt')

print(round(students.isnull().sum() / students.shape[0], 2))
