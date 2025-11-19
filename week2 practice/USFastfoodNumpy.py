
import numpy as np
#Load the entire data

address,long,lat,postalcode = np.genfromtxt("FastFoodRestaurants-V1.csv",delimiter=',',usecols=(0,4,5,7),invalid_raise=False, unpack=True, skip_header=1,dtype=('U100','f8','f8','U100'),#force correct type,
                                            encoding='Utf-8')
print(address)
print(long)
print(lat)
print(postalcode)

#USFastfood - statics operations
print("USFastfood Lat mean:", np.mean(lat))
print("USFastfood Lat average:", np.average(lat))
print("USFastfood Lat std:", np.std(lat))
print("USFastfood Lat mod:", np.median(lat))
print("USFastfood Lat percentile - 25:", np.percentile(lat,75))
print("USFastfood Lat percentile - 75:", np.percentile(lat,75))
print("USFastfood Lat percentile - 3:", np.percentile(lat,3))
print("USFastfood Lat min:", np.min(lat))
print("USFastfood Lat max:", np.max(lat))

#USFastfood - maths operations
print("USFastfood Lat square:", np.mean(lat))
print("USFastfood Lat sqrt:", np.sqrt(lat))
print("USFastfood Lat abs:", np.abs(lat))

#perform basic arithmetic operations
addition = long + lat
subtraction = long - lat
multiplication = long * lat
division = long / lat

print("USFastfood Long - Lat - Addition:",addition)
print("USFastfood Long - Lat - subtraction:",subtraction)
print("USFastfood Long - Lat - multiplication:",multiplication)
print("USFastfood Long - Lat - division:",division)


#Trigonometric Functions

latpie = (lat/np.pi) +1
#calculate sine, cosine, and tangent
sine_values = np.sin(latpie)
cosine_values = np.cos(latpie)
tangent_values = np.tan(latpie)

print("USFastfood Lat - div - pie - sine values:", sine_values)
print("USFastfood Lat - div - pie - cosine values:", cosine_values)
print("USFastfood Lat - div - pie - tangent values:", tangent_values)

print("USFastfood Lat - div - pie - Exponential values:", np.exp(latpie))

#calculate the natural logarithem and base-10 logarithem
log_array= np.log(latpie)
Log10_array= np.log10(latpie)

print("USFastfood Lat - div - pie - natural logarithem values:", log_array) 
print("USFastfood Lat - div - pie - base-10 logarithem values:", Log10_array) 

#Example: Hyperbolic sine
# calculate the hyperbolic sine of each element
sinh_values = np.sinh(latpie)
print("USFastfood Lat - div - pie - Hyperbolic sine values:",sinh_values)


#Hyperbolic cosine using cose() function
#calculate the hyperbolic cosine of each element
cosh_values = np.cosh(latpie)
print("USFastfood Lat - div - pie - Hyperbolic cosine values:",cosh_values)

#Hyperbolic tangent using tan() function
#calculate the hyperbolic tangent of each element
tanh_values = np.tanh(latpie)
print("USFastfood Lat - div - pie - Hyperbolic tangent values:",tanh_values)

#Example: Inverse hyperbolic sine
#calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(latpie)
print("USFastfood Lat - div - pie - Inverse Hyperbolic sine values:", asinh_values)

#Example: Invrse hyperbolic cosine
#calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccos(latpie)
print("USFastfood Lat - div - pie - Hyperbolic cosine values:",acosh_values)

#USFastfood long plus lat - 2 dimentional array
D2longlat = np.array([long,
                  lat])

print("USFastfood Long plus lat 2 dimentional array",D2longlat)

#check the dimension array1
print("USFastfood long plus lat 2 dimentional array - dimension",D2longlat.ndim)
#Output: 2

#RETURN total numbers of elements in array1
print("USFastfood long plus lat - 2 dimentional array - total numbers of elements",D2longlat.size)
#output: 6

#return a tuple that gives the size of array in each dimension
print("USFastfood long plus lat - 2 dimensional array - give size of array in each dimension",D2longlat.shape)
#output: int64

#check the datatype of array1
print("USFastfood long plus lat - 2dimensional array - splicing array - datatype",D2longlat.dtype)

#splicing array
D2longlatslice = D2longlat[:1,:5]
print("USFastfood long plus lat - 2dimensional array - splicing array - D2longlat[:1:5]",D2longlatslice)
D2longlatslice2 = D2longlat[:1, 4:15:4]
print("USFastfood long plus lat - 2dimensional array - splicing array - D2longlat[:1, 4:15:4]",D2longlatslice2)

#Indexing array
D2longlatsliceitemonly = D2longlatslice[0,1]
print("USFastfood long plus lat - 2dimensional array - index array - D2longlatslice[0,1]",D2longlatsliceitemonly)
D2longlatslice2itemonly = D2longlatslice2[0,2]
print("USFastfood long plus lat - 2dimensional array - index array - D2longlatslice2[0,2]",D2longlatslice2itemonly)


#you should use the buildin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2longlat):
    print(elem)

#EDIT: if you need indexes (as a tuple for 2D table),then:
for index,elem in np.ndenumerate(D2longlat):
    print(index, elem)
    