
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#lets read the csv file in dataframe
df = pd. read_csv('Linear\HousingData.csv')

#onces the data is loaded print the header file using head() method
print(df.head())

#we can aalso check the shape of our dataset using shape 
print("df.shape:"      ,df.shape)
  
#So, what's the relationship between these variables? A great way to explore relationships between variables is through Scatter plots. We'll plot the hours on the X-axis and scores on the Y-axis, and for each pair, a marker will be positioned based on their values: 
df.plot.scatter(x='INDUS',y='MEDV')
plt.show()

print("df.corr():     ",df.corr())


print("df.describe():     ",df.describe())


print("df['MEDV'] :  ",df['MEDV'])

#The .reshape() method takes in two arguments: the first is the number of columns you want the dataframe to have, and the second is the number of rows you want the dataframe to have.
y = df['MEDV'].values.reshape(-1, 1)
X = df['CRIM'].values.reshape(-1, 1)


print("y :  " , y)
print("x : " , X)

print(df['NOX'].values) 
print(df['NOX'].values.shape) 
#It expects a 2D input because the LinearRegression() class (more on it later) expects entries that may contain more than a single value (but can also be a single value). In either case - it has to be a 2D array, where each element (hour) is actually a 1-element array:

print(X.shape) 
print(X) 


SEED = 42

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = SEED)

print(X_train) 
print(y_train)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#now we need to fit the line into our data  we will do that data by using the.fit() method
regressor.fit(X_train, y_train)


print(regressor.intercept_)

print(regressor.coef_)
def calc(slope, intercept, research):
    return slope*research+intercept

MEDV = calc(regressor.coef_,regressor.intercept_,53.0)
print(MEDV)

MEDV= regressor.predict([[53.0]])
print(MEDV)

y_pred = regressor.predict(X_test)

df_pred = pd.DataFrame({'actual': y_test.squeeze(),'predict':y_pred.squeeze()  })
print(df_pred)

from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score

import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
#We will also print the metrics results using the f string and the 2 digit precision after the comma with :.2f:

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')    