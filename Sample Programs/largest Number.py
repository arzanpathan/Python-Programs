c,b,Total=999999999,0,0
for i in range(10):
 a=int(input('Enter a New No'))
 if(a>b):
     b=a
 else:
     b=b
 if(a==b):
     b=a
 if(a<c):
     c=a
 else:
     c=c
 if(a==c):
     c=a
 Total=a+Total
     
print('Largest Number is: ',b)
print('Smallest Number is: ',c)
print('Sum of all Numbers is: ',Total)
print('Average Number is: ',Total/2)
       
