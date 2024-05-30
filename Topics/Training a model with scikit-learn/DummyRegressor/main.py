import pandas as pd
from sklearn.dummy import DummyRegressor

df = pd.read_csv('/Users/alexeysobolev/PycharmProjects/House Classification/Topics/Training a model with scikit-learn/DummyRegressor/data/dataset/input.txt')
X = df["X"]
y = df["y"]

dummy_regressor = DummyRegressor(strategy="quantile", quantile=0.4)

dummy_regressor.fit(X, y)
result = dummy_regressor.predict(X)

print(round(result[0], 4))
