#  $$$
#  ***
#  $$$
for i  in range(1,5):
 for j in range(1,2):
     if(i%2==0):
         print('*',end=' ')
     else:
         print('$',end=' ')
 print()

#1
#12
#123
#1234

for i  in range(4,0,-1):
 for j in range(1,i+1):
     print(j,end=' ')

 print()


#1
#12
#123
#1234

for i  in range(1,5):
 for j in range(1,6-i):
     print(j,end=' ')

 print()
