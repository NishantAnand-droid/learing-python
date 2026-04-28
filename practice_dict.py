# practice_dict.py
# simple dictionary with 5 elements and basic operations

my_dict = {
    "apple": 3,
    "banana": 5,
    "orange": 2,
    "grape": 10,
    "pear": 1
}

print(my_dict)

print(my_dict.get('apple'))
print(my_dict.pop('pear'))
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
my_dict.update({"cheeku":4})
print(my_dict)

#print(my_dict["mango"])# Error
print(my_dict.get("mango"))

new_dict={
    1:"Nishant",
    2:"ANAND",
    2:"Lamba"
}
print(new_dict) #duplicate keys take the last value of the same key

students=dict({1:"Nishant",2:"Anand"})
print(students)
print(students[1])
if 3 in students:
    print(3,"IS present")#key is present or not

A={"l1":"M1","l2":"M2"}
l3=A.setdefault("l3","M3")
print(A)

#Merge operator
d1={1:"Hindi",2:"English"}
d2={3:"Urdu"}
d3=d1|d2
print(d3)