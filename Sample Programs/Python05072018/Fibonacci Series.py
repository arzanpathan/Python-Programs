#Fibonacci Series
no=int(input('How Many Elements'))
a,b=0,1
print(a,b)
for i in range (1,no-1):
 c=a+b
 print(c)
 a,b=b,c
    


