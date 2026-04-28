#Simple calculator
num1 = float(input("\nEnter first number: "))
num2 = float(input("\nEnter second number: "))

print("\nChoose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Floor Division (//)")
print("7. Exponentiation (**)")

choice = int(input("\nEnter choice (1-7): "))

if choice == 1:
    print("Result:", num1 + num2)

elif choice == 2:
    print("Result:", num1 - num2)

elif choice == 3:
    print("Result:", num1 * num2)
             
elif choice == 4:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")

elif choice == 5:
    print("Result:", num1 % num2)

elif choice == 6:
    print("Result:", num1 // num2)

elif choice == 237:
    print("Result:", num1 ** num2)

else:
    print("Invalid choice!")







#multi line assignment using add arithematic
x=(11+
   22+
   33+
   44)
print("total=",x)










#logic tables
t=1
f=0

#And 
print(f and f)
print(f and t)
print(t and f)
print(t and t)
 
#Or
print(f or f)
print(f or t)
print(t or f)
print(t or t)

#Not
print(not t)
print(not f)
 