
# Immutable ---->having value type storing

x=10
print(id(x))
x=20
print(id(x))

# Mutable ---->having refrence type storing 
a1=[3,5,3]
b1=a1
b1.append(4)
print(b1)
print(id(a1),id(b1))

a=[10,20,30]
b=a[:]
b.append(34)#-----> but here it is shallow copy of list
print(a,b)
print(id(a),id(b))#------- having differnt ids


# String 
str_1='Hi there its 2026'
print(str_1)

str_2="Hola, Today is good day"
print(str_2)

# Multiline string
mul_str=''' Hi there this is 
multiline string'''
print(mul_str)

#Methods of String
print(str_1.upper())
print(str_2.lower())

new_string="Hi there its new journey focuseson what can be good."

print(new_string.capitalize())
print(new_string.title())

new_string1="  Hey devs its time to comeback and straight to work  "
print(new_string1.lstrip())
print(new_string1.rstrip())

S1="Hey buddy its your high time."
print(S1.replace("time","Chance"))

# Seperator
S2="Ram is great."
print(S2.split())

s2=" Apple : banana: grapes"
print(s2.split(":"))

#join 
l1=["I", "Love","Coding"]
print(" ".join(l1))

l2=["RR","Kkr","Csk","Mi"]
print(",".join(l2))

