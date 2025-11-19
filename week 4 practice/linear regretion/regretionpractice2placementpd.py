import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lets read the csv file in dataframe
df = pd. read_csv('placement.csv')

# Once the file is loaded print the header file using head() method
print(df.head())

# We can also check the shape of our dataset  using shape method
print("df.sdape:"    , df.shape)

# So what's the realtionship between these variables? A great way to explore the relationship is through Scatter plot. We will plot placement_exam_marks and placed as x-axis and y-axis as cgpa
df.plot.scatter(x='placement_exam_marks', y='cgpa')
plt.show()

print("df.corr():  ", df.corr())

print("df.describe():  ", df.describe())

print("df['placement_exam_marks'] : ",df['placement_exam_marks'])

print("df['cgpa'] : " , df['cgpa'])

# The .reshape() method takes in two arguments : first is number of coloumns you want the dataframe to have, and the second is number of rows you want the dataframe to have.
y = df['cgpa'].values.reshape(-1, 1)
X = df['placement_exam_marks'].values.reshape(-1, 1)

print("y :  " , y)
print("x : " , X)

print(df['cgpa'].values) 
print(df['cgpa'].values.shape) 
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
def calc(slope,intercept,marks):
    return slope*marks+intercept

Marks = calc(regressor.coef_,regressor.intercept_,53.0)
print(Marks)

Marks = regressor.predict([[53.0]])
print(Marks)

y_pred = regressor.predict(X_test)

df_pred = pd.DataFrame({'actual': y_test.squeeze(),'predict':y_pred.squeeze})
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