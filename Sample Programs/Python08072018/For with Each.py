a='hello world'
for each in a:
 print(each)



#For Vowels

#To Find a Sequence
a='hello world'
if 'hw' in a:
 print('Present')
else:
 print('Absent')


# For getting a particular str on given value (index)
a='hello world'
print(a[6])

a='hello world'
print(len(a)) # a is a parameter hence len(a) is a function

#For Printing alphabets alternately
a='hello world'

for i in range(0,len(a),2):
 print('\n',a[i])

a.count='o' # here a is reference to the parameter o hence it is a Method

