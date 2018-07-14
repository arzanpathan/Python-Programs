#WAP to find whether the given no is Armstrong or Not
no=int(input('Enter a Number '))
s=0
t=no
while(no!=0):
 r=no%10
 s=s+(r**3)
 no=no//10

if(s==t):
 print('It is an Armstrong Number ')
else:
     print('It is Not an Armstrong Number ')
