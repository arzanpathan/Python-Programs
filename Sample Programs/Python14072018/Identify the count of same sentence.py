#count of a word in a sentence
s=input('Enter a String')
l=s.split()
print(l)
for each in l:
 print(l.count(each))
 
#Count with the Words in sentence
s=input('Enter a Sentence: ')
l=s.split()
for each in l:
 print(each,' : ',l.count(each)
'''
s=input('Enter a Sentence: ')
l=s.split()
for each in l:
 if each!=each:
     print(each,' : ',l.count(each))'''
       
#To Separate Same word in a sentence
s=input('Enter a Sentence: ')
l=s.split()
x=[]
for each in l:
 if each not in x:
     print(each,' : ',l.count(each))
     x.append(each)
#    
s=input('Enter a Sentence: ')
l=s.split()
x=[]
y=[]
for each in l:
 if each not in x:
     print(each,' : ',l.count(each))
     x.append(each)
     y.append(l.count(each))
print(y)
print(x)




