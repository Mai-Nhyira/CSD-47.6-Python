#lets build a simple calculator using functions

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def modulus(x, y):
    return x % y
def exponential(x, y):
    return x ** y
def floordivision(x, y):
    return x // y
def squareroot(x, y):
    return x . y
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Exponentiation")
print("7. Floordivision")
print("8. Squareroot")
while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")
    if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == "5":
            print(f"{num1} % {num2} = {modulus(num1, num2)}")
        elif choice == "6":
            print(f"{num1} ** {num2} = {exponential(num1, num2)}")
        elif choice == "7":
            print(f"{num1} // {num2} = {floordivision(num1, num2)}")
        elif choice == "8":
            print(f"{num1} . {num2} = {squareroot(num1, num2)}")
        else:
            print("Invalid choice")
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid Input")

