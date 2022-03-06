principal = 1000
rate = 10
time = 5
number = 6

rate=rate/100
amount = principal * pow(1+(rate/number), number*time)
ci = amount - principal

print('Compound interest = %.2f' %ci)
print('Total amount = %.2f' %amount)

# Python program to find compound interest using user inputs

# store the inputs
principal = float(input('Enter principal amount: '))
rate = float(input('Enter the interest rate: '))
time = float(input('Enter time (in years): '))
number = float(input('Enter the number of times that 
                            interest is compounded per year: '))

# convert rate
rate = rate/100

# calculate total amount
amount = principal * pow( 1+(rate/number), number*time)
# calculate compound interest
ci = amount - principal

# display result
print('Compound interest = %.2f' %ci)
print('Total amount = %.2f' %amount)

# Python program to find compound interest using functions 

def compund_interest(principal,rate,time,number):
       # calculate total amount
      amount = principal * pow( 1+(rate/number), number*time)
      return amount;

# store the inputs
principal = float(input('Enter principal amount: '))
rate = float(input('Enter the interest rate: '))
time = float(input('Enter time (in years): '))
number = float(input('Enter the number of times that interest is compounded per year: '))

# convert rate
rate = rate/100

# calling function 
amount = compund_interest(principal,rate,time,number)
# calculate compound interest
ci = amount - principal

# display result
print('Compound interest = %.2f' %ci)
print('Total amount = %.2f' %amount)

    

