# decimal to binary 
a=64
print(bin(a))
_ds=128
print(bin(_ds))

# decimal to octal
a1=123
print(oct(a1))
A=23
print(oct(A))

#decimal to hexadecial
d=243
print(hex(d))

#bianry to deciaml  ******************
no='1100'
print(int(no,2))

#binary to octal
a2=0b1010
print(oct(a2))

#binary to hexa
a3=0b11000
print(hex(3))

  











  #Boolean 
E=True
f=False
print(E+f)
print(E-f)

g="Hello there\n" 
'''Multiple 
times printing '''
print(g*5)

p=bytes([65,66,67])#treat list as single object
print(p)
print(p[0])
for i in p: #differnt list object
    print(i)
print(type(p))\

v=b"abc" # b used for byte literals
print(type(v),v)


#Bytearray
y=bytearray([10,20,3,0])
for i in y:
    print(i)
    # perform changeable operation
y[2]=30
for i in y:
    print(i)
    # perform changeable operation
print(type(y))



list=[1,3,4,5,6,7]
print(list[2::-2])