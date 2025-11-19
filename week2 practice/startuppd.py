#USA Funding with pandas
import pandas as pd
#read csv file
df= pd.read_csv('Startup in 2021 end.csv', delimiter=',')
print(df)
#Remove the dolllar sign using.Str.replace()
df["Valuation ($B)"]=df['Valuation ($B)'].str.replace('$','',regex=False)
#Convert numeric type
df['Valuation ($B)']=df['Valuation ($B)'].astype(float)
print(df)
Valuation=df['Valuation ($B)']

print(Valuation)
print("df - data types" , df.dtypes)

print("df.info():   " , df.info() )

# display the last three rows
print('Last three Rows:')
print(df.tail(3))

# display the first three rows
print('First Three Rows:')
print(df.head(3))
print()

#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()
#Selecting a single row using .loc
second_row = df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df.loc[[1, 3]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df.loc[1:5]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()
#Selecting a single row using .iloc
second_row = Valuation.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

#Selecting multiple rows using .iloc
second_row2 = Valuation.iloc[[1, 3,5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

#Selecting a slice of rows using .iloc
second_row3 = Valuation.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()
# delete row with index 1
df.drop(index=2, inplace=True)
# delete rows with index 3 and 5
df.drop([3, 5], axis=0, inplace=True)
# display the modified DataFrame aft]er deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)