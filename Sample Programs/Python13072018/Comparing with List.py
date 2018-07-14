#Comparing with list
l1=[1,2,3,4]
l2=[1,2,5,6,7]
for x in l2:
 if x in l1:
     continue
 else:
     print(x)

     '''OR'''
     
l1=[1,2,3,4]
l2=[1,2,5,6,7]
for x in l2:
 if x not in l1:
     print(x)


l1=[1,2,3,4]
l2=[1,2,5,6,7]

for x in l2:
 if x not in l1:
     print(x)
for x in l1:
 if x not in l2:
     print(x)
     
     
'''
l1=[1,2,3,4]
l2=[1,2,5,6,7]
for l2 in l1:
 if(l1!=l2):
     print(l1)'''
  
