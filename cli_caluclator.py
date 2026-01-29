def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):     
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

def modulus(num1, num2):
    return num1 % num2

action = True

while action:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exit")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(e)
        elif choice == '5':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")
    elif choice == '6':
        action = False
        print("Exiting the calculator. Goodbye!")
    else:
        print("Invalid input. Please select a valid operation.")
