#list comprehension in one liner
sq=[x**2 for x in range(11)]
print(sq)

even=[x for x in range(10) if x%2==0]
print(even)

ab=[ "true"if x%2==0 else "false" for x in range(11)]
print(ab)