# take input
num = int(input("Enter number:"))

if(num%2==0):
    print("{0} is an even number ".format(num))
else:
    print("{0} is an odd number".format(num))

# Python program to check even or odd using function
def oddeven(num):
    return(num%2==0)
    
# take input
num = int(input("Enter number:"))

if oddeven(num):
    print("{0} is an even number ".format(num))
else:
    print("{0} is an odd number".format(num))

# Python program to find even/odd using a given range
start = int(input('Start: '))
end = int(input('End: '))

for num in range(start, end + 1):
    if num%2==0:
        print(num,':Even')
    else:
        print(num,':Odd')


# Python program to print all even and odd numbers in given range 

# take range
start, end = 1, 100

for num in range(start, end + 1):
    # check number is odd or not
    if num % 2 == 0:
        print(num,end = ':Even ')
    else:
        print(num, end = ':Odd ')