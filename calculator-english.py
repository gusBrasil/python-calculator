
# program to make a simple calculator

# these functions will add, subtract, multiply and divide

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("select an operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # this function will take the user's input
    choice = input("Enter choice (1/2/3/4): ")

    # this will check if the input was one of the available ones
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide((num1, num2)))

        # this function will check if the user wants another calculation
        # and will break the while loop if the answer is no
        next_calculation = input("Let's do another calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("invalid input")
