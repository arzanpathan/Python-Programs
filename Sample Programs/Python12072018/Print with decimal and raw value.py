#Print variabbles using Various Format(Acces Specifier eg %d for decimal)
a,b,c=5,10,15
print('a=%d\nb=%d\nc=%d\n'%(a,b,c))#For Deciaml
print('a=%r\nb=%r\nc=%r\n'%(a,b,c))#For Raw data (by default it will consider integer)
print('a=%f\nb=%f\nc=%f\n'%(a,b,c))#For float
print('a=%s\nb=%s\nc=%s\n'%(a,b,c))#FOr String


print('a={0}\nb={0}\nc={0}\n'.format(a,b,c))# if its 0 value of 'a' will be printed in a,b,c
print('a={1}\nb={1}\nc={1}\n'.format(a,b,c))# Its like an Array                          
