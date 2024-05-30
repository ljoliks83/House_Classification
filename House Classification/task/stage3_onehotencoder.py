house_class = pd.read_csv('../Data/house_class.csv')

X = house_class.iloc[:, 1::]
y = house_class.iloc[:, 0]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=1,
                                                    stratify=X['Zip_loc'].values)

enc_train = OneHotEncoder(drop='first')

enc_train.fit_transform(X_train[['Zip_area', 'Zip_loc', 'Room']])

X_train_transformed = pd.DataFrame(enc_train.transform(X_train[['Zip_area', 'Zip_loc', 'Room']]).toarray(),
                                   index=X_train.index).add_prefix('enc')

X_train_final = X_train[['Area', 'Lon', 'Lat']].join(X_train_transformed)

cls = DecisionTreeClassifier(criterion='entropy', max_features=3, splitter='best', max_depth=6,
                             min_samples_split=4, random_state=3)

cls.fit(X_train_final, y_train)

X_test_transformed = pd.DataFrame(enc_train.transform(X_test[['Zip_area', 'Zip_loc', 'Room']]).toarray(),
                                  index=X_test.index).add_prefix('enc')
X_test_final = X_test[['Area', 'Lon', 'Lat']].join(X_test_transformed)

predict_prices_test = cls.predict(X_test_final)

result = accuracy_score(y_test, predict_prices_test)

print(result)
