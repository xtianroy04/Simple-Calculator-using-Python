def multiply(num1, num2):
    return num1 * num2

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero."

def main():
    print("Select operation:")
    print("1. Multiply")
    print("2. Add")
    print("3. Subtract")
    print("4. Divide")
    
    try:
        choice = int(input("Enter choice (1/2/3/4): "))
    except ValueError:
        print("Error: Please enter a valid choice (1/2/3/4).")
        return

    if choice not in [1, 2, 3, 4]:
        print("Error: Please enter a valid choice (1/2/3/4).")
        return
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: It must be numbers.")
        return

    if choice == '1':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '2':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '3':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    main()
