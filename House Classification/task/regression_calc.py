X_1 = [-2, -1, 0, 1, 2]
X_2 = [2, 1, 0, -1, 2]
Y = [1.5, 1, 0, -0.5, 9]

pred_model_1 = []
pred_model_2 = []
pred_model_3 = []
pred_model_4 = []

for i in range(len(X_1)):
    pred_model_1.append(2 * X_1[i] + 3 * X_2[i])

for i in range(len(X_1)):
    pred_model_2.append(3 * X_1[i] + 2 * X_2[i])

for i in range(len(X_1)):
    pred_model_3.append(2 * X_1[i] + 3 * X_2[i] - 0.5)

for i in range(len(X_1)):
    pred_model_4.append(0.5 + 2 * X_1[i] + 3 * X_2[i])

print(pred_model_1)
print(pred_model_2)
print(pred_model_3)
print(pred_model_4)

sum_1 = 0
for i in range(len(X_1)):
    sum_1 += (Y[i] - pred_model_1[i]) ** 2

sum_2 = 0
for i in range(len(X_2)):
    sum_2 += (Y[i] - pred_model_2[i]) ** 2

sum_3 = 0
for i in range(len(X_2)):
    sum_3 += (Y[i] - pred_model_3[i]) ** 2

sum_4 = 0
for i in range(len(X_2)):
    sum_4 += (Y[i] - pred_model_4[i]) ** 2

mse_1 = sum_1 / len(X_1)
mse_2 = sum_2 / len(X_2)
mse_3 = sum_3 / len(X_1)
mse_4 = sum_4 / len(X_2)

print(mse_1)
print(mse_2)
print(mse_3)
print(mse_4)
