# Method a.count
a='hello world'
print(a.count('o'))

a='hello world'
print(a.count('hello'))

a='hello world hello world hello world'
print(a.count('l',7,16)) # 7 here is the Start point while 16 is the end point

print(a.count('l',7)) 

print(a.count('l',0,3))

# for making it Capital
a='hello world'
print(a.capitalize())

print(a.upper())
a='HELLO WORLD'
print(a.lower())

#Stripper
a='   hello world   '
print(a.strip()) # For removing the spaces or stripping the a sentence with spaces
print(a.lstrip())# For removing only left side spaces
print(a.rstrip())# For removing only right side spaces

#checks the starting of String
a='hello world'
print(a.startswith('he'))
print(a.endswith('rld'))

#For Checking the string
a='hello3'
print(a.isalnum()) # For Alphanumeric values
a='hello'
print(a.isalpha()) # For Alphabet values
a='43'
print(a.isdigit()) # For numeric values
a='Hello'
print(a.isupper()) # For checking is it upper case or not
a='hellO'
print(a.islower()) # For checking is it lower case or not
a="    "
print(a.isspace()) # For Spaces




from random import randint
print radint(2,6)















