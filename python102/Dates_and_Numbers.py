#find the abslute value
num = -1000
print(abs(num))


#Rounding the number
num1 = 3.67
print(round(num1))

num2 = 5.431
print(round(num2 , 2))


#Exponentiation
num3 = 5
print(pow(num3 , 2))


#Find the largest and smallest value
numbers = 300 , 600 , 598 , 3 , 1965
print(max(numbers))

print(min(numbers))


#Add a set of numbers
numbers1 = 21 , 11 , 7 , 20 ,19
print(sum(numbers1)) 


#Finding the square root
import math
num4 = 64
print(math.sqrt(num4))


#The rest of the division
import math
print(math.remainder(21 , 4))
# OR 
num5 = 21%4
print(num5)


#Find a random number
#generate a random number between 1 - 100
import random
print(random.randint(1 , 100))


#Create a date
import datetime
date = datetime.date(2007 , 1 , 21)
print(date)
print(date.year)
print(date.month)
print(date.day)


#Create time
import datetime
time = datetime.time(22 , 38 , 40)
print(time)
print(time.hour)
print(time.minute)
print(time.second)


#Know the current time
import datetime
now = datetime.datetime.today()
print(now)
print(now.year)
print(now.day)
print(now.month)
print(now.hour)
print(now.minute)
print(now.second)


#Convert date to text
import datetime

date = datetime.date(2026 , 8 , 23)
time = datetime.time(23 , 47 , 35)

print(date)
print(time)
print(date.strftime("%A %B %Y"))

print(time.strftime("%I %M %S"))