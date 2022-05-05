# Python program to check if the number is a square root
# import math module
import math
#take inputs
num = int(input('Enter number:'))
# find sqrt
root = math.sqrt(num)
#Check if number is  a perfect square
if  int(root+0.5) **2 ==num:
     print(num, 'is a perfect square')
else:
     print(num,'is not a perfect square')

# Python program to check if the number is a square root using function
# import math module
import math

#function to check if number is a perfect square
def sqrt(num):
root = math.sqrt(num)
#Check if number is  a perfect square
if  int(root+0.5) **2 ==num:
     print(num, 'is a perfect square')
else:
     print(num,'is not a perfect square')
return root
#take inputs
num = int(input('Enter number:'))

#calling function
sqrt(num)
