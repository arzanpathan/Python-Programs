# WAP to Print numbers from 1 to 50 but
# print 'fizz' if it is divisible 3
#'buzz' if it is divisible 5
#Print 'fizz and buzz'if it is divisible by both

for i in range(1,51):
 if(i%3==0 and i%5==0):
     print('fizz and buzz')
 elif(i%3==0):
     print('fizz')
 elif(i%5==0):
     print('buzz')
 else:
     print(i)

