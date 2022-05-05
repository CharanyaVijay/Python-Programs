Multiplication Program in Python - 
# Using For loop
num = int(input('Display Multiplication table of : '))

for i in range(1,11):
     print("%d * %d = %d" % (num,i,num*i))

# Using while loop

num=int(input('Display Multiplication table of:'))

while i<11:
     print("%d * %d = %d" % (num,i,num*i))
     i=i+1

# Python program to print multiplication table from 1 to 10

print('Multiplication table from 1 to 10:')
for i in range (1,11):
         print('\n')
         for j in range(1,11):
             print(i*j,end='\t')

# Python program to print multiplication table in a given range

print('Display Multiplication table')
start=int(input('Start: ')) 
end=int(input('End: ')) 

#print multiplication table
for i in range (start, end+1):
         print('\n\nMutiplication table of %d\n' %(i))
         for j in range(1, 11):
             print('%d * %d = %d' % (i,j,i*j))