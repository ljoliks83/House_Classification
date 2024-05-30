#  write your code here 

import pandas as pd
df_rock = pd.read_csv('/Users/alexeysobolev/PycharmProjects/House Classification/Topics/Summarizing categorical columns/Non-NA values/data/dataset/input.txt')

non_na_count = df_rock.labels.shape[0] - df_rock.labels.isna().sum()

print(non_na_count)