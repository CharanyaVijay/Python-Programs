# python program to find area of circle

# take inputs
r = 10

# calculate area of circle
area = 3.14 * r * r

# display result
print('Area of circle = ',area)


# python program to find area of circle using user inputs

# store input
r = float(input('Enter the radius of the circle: '))

# calculate area of circle
area = 3.14 * r * r

# display result
print('Area of circle = %.2f ' %area)

# python program to find area of circle using math file

import math   # math file

# store input
r = float(input('Enter the radius of the circle: '))

# calculate area of circle
area = math.pi * r * r

# display result
print('Area of circle = %.2f ' %area)


# python program to find area of circle using functions

import math  # math file

def area_of_circle(r):        #user-defined function
   area = math.pi*r*r          #calculate are of circle
   return area                     #return value

# store input
r = float(input('Enter the radius of the circle: '))

# display result
print('Area of circle = %.2f ' %area_of_circle(r))
