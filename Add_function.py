def add_numbers(a: float, b: float) -> float:
    """
    Function to add two numbers.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: Sum of a and b
    """
    return a + b


if __name__ == "__main__":
    print("Welcome to the Add Numbers Program!")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = add_numbers(num1, num2)

        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Please enter valid numbers.")