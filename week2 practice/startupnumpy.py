import numpy as np

valuation = np.genfromtxt ("Startups in 2021 end (1).csv",delimiter=",",dtype=None,usecols=(2),unpack=True,skip_header=1,invalid_raise=False)

print(valuation)

# Remove the dollar sign using string slicing 
numeric_strings = np.array([s[1:] 
                            for s in valuation])
# Convert to a numeric type (e.g., float)  
print(numeric_strings)
price= numeric_strings.astype(float) 

print(price)
print("Startups in 2021 end (1).csv average:", np.average(price))
print("Startups in 2021 end (1).csv std:", np.std(price))
print("Startups in 2021 end (1).csv percentile - 25:", np.percentile(price,25))
print("Startups in 2021 end (1).csv percentile - 75:", np.percentile(price,75))
print("Startups in 2021 end (1).csv percentile - 3:", np.percentile(price,3))
print("Startups in 2021 end (1).csv max:", np.min(price))
print("Startups in 2021 end (1).csv max:", np.max(price))

#maths operation
print("Startups in 2021 end (1).csv square:", np.square(price))
print("Startups in 2021 end (1).csv sqrt:", np.sqrt(price))
print("Startups in 2021 end (1).csv pow:", np.pow(price,2))
print("Startups in 2021 end (1).csv abs:", np.abs(price))

#perform basic arithmetic operation
addition = price + 870
subtraction = price + 870
multiplication = price + 870
division = price + 870

print("Startups in 2021 end (1).csv price - 870 - addition:",addition)
print("Startups in 2021 end (1).csv price - 870 - subtraction:",subtraction)
print("Startups in 2021 end (1).csv price - 870 - multiplication:",multiplication)
print("Startups in 2021 end (1).csv price - 870 - division:",division)


#trigonometric functions
pricepie = (price/np.pi) + 1
#calculate sine, cosine, and tangent
sine_value = np.sin(pricepie)
cosine_values = np.cos(pricepie)
tangent_values = np.tan(pricepie)

print("Startups in 2021 end (1).csv price - div - pie - sine values:",sine_value)
print("Startups in 2021 end (1).csv price - div - pie - cosine values:",cosine_values)
print("Startups in 2021 end (1).csv price - div - pie - tangent values:",tangent_values)

print("Startups in 2021 end (1).csv price - div - pie - exponential values:",np.exp(pricepie))

#calculate the natural logaritem and base 10 logarithem
log_array= np.log(pricepie)
log10_array= np.log10(pricepie)

print("Startups in 2021 end (1).csv price - div - pie - natural logarithem values:",log_array)
print("Startups in 2021 end (1).csv price - div - pie - basr10 logarithem values:",log10_array)

#Example: hyperbolic sine
#calculate the hyperbolic sine of each element
sinh_values = np.sinh(pricepie)
print("Startups in 2021 end (1).csv price - div - pie - hyperbolic sine values:",sinh_values)

#Example : hyperbolic cosine using cosh() function
#calculate the hyperbolic cosine of each element
cosh_values = np.cosh(pricepie)
print("Startups in 2021 end (1).csv price - div - pie - hyperbolic cosine values:",cosh_values)

#Hyperbolic tangent function
#calculate the hyperbolic tangent of each element
tanh_values = np.tanh(pricepie)
print("Startups in 2021 end (1).csv price - div - pie - hyperbolic tangent values:",tanh_values)

#Example Inverse hyperbolic sine
#calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(pricepie)
print("Startups in 2021 end (1).csv price - div - pie - inverse hyperbolic sine values:",asinh_values)

#Inverse hyperbolic cosine
#calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(pricepie)
print("Startups in 2021 end (1).csv price - div - pie inverse hyperbolic cosine values:",acosh_values)

#startup
