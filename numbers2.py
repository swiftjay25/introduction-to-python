import math

radius = input("please enter the radius of the circle ")
radius = float(radius )#this line takes the input, which is a string and converts it to a float, which is a number with a decimal point)
area = math.pi * math.pow(radius,2)
print (area)