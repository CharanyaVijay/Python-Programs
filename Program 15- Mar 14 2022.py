# Python program to make a simple calculator

# take inputs
num1 = float(input('Enter first number:'))
num2 = float(input("Enter second number: "))

# choise operation
print("Operation: +, -, *, /")
select = input("Select operations: ")

# check operations and display result
# add(+) two numbers
if select == "+":
     print(num1, "+",  num2, "=", num1+num2)  
# subtract(-) two numbers
elif select == "-":
        print(num1, "-",  num2, "=", num1-num2)  
# multiplies(*) two numbers
elif select == "*":
        print(num1, "*", num2, "=", num1*num2)
# divides(/) two numbers
elif select == "/":
        print(num1, "/", num2, "=", num1/num2)
else:
        print("Invalid inputr")


# Python program to make a simple calculator using function

# This function adds two numbers
def add(a, b):
       return a + b

# This function adds subtract numbers
def subtract(a, b):
       return a - b

# This function adds multiply numbers
def multiply(a, b):
       return a * b

# This function adds division numbers
def divide(a, b):
       return a / b

# take inputs
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))

# choise operation
print("Operation: +, -, *, /") 
select = input("Select operations: ")

# check operations and display result
if select == "+":
   print(num1, " + ", num2, "= ", add(num1, num2))
elif select =="-":
   print(num1, " -", num2, "=", subtract(num1,num2))
elif select =="*":
   print(num1, "*", num2, "=", multiply(num1,num2))
elif select == "/":
   print(num1, "/", num2, "=", divide(num1,num2))
else:
   print("Invali input")
