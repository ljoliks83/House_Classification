from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

X, y = load_iris(return_X_y=True)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

setosa_df = pd.read_csv('/Users/alexeysobolev/PycharmProjects/House Classification/Topics/Decision tree with scikit-learn/Predict setosa/data/dataset/input.txt')

pred_setosa = clf.predict(setosa_df)

result = np.nonzero(pred_setosa == 0)

print(len(result[0]))