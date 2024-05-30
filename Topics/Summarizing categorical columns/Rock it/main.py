#  write your code here 
import pandas as pd

df_rock = pd.read_csv('/Users/alexeysobolev/PycharmProjects/House Classification/Topics/Summarizing categorical columns/Rock it/data/dataset/input.txt')

print(df_rock.labels.loc[df_rock.labels == 'R'].count())