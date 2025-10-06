import numpy as np
# Load the entire data (not always useful if mixed data types)
data = np.genfromtxt("RealEstate-USA.csv",delimiter=',',skip_header=1,dtype=None ,encoding='utf-8')
print(data)

# Load selected columns using unpack
Brokered_by, Price, bed, bath, street, zip_code, house_size = np.genfromtxt("RealEstate-USA.csv", delimiter=",", usecols=(0,2,3,4,6,9,10), unpack=True, skip_header=1)


# Print selected columns
print("Brokered_by:", Brokered_by)
print("Price:", Price)
print("bed:", bed)
print("bath:", bath)
print("street:", street)
print("zip_code:", zip_code)
print("house_size:", house_size)
 #Arithematic operations between bed and bath
  

print(bed)
print(bath)
Addition = bed + bath
division = bed / bath
subtraction = bed - bath
multiplication = bed * bath
#Avoid 0 in division
 
print("addition(bed+bath):",Addition)
print("division(bed/bath):",division)
print("subtraction(bed-bath):",subtraction)
print("multiplication(bed*bath):",multiplication)

#Realstate statistics operation

print("RealEstate-USA.csv mean:",np.mean(Price))
print("RealEstate-USA.csv average:",np.average(Price))
print("RealEstate-USA.csv std:",np.std(Price))
print("RealEstate-USA.csv mod:",np.median(Price))
print("RealEstate-USA.csv percentile - 75:",np.percentile(Price,75))
print("RealEstate-USA.csv percentile -25:",np.percentile(Price,25))
print("RealEstate-USA.csv percentile -3:",np.percentile(Price,3))
print("RealEstate-USA.csv min:",np.min(Price))
print("RealEstate-USA.csv max:",np.max(Price))

#Realstate math operation

print("RealEstate-USA.csv square:",np.square(Price))
print("RealEstate-USA.csv sqrt:",np.sqrt(Price))
print("RealEstate-USA.csv pow:",np.power(Price,Price))
print("RealEstate-USA.csv abs:",np.abs(Price))

#trigonometric operation

PricePie =(Price/np.pi) + 1
#calculate sin, cosine,and tangent
sine_values = np.sin(PricePie)
cosine_values = np.cos(PricePie)
tangent_values = np.tan(PricePie)

print("Realstate - div - pie - sine_values:", sine_values)
print("Realstate - div - pie - cosine_values:", cosine_values)
print("Realstate - div - pie - tangent_values:", tangent_values)

print("Realstate - div - pie - exponential_values:",np.exp(PricePie))


#calculate the natural logarithemand Base_10 logarithem

log_array = np.log(PricePie)
log_10array = np.log10(PricePie)

#Example: Hyperbolic Sine
#Calculate the Hyperbolic sine of each element
sinh_value = np.sinh(PricePie)
print("Realstate - div - pie - Hyperbolic sine_values:",sinh_value)
 
#Hyperbolic cosine using cosh()Function
#Calcilate the Hyperbolic cosine of each element
cosine_values = np.cosh(PricePie)
print("Realstate - div - pie - Hyperbolus cosine_values:",cosine_values)

#Example: Hyperbolic Tangent
#Calculate the Hyperbolic Tangent of each element

tanh_values =np.tanh(PricePie)
print("Realstate - div - pie - Hyperbolic Tangent Values:",tanh_values)

#Example: Hyperbolic Sine

#Calculate the inverse Hyperbolic Sine of each element
asinh_values = np.arcsinh(PricePie)
print("Realstate - div - pie - Invrse Hyperbolic sine Values:",asinh_values)

#Example : Hyperbolic cosine

#Calculate the Inverse Hyperbolic cosine of each element
acosh_values = np.arccosh(PricePie)
print("Realstate - div - pie - Inverse Hyperbolic cosine Values:",acosh_values)

#Real state bed plus bath - 2 dimentional array
D2bedbath = np.array([bed,
                 bath])

print("Real state bed plus bath - 2 dimentional array - ",)
# chek the dimension of array1
print("Real state bed plus bath - 2 dimentional array - dimention",D2bedbath)

#check the dimension of array1
print("Real state bed plus bath - 2 dimentional array - dimention",D2bedbath.ndim)
#output:2

#Return the total number of elements in array1
print("Real state bed plus bath lat - 2 dimentional array - total numbers of elements",D2bedbath.size)
#output: 6

#return a tuple that gives size of array in each dimension
print("Real state bed plus bath lat - 2 dimentional array - gives size of array in each dimension",D2bedbath.shape)
#output(2,3)

#chek the date type of array1
print("Real state bed plus bath lat - 2 dimentional array - data type",D2bedbath.dtype)
#output: int64

#splicing array
D2bedbathSlice= D2bedbath[:1,:5]
print("Real state bed plus bath lat - 2 dimentional array - splicing array - D2bedbath[:1:5]",D2bedbathSlice)
D2bedbathSlice2= D2bedbath[:1, 4:15:4]
print("Real state bed plus bath lat - 2 dimentional array - slicing array - D2bedbath[:1, 4:15:4]",D2bedbathSlice2)


#Indexing array
D2bedbathsliceItemOnly= D2bedbathSlice[0,1]
print("Real state bed plus bath lat - 2 dimentional array - Index array - D2bedbathslice[1,5]",D2bedbathsliceItemOnly)
D2bedbathsliceItemOnly= D2bedbathSlice2[0,2]
print("Real state bed plus bath lat - 2 dimentional array - Index array - D2bedbathslice[0,2]",D2bedbathsliceItemOnly)


#you should use the build in function nditer,if you don't need to have the indexed value.
for index, elem in np.ndenumerate(D2bedbath):
    print(index, elem)