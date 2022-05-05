1,1,2,3,5,8,13,21,34

# Python program to print fibonacci series up to n-th term using while loop

# take input
num = int(input('Enter number of terms: '))

# print fibonacci series
a,b=0,1
i=0

# check if the number of terms is valid
if num <= 0:
    whi 

elif num== 1:
    print('Fibonacci series: ')
    print(a)

else:
   print('The Fibonnaci series:')  
   while(i<num):
      print(a,end = '   ')
      c=a+b
      a=b
      b=c
      i=i+1


# Python program to print fibonacci series up to n-th term using for loop

# take input
num = int(input('Enter number of terms: '))

# print fibonacci series
a,b=0,1
i=0

# check if the number of terms is valid
if num <= 0:
    whi 

elif num== 1:
    print('Fibonacci series: ')
    print(a)

else:
   print('The Fibonnaci series:')  
   for i in range (1, num+1):
     print(a,end = '   ')
     c=a+b
     a=b
     b=c


# Python program to find n-th fibonacci number

# take input
num = int(input('Enter number of terms: '))

# print fibonacci term
a, b = 0, 1
    
# check if the number of terms is valid
if num <= 0:
    print('Please enter a positive integer.')

elif num == 1:
    print('The Fibonacci term is = ', end='')
    print(a)

else:
    print('The Fibonacci term is = ', end='')
    for i in range (2, num):
        c = a + b
        a = b
        b = c
    print(b)
    
