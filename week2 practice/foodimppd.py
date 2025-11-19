import pandas as pd
df=pd.read_csv('FastFoodRestaurants.csv',delimiter=',')
print(df)
print('df-data types:',df.dtypes)

print('df.info() :',df.info())

#display last three rows
print("last threee rows :")
print(df.tail(3))

#display first three rows
print("first three rows")
print(df.head(3))
print()
#summary of statistics of data frame using describe ()method
print("Summmary of statisstics of data frame using describe() method using shape",df.describe())
#counting the rows and coloumn in data frameusing shape()
print("Counting the rows and coloumn in data frameusing shape() :",df.shape)
print()
#acess the name coloumn
latitude=df['latitude']
print("acess the name coloumn:df: ")
print(latitude)
print()
#Acess multple coloumn
latitude_longitude=df[['latitude','longitude']]
print("acess multiple colcoumn :df:")
print(latitude_longitude)
print()
#Selecting a single row using .loc
second_row = df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()