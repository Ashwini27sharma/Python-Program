import random

class ArithmeticOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.operation = random.choice(["+", "-", "*", "/"])
        self.result = None
        self.perform_operation()

    def perform_operation(self):
        if self.operation == "+":
            self.result = self.a + self.b
        elif self.operation == "-":
            self.result = self.a - self.b
        elif self.operation == "*":
            self.result = self.a * self.b
        elif self.operation == "/":
            self.result = self.a / self.b if self.b != 0 else "Undefined (division by zero)"

    def print_result(self):
        print(f"Operation: {self.a} {self.operation} {self.b}")
        print(f"Result: {self.result}")


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

calc = ArithmeticOperation(x, y)
calc.print_result()
