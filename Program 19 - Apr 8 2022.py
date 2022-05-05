# Python Program to get the first digit of number

# take input
num = int(input('Enter any Number: '))

# get the first digit
while (num >= 10):
    num = num // 10

# printing first digit of number
print('The first digit of number:', num)


# Python Program to get the first digit of number using Math module and log function

# importing math module
import math

# take input
num = int(input('Enter any Number: '))

# get the first digit
digits = int(math.log10(num))
first_digit = int(num / pow(10, digits))

# printing first digit of number
print('The first digit of number:', first_digit)


# Python Program to get the first digit of number by converting int into string

# take input
num = int(input('Enter any Number: '))

# convert int to string
num_str = str(num)

# get the first digit
first_digit = num_str[0]

# printing first digit of number
print('The first digit of number:', first_digit)


# Python Program to get the first digit of number using slicing

# take input
num = int(input('Enter any Number: '))

# convert int to string
num_str = str(num)

# get the first digit
first_digit = num_str[:1]

# printing first digit of number
print('The first digit of number:', first_digit)


# Program to get the last digit

num = int(input('Enter number'))
num = num%10
print(num)

# Program to get the last digit using str

num = int(input('Enter any Number: '))

# convert int to string
num_str = str(num)

# get the last digit
i=len(num_str)
last_digit = num_str[i-1]

# printing first digit of number
print('The last digit of number:', last_digit)


# Program to get the last digit using slicing

num = int(input('Enter any Number: '))

# convert int to string
num_str = str(num)

# get the last digit
last_digit = num_str[-1:]

# printing first digit of number
print('The last digit of number:', last_digit)


