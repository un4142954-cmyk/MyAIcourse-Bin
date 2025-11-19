#  Seaborn Practice on Real Estate Data of USA
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data= pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})
df= pd.read_csv('RealEstate-USA.csv',delimiter=',') 
#print(df)
dffilter= df.head(100)
sns.set(style="whitegrid")
#kind='hist'  
g=sns.displot(data=dffilter, x="brokered_by" , y="price" , hue="city",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=brokered_by , y=price , hue=city,  kind='hist'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

""""kind="kde" in Seaborn specifies the use of Kernel Density Estimation plots. 
KDE plots visualize the probability density of a continuous variable. 
Instead of discrete bins like in histograms, KDE plots use a continuous curve to estimate 
the underlying distribution of the data. This provides a smoother and often more informative 
representation of the data's distribution, especially for continuous variables."""
#kind='kde'
g=sns.displot(data=dffilter, x="brokered_by" , y="price" , kind='kde')
g.figure.suptitle("sns.displot(data=dffilter, x=brodered_by , y= price , kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.kdeplot(data=dffilter, x="price")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=price)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

"""Draw a scatter plot with possibility of several semantic groupings.

The relationship between x and y can be shown for different subsets of the data using the hue, size,
and style parameters. These parameters control what visual semantics are used to identify the different 
subsets. It is possible to show up to three dimensions independently by using all three semantic types, 
but this style of plot can be hard to interpret and is often ineffective. Using redundant semantics (i.e.
both hue and style for the same variable) can be helpful for making graphics more accessible."""
# Use Seaborn to create a plot
g = sns.scatterplot(x='brokered_by', y='price', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='brokered_by', y='price', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

"""Draw a line plot with possibility of several semantic groupings.

The relationship between x and y can be shown for different subsets of the data using the hue, size, 
and style parameters. These parameters control what visual semantics are used to identify the different 
subsets. It is possible to show up to three dimensions independently by using all three semantic types, 
but this style of plot can be hard to interpret and is often ineffective. Using redundant semantics (i.e.
both hue and style for the same variable) can be helpful for making graphics more accessible."""
g=sns.lineplot(data=dffilter, x="brokered_by" , y="price"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=brokered_by , y=price  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

"""Show point estimates and errors as rectangular bars.

A bar plot represents an aggregate or statistical estimate for a numeric variable with the height of each 
rectangle and indicates the uncertainty around that estimate using an error bar. Bar plots include 0 in 
the axis range, and they are a good choice when 0 is a meaningful value for the variable to take."""
g=sns.barplot(data=dffilter, x="brokered_by", y="price", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=brokered_by, y=price, legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

""""Figure-level interface for drawing categorical plots onto a FacetGrid.

This function provides access to several axes-level functions that show the relationship between a 
numerical and one or more categorical variables using one of several visual representations. The kind 
parameter selects the underlying axes-level function to use."""

g=sns.catplot(data=dffilter, x="brokered_by", y="price")
g.figure.suptitle("sns.catplot(data=df, x=brokered_by, y=price)"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()

""""Plot rectangular data as a color-encoded matrix.

This is an Axes-level function and will draw the heatmap into the currently-active Axes if none is 
provided to the ax argument. Part of this Axes space will be taken and used to plot a colormap, 
unless cbar is False or a separate Axes is provided to cbar_ax."""
#.pivot(index="Model", columns="brokered_by", values="price")
glue = dffilter.pivot(columns="brokered_by", values="price")



print("Ends Here")