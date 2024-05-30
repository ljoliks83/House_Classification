#  write your code here 
import pandas as pd

df_rock = pd.read_csv('/Users/alexeysobolev/PycharmProjects/House Classification/Topics/Summarizing numeric columns/Rock or Mine/data/dataset/input.txt')

rock_median_df = df_rock.loc[df_rock.labels == 'R']
mine_median_df = df_rock.loc[df_rock.labels == 'M']

print('M = ' + str(round(mine_median_df.null_deg.median(), 3)) + ' R = '
      + str(round(rock_median_df.null_deg.median(), 3)))