#WAP to take MRP from user of a Product and Display the Final Price after calculating with different schemes
#Scheme 1 40% of on MRP          2 60% of on MRP      3 80%  of on MRP  for all other product there is no Scheme applicable 
MRP,Scheme=int(input('MRP of a Product')),int(input('Scheme'))
if(Scheme==1):
 print('Final Price for Scheme 1',(60/100)*MRP)
elif(Scheme==2):
 print('Final Price for Scheme 2',(40/100)*MRP)
elif(Scheme==3):
 print('Final Price for Scheme 3',(20/100)*MRP)
else:
 print('Final Price for No Scheme',MRP)


