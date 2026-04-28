x=bytes([65,66,67])
print(x)
for i in x:
    print(i)
print(x[1])

# Now for bytearray
arr=bytearray([65,66,67])
print(arr)# Single entity treated
for i in arr:
    print(i)
arr[2]=70
print(arr)# Modification possible
  
# Range 

#type 1
d1=range(10)
print(d1)
for i in d1:
    print(i)
print(d1[4])

 #Type 2

d2=range(1,20)
for i in d2:
    print(i)
#d2[10]=3 can't modify
print("Range with steps")
#Type 3
for i in range(10,20,2):
    print(i)
print("opposite")
d3=range(20,10,-1)
for i in d3:
    print(i)
#print(d3[10])# indexError
print(d3[9],"is at 9 index")
print(d3[-1])