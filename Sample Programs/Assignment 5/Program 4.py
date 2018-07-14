#WAP to take 10 inputs from user and print the largest,smallest,total,average(Total/2) out of it
print('WAP to take 10 inputs from user and print the largest,smallest,total,average(Total/2) out of it\n')
c,b,Total=9999999999,0,0
n=int(input('Enter No Of Inputs: '))
for i in range(n):
 a=int(input('Enter a New No: '))
 if(a>b):
     b=a
 else:
     b=b
 if(a<c):
     c=a
 else:
     c=c
 if(a==b):
     b=a
 if(a==c):
     c=a
 Total=a+Total
     
print('Largest Number is: ',b)
print('Smallest Number is: ',c)
print('Sum of all Numbers is: ',Total)
print('Average Number is: ',Total/n)
       
