from pyexpat import model
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# reading the data_set
dataset = pd.read_csv('/Users/zakariadarwish/Desktop/poly_linear_regression/Position_Salaries.csv')
# feeding the dependant & independant variables
# where X is dep & y is indep
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# printing the indep. variable
print(f"The dep. variable \n{X}")

# printing the dep. variable
print(f"the indep. variable \n{y}")


lin_reg = LinearRegression()
lin_reg.fit(X, y)

poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)


lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# plt.scatter(X, y, color = 'red')
# plt.plot(X, lin_reg.predict(X), color = 'blue')
# plt.title('Truth or Bluff (Linear Regression)')
# plt.xlabel('Position Level')
# plt.ylabel('Salary')
# plt.show()


plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#prediction used in linear regression
print(lin_reg.predict([[6.5]]))

#prediction used in poly-linear regression
print(lin_reg_2.predict(poly_reg.fit_transform([[6.5]])))