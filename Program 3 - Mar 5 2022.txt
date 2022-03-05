# Python program to find average of three numbers

#take inputs
a=2
b=3
c=4

# calculate average
d=(a+b+c)/3

# display result
print(d)


# Python program to find average of three numbers using user input

#take inputs
a=float(input('Enter first number: '))
b=float(input('Enter second number: '))
c=float(input('Enter third number: '))

# calculate average
d=(a+b+c)/3

# display result
print(d)


# Python program to find average of three numbers using function

def avg_num(num1,num2,num3):
       avg = (num1+num2+num3)/3
       return avg


#take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))

#function call
average = avg_num(num1,num2,num3)

# display result
print('The average of numbers  =' ,average)
