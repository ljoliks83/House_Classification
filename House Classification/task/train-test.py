from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine

data = load_wine(as_frame=True)["frame"]
u, v = data.iloc[:, :5], data.iloc[:, 5:9]
w, y = data.iloc[:, 9:-1], data["target"]

print(len(train_test_split(u, v, w, y, train_size=0.8, shuffle=True)))

