import pandas as pd

df=pd.read_csv('RealEstate-USA.csv', delimiter=',')

print(df)
print("df- data types",df.dtypes)

print("df.info():",df.info())
#print last three rows
print("Print Last three rows:")
print(df.tail(3))
print()
#print first threee rows
print("Print first three rows:")
print(df.head(3))
print()
#Statistics of data frame using describe method()
print("Summary of Statistics of data frame using describe method",df.describe())
#Counting the rows and coloumn in Data Frame using shape().
print("Counting the rows and coloumn in DataFrame using shape():",df.shape)
print()


#acees the name coloumn
zipcode=df['zip_code']
print("Acess the name coloumn: df:")
print(zipcode)
print()
#Acess multiple coloumn
zipcode_housesize=[['zip_code','house_size']]
print("Acess multiple coloumns:df:")
print(zipcode_housesize)
print()
#selecting a single row using .loc
second_row=df.loc[1]
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

#delete row with index 1
df.drop(1, axis=0, inplace=True)
# delete row with index 1
df.drop(index=2, inplace=True)
# delete rows with index 3 and 5
df.drop([3, 5], axis=0, inplace=True)
# display the modified DataFrame aft]er deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)