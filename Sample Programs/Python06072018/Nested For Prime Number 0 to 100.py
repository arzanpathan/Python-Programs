#Nested For to print prime numbers from 1 to 100
j=0
print('2')
for i in range(2,101):
 no=i
 for j in range(2,no):
  if(no%j==0):
     break
 if(j==no-1):
     print(no)
