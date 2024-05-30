import pandas as pd
from sklearn.model_selection import train_test_split

house_class = pd.read_csv('../Data/house_class.csv')

X = house_class.iloc[:, 1::]
y = house_class.iloc[:, 0]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=1,
                                                    stratify=X['Zip_loc'].values)

Zip_loc_train_dict = dict(X_train['Zip_loc'].value_counts())

print(Zip_loc_train_dict)
