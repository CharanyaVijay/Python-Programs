# Python program to find ASCII value of character

# take input
ch = input("Enter any character: ")

# printing ascii value of character
print("The ASCII value of " + ch + " is:", ord(ch))

# Python program to find ASCII value of all characters

#importing string function
import string

# printing ascii value of character
for c in string.ascii_letters:
    print(c,':', ord(c), end = ', ')
