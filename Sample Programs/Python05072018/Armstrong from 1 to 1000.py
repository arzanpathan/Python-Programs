# Armstrong No From 1 to 1000
for i in range(1,1000):
 s=0
 t=i
 while(i!=0):
     r=i%10
     s=s+(r**3)
     i=i//10
     
 if(s==t):
     print(s)




#############################
for i in range(1,1000):
 s=0
 t=i
 while(i!=0):
     i,r=divmod(i,10)
     s=s+(r**3)
     
 if(s==t):
     print(s)

