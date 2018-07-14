x=31
y=23
#Comparison Operator
print('Value of x==y :',x==y)
print('Value of x>y :',x>y)
print('Value of x<y :',x<y)
print('Value of x>=y :',x>=y)
print('Value of x<=y :',x<=y)
print(x%10==0)

#Logical Operator
print('AND Operation',x%10==0 and x>30)

#No is ODD and No is < 50
print('No is Odd AND No<50',x%2!=0 and x<50)

#No is Not -ve and No is >20
print('No is -ve AND No>20',x>0 and x>20)

#Not -ve or Even No
print('No is -ve OR No is Even',x<0 and x%2==0)
      
#No is Divisible by 5 and 3
print('No/5 AND No/3',x%5==0 and x%3==0)

#No is -ve or even no less than 100
print('No is -ve OR Even No<100',x<0 or ((x%2==0) and x<100))      





