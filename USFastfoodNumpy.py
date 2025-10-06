
import numpy as np
#Load the entire data

long,lat,postalcode = np.genfromtxt("FastFoodRestaurants-V1.csv",delimiter=',',usecols=(4,5,7),invalid_raise=False, unpack=True, skip_header=1,dtype=None)

print(long)
print(lat)
print(postalcode)













