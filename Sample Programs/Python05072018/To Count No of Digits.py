#WAP to Count Number of digits in the given number

No=int(input('Enter a No '))

count=0
while(No!=0):
 count=count+1
 No=No//10
print('No of Digits',count)



#what if user enters 0 or 000
