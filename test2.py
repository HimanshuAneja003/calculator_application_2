#Test.py
#
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")


if __name__ == "__main__":
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        option = int(
            input(
                "Choose operation (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division): "
            )
        )

        if option == 1:
            result = add(x, y)
        elif option == 2:
            result = subtract(x, y)
        elif option == 3:
            result = multiply(x, y)
        elif option == 4:
            result = divide(x, y)

        print(f"The result of {x} and {y} is: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero divisor.")

