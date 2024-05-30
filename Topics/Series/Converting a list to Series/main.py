import pandas as pd


def create_series(foods, calories):
    # write your code here ....
    return pd.Series(calories, index=foods, name='Calorie content')


calorie = create_series(['f1', 'f2'], [10, 20])
