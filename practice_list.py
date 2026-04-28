#list 
l1=[10,20,45,"aman"]
print(l1[1])
print(l1[-1])
print(l1[::-1])#reverse list
print(l1[:3])


a= [10, 20, 30, 40, 50]
print(a[0:3])
print(a[:4:-1])

#creating shallow copy of list
b=a[:]
b.append(90)
print(b)
print(a)#not affects list a

'''Applying list methods'''
list1=[10,20,30,40,50,90,34,42,1,33,100]

list1.append(200)
list1.extend([23,56,35,78,29,52])
print(list1)

list1.insert(2,'HOLÀ')
print(list1)

list1.remove(33)
print(list1)

list1.pop()
print(list1)
list1.pop(4)
print(list1)

list1.insert(4,55)
print(list1)

print(list1.index(100))
print(list1.count(33))

#copy method

fruits=["apple","mango",'Banana']
copy_fruits=fruits.copy()
print(fruits,id(fruits))
print(copy_fruits,id(copy_fruits))

copy_fruits.append("Litchi")
fruits.append("Cheeku")

print(fruits)
print(copy_fruits)

data=[11,323,22,44,66]
del data[1]
print(data)
del data[0:2]
print(data)

data.clear()
print(data)