#Square of even numbers from 1 to 10
print([x**2 for x in range (1,10) if (x**2)%2==0])
print([x**2 for x in range (1,10) if x%2==0]) # if you want to check only the base of that number
print([x**2 for x in range (2,11,2)]) # Optimal
