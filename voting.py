age = int(input("Enter the age : "))
if age < 18:
    print("You are minor")
elif 18 <= age < 65:
    print("You are adult")
elif age > 65:
    print("You are senior")
