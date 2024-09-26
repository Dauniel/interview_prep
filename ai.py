import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X = np.array([[1], [2], [3], [4], [5]]).reshape(-1, 1)
y = np.array([30000, 35000, 50000, 60000, 80000])

model = LinearRegression()

model.fit(X, y)

y_pred = model.predict(X)

print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])

plt.scatter(X, y, color='blue', label='Actual Data')
plt.scatter(X, y_pred, color='red', label='Predicated Data')

plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Linear Regression Example')
plt.legend()
plt.show()
