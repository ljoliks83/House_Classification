from sklearn.metrics import classification_report
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd

true_labels = ['apple', 'banana', 'orange', 'pear', 'apple', 'banana', 'orange', 'pear']
predicted_labels = ['apple', 'banana', 'orange', 'pear', 'orange', 'banana', 'orange', 'apple']

df = pd.DataFrame({"True_Labels": true_labels, "Predicted_Labels": predicted_labels})

print(classification_report(df["True_Labels"], df["Predicted_Labels"], output_dict=True, labels=["pear"]))






enc_ordinal = OrdinalEncoder()
enc_ordinal.fit_transform(X_train[['Zip_area', 'Zip_loc', 'Room']], y_train)

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
result_target = round(classification_dict_ordinal['macro avg']['f1-score'], 2)