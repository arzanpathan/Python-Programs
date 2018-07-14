#Create a list put Random values
l=[]
n=0
while(n!=4):
 r=float(input('Enter Your Marks: '))
 if (r>100):
     print('Your Value is Invalid')
     r=float(input('Enter Your Marks: '))
 
 l.append(r)
 print(l)
 n+1

l=[]
for n in range (5):
 r=float(input('Enter Your Marks: '))
 while(r>100):
     print('Your Marks is Invalid')
     r=float(input('Enter Your Marks: '))
 l.append(r)
 print(l)

