#WAP to Check whether the given no is prime or not (Prime no means divisible by its own)
   #for k in range(2,no):c=no/k if(c!=1): print('\nIt is Not a Prime No')
no=int(input('\nEnter a No: '))

for i in range(2,no):
 if(no%i==0):
     print('It is not a Prime No')
     break
if(i==no-1):
 print('No is Prime')
