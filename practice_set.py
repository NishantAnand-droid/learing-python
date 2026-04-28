x=bin(10)

print(x,type(x))

A=0b1010
B=0xABC
print(A+B)

# Sets and Frozenset

s={10.23,42,42,564,2}
print(s,type(s))
s.add(11)
print(s)
s.remove(2)
print(s)
s.discard(19)
s.pop()
print(s)
s.clear()
print(s,type(s))

x={}
x=set(x)
print(type(x))

fs=frozenset([10,34])
print(fs)


