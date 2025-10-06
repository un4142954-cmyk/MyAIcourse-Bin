import numpy as m

print("Start here ")
celiuse = float (input ("enter temperature =")) 
faherheit =((celiuse*9/5)+32)


print("Temperature in faherheit =",faherheit)

# Area of Rectangle
width = float(input ("enter width:"))
length= float(input("enter length: "))
area =  ( width*length)
print("area of rectangle =",area)

# Compound  interest
principal = float(input("enter your principal:"))
rate = float (input("enter interest rate"))
time = float (input("enter time rate"))
CI = principal*(1+ rate/100)**time- principal
print("Compuond Interset:",CI)

#PERIMETER of Rectangle 
per = width*length
print("Perimeter of a rectangle",per)

#Average of Three Number
num1 = float(input ("please enter a number "))
num2= float(input("please enter another nuumber"))
num3= float (input ("please enter a  number"))
avg= (num1 + num2+num3)/3
print("The of three number :",avg)

# squqre and cube 
num =float(input("enter a number want to get squqre and cube :"))
print ("the squqre of value :",m.square(num))
ma = num*num*num 
print("cube of value :",ma)


#Distribution item equailty
n = int (input ("please enter number of candies"))
k=int (input ("please enter number of student"))
print("Candies student each get:",n//k)
print("Remaining candies",n%k)

#Profit and loss
pri=float(input("enter cost price"))
ser=float(input("enter selling price"))
if ser>pri:
    print("you are in profit of :",ser-pri)
elif pri>ser:
    print("you are in loss of :",pri-ser)
else:
    print("No profit no loss")

#Totaal marks and percentage
num=[]
for i in range (5):
    marks = float(input("enter your marks"))
    num.append(marks)   #adding marks to list
total = sum(num)
percentage = total / 5
print("Total marks:", total)
print("Percentage:", percentage)
avg = total / 5
print("Average marks:", avg)  

#Salary calculation
basic = float(input("enter your basic salary"))
hra = 0.20 * basic
da = 0.10 * basic
gross_salary = basic + hra + da
print("Your gross salary is:", gross_salary)

#Age calculation
birth_year = int(input("enter your birth year"))
current_year = int(input("enter current year")) 
age = current_year - birth_year
print("Your age is:", age)
mon = age * 12
day = age * 365
print("Your age in month:", mon)
print("Your age in days:", day)

#Currency conversion
usd = float(input("enter amount in USD"))
inr = usd * 280
print("Amount in PKR:", inr)

#Sum of N natural numbers
n = int(input("enter a number"))
sum_n = n * (n + 1) / 2
print("Sum of first", n, "natural numbers is:", sum_n)

#Percentage of Correct answers
total_questions = int(input("enter total number of questions"))
correct_answers = int(input("enter number of correct answers")) 
percentage_correct = (correct_answers / total_questions) * 100
print("Percentage of correct answers:", percentage_correct)


#calculate speed , distance and time
distance = float(input("enter distance in km"))     
time = float(input("enter time in hours"))
speed = distance / time
print("Speed in km/h:", speed)
time = distance / speed
print("Time in hours:", time)
distance = speed * time
print("Distance in km:", distance)  

#calculate body mass index
weight =float(input("enter mass in kilograms:"))
height = float(input("enter height in meters:"))
BMI = weight / (height ** 2)
print("Your Body Mass Index (BMI) is:", BMI)

#Convert Minutes to Hours and Minutes
minutes = int(input("enter time in minutes:"))
hours = minutes // 60
remaining_minutes = minutes % 60
print("Time is:", hours, "hours and", remaining_minutes, "minutes")




