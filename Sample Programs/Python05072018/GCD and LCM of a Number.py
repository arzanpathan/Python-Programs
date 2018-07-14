#WAP to get GCD and LCM of a number
a1,a2=int(input('Enter the Value of N1')),int(input('Enter the Value of N2'))

a1,a2=b1,b2

while(a1!=a2):
    if(a1>a2):
        a1=a1-a2
    else:
       a2=a2-a1
gcd=a1

lcm=(b1*b2)/gcd
print('Gcd is ',gcd,'LCM is ',lcm)

 
     
  
