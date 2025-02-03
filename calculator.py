# Basic Math Functions

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

def exponent(x, y):
    return x ** y

def floor_division(x, y):
    return x // y

# Menu to choose operations
def menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponent")
    print("7. Floor Division")

def main():
    while True:
        menu()
        
        # Take user input for operation
        choice = input("Enter choice (1/2/3/4/5/6/7) or 'q' to quit: ")
        
        if choice == 'q':
            print("Exiting...")
            break
        
        # Check if the choice is valid
        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Invalid Input")
            continue
        
        # Get the numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number input.")
            continue
        
        # Perform the operation
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")
        elif choice == '6':
            print(f"{num1} ** {num2} = {exponent(num1, num2)}")
        elif choice == '7':
            print(f"{num1} // {num2} = {floor_division(num1, num2)}")

if __name__ == "__main__":
    main()