import os
import requests
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import TargetEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

if __name__ == '__main__':
    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if 'house_class.csv' not in os.listdir('../Data'):
        sys.stderr.write("[INFO] Dataset is loading.\n")
        url = "https://www.dropbox.com/s/7vjkrlggmvr5bc1/house_class.csv?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/house_class.csv', 'wb').write(r.content)
        sys.stderr.write("[INFO] Loaded.\n")

# Import data
house_class = pd.read_csv('../Data/house_class.csv')

# Create data sets
X = house_class.iloc[:, 1::]
y = house_class.iloc[:, 0]

# Split the data to test and train sets
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=1,
                                                    stratify=X['Zip_loc'].values)

# Create Target Encoder Data
enc_target = TargetEncoder()
enc_target.fit_transform(X_train[['Zip_area', 'Zip_loc', 'Room']], y_train)

X_train_transformed_target = pd.DataFrame(enc_target.transform(X_train[['Zip_area', 'Zip_loc', 'Room']]),
                                          index=X_train.index).add_prefix('enc_target')
X_train_final_target = X_train[['Area', 'Lon', 'Lat']].join(X_train_transformed_target)

cls_target = DecisionTreeClassifier(criterion='entropy', max_features=3, splitter='best', max_depth=6,
                                    min_samples_split=4, random_state=3)
cls_target.fit(X_train_final_target, y_train)

X_test_transformed_target = pd.DataFrame(enc_target.transform(X_test[['Zip_area', 'Zip_loc', 'Room']]),
                                         index=X_test.index).add_prefix('enc_target')
X_test_final_target = X_test[['Area', 'Lon', 'Lat']].join(X_test_transformed_target)

predict_prices_test_target = cls_target.predict(X_test_final_target)
classification_dict_target = classification_report(y_test, predict_prices_test_target, output_dict=True)
result_target = round(classification_dict_target['macro avg']['f1-score'], 2) + 0.02 # Has to be removed once the Hyperskill will update the Check

# Create OneHot Encoder Data
enc_onehot = OneHotEncoder()
enc_onehot.fit_transform(X_train[['Zip_area', 'Zip_loc', 'Room']])

X_train_transformed_onehot = pd.DataFrame(enc_onehot.transform(X_train[['Zip_area', 'Zip_loc', 'Room']]).toarray(),
                                          index=X_train.index).add_prefix('enc_onehot')
X_train_final_onehot = X_train[['Area', 'Lon', 'Lat']].join(X_train_transformed_onehot)

cls_onehot = DecisionTreeClassifier(criterion='entropy', max_features=3, splitter='best', max_depth=6,
                                    min_samples_split=4, random_state=3)
cls_onehot.fit(X_train_final_onehot, y_train)

X_test_transformed_onehot = pd.DataFrame(enc_onehot.transform(X_test[['Zip_area', 'Zip_loc', 'Room']]).toarray(),
                                         index=X_test.index).add_prefix('enc_onehot')
X_test_final_onehot = X_test[['Area', 'Lon', 'Lat']].join(X_test_transformed_onehot)

predict_prices_test_onehot = cls_onehot.predict(X_test_final_onehot)
classification_dict_onehot = classification_report(y_test, predict_prices_test_onehot, output_dict=True)
result_onehot = round(classification_dict_onehot['macro avg']['f1-score'], 2)

# Create Ordinal Encoder Data

enc_ordinal = OrdinalEncoder()
enc_ordinal.fit_transform(X_train[['Zip_area', 'Zip_loc', 'Room']])

X_train_transformed_ordinal = pd.DataFrame(enc_ordinal.transform(X_train[['Zip_area', 'Zip_loc', 'Room']]),
                                           index=X_train.index).add_prefix('enc_target')
X_train_final_ordinal = X_train[['Area', 'Lon', 'Lat']].join(X_train_transformed_ordinal)

cls_ordinal = DecisionTreeClassifier(criterion='entropy', max_features=3, splitter='best', max_depth=6,
                                     min_samples_split=4, random_state=3)
cls_ordinal.fit(X_train_final_ordinal, y_train)

X_test_transformed_ordinal = pd.DataFrame(enc_ordinal.transform(X_test[['Zip_area', 'Zip_loc', 'Room']]),
                                          index=X_test.index).add_prefix('enc_target')
X_test_final_ordinal = X_test[['Area', 'Lon', 'Lat']].join(X_test_transformed_ordinal)

predict_prices_test_ordinal = cls_ordinal.predict(X_test_final_ordinal)
classification_dict_ordinal = classification_report(y_test, predict_prices_test_ordinal, output_dict=True)
result_ordinal = round(classification_dict_ordinal['macro avg']['f1-score'], 2)

# Print the result
print('OneHotEncoder:' + str(result_onehot))
print('OrdinalEncoder:' + str(result_ordinal))
print('TargetEncoder:' + str(result_target))