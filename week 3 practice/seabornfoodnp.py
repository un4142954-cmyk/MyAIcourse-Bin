import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Fast food Resturant data of USA: Example of data set
#Load data from csv file
df=pd.read_csv("FastFoodRestaurants.csv",delimiter=',',index_col='address')
print(df.dtypes)
dffilter=df.head(200)
#kind 'His'
g=sns.displot(data=dffilter,x="city",y="province",hue="postalCode",kind="hist")
g.figure.suptitle("sns.displot(data=dffilter,x=city, y=price,hue=agent,kind ='hist')")
#display the plot
g.figure.show()
read=input("wait for me......")
#kind='kde'
g=sns.displot(data=dffilter,x="longitude",y="latitude",hue="province",kind="kde")
g.figure.suptitle("sns.displot(data=dffilter,x=longitude, y=latitude,hue=provincet,kind ='kde')")
#display the plot
g.figure.show()
read=input("wait for me......")
#kind='kde' direct reading command
g= sns.kdeplot(data=dffilter, x="longitude", y="latitude")
g.figure.suptitle("sns.kdeplot(data=dffilter, x='longitude', y='latitude')")

# Display the Plot
g.figure.show()
# read=input("Wait for me.....")

# Use Seaborn to create Scatter Plot a plot
g = sns.scatterplot(x='longitude', y='latitude', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='Longitude', y='latitude', data=dffilter)"  )
g.figure.show()


"""Draw a line plot with possibility of several semantic groupings."""
g=sns.lineplot(data=dffilter, x="longitude" , y="latitude")
g.figure.suptitle("sns.lineplot(data=dffilter, x=longitude , y=latitude)")
# Display the plot
g.figure.show()

# A Bar Plot
g=sns.barplot(data=dffilter, x="latitude", y="longitude") 
g.figure.suptitle("sns.barplot (data=dffilter, x=latitude, y=longitude)")
g.figure.show()

# Categorical Plots 

g=sns.catplot(data=dffilter, x="latitude", y="longitude")
g.figure.suptitle("sns.catplot(data=dffilter, x=latitude, y=longitude)"  )
# Display the plot
g.figure.show() 

# Pivot table

glue = dffilter.pivot(columns="latitude", values="longitude")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=latitude, values=longitude)"  )
# Display the plot
g.figure.show()

print("------------------------Ends Here-----------------------------")