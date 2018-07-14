#Palindrome
temp=word=input('Enter a Word')
l=list(word)
l.reverse()
word=''.join(l)
word=word.upper()
print(word)

if temp==word:
    print('Palindrome')
else:
    print('Not a Palindrome')





'''
word=input('Enter a Word')
'''
