# Python program to check year is a leap year or not

# take input
year = int(input('Enter a year:  '))

# check leap year or not
if(year % 400) == 0:
   print('{0} is a leap year'.format(year))
elif (year % 100) ==0:
   print('{0} is not aleap year'.format(year))
elif (year % 400) == 0:
    print('{0} is a leap year'.format(year))
else:
    print('{0} is not a leap year'.format(year))


# Python program to check year is a leap year or not

# take input
year = int(input('Enter a year: '))

if(year % 4) == 0:
   if(year % 100) == 0:
      if(year % 400) == 0: 
               print('{0} is a leap year'.format(year))
      else:
               print('{0} is not a leap year'.format(year))
   else:
         print('{0} is a leap year'.format(year))
else:
     print('{0} is not a leap year'.format(year))    


# Python program to check year is a leap year or not using function

def checkyear(year):   #user-defined function
    # check leap year or not
     if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
     else:
        return False

# take input
year = int(input('Enter a year: '))

# function call and display result
if(checkyear(year)):
     print('{0} is a leap year'.format(year))
else:
     print('{0} is not a leap year'.format(year))
  
