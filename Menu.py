print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")

choice = input("Choose (1-4): ")

a = int(input("First number: "))
b = int(input("Second number: "))

if choice == "1":
    print("Result:", a + b)
elif choice == "2":
    print("Result:", a - b)
elif choice == "3":
    print("Result:", a * b)
elif choice == "4":
    print("Result:", a / b)
else:
    print("Invalid choice")
