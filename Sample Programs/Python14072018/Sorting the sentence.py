s=input('Enter a Sentence: ')
l=s.split()
x=[] #Unique word
y=[] #
for each in l:
 if each not in x:
     x.append(each)     
x.sort()
print(x)
for each in x:
 if each not in y:
      y.append(l.count(each))
print(y)
 

l=s.split()
x=[] #Unique word
x.sort()
y=[] #Unique COunt
for each in l:
 if each not in x:
     x.append(each)
     y.append(l.count(each))
x.sort()

print(x)
print(y)
