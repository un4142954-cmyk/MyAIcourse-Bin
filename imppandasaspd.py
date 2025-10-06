
import pandas as pd
#Read csv file to dataframe
#Referance : https://pandas.pydata.org/docs/dev/reference/api/pandas.read_csv.html
#Note below , Dataformating - In Pandas,Datetime is a data type that represents a singlepoint in time. It is especially useful while dealing with time-series  stock prices,weather records, economic indecator etc
Df = pd.read_csv('C:\Users\welcome\Documents\GitHub\Realestate\Week2\imp pandas as pd.py',delimiter=';',parse_dates=[14],date_format={'date_added': '%d-%m-%y'})
