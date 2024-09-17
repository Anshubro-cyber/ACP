class Operation:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def add(self):
        return self.operand1 + self.operand2

    def subtract(self):
        return self.operand1 - self.operand2

    def multiply(self):
        return self.operand1 * self.operand2

    def divide(self):
        if self.operand2 == 0:
            raise ValueError("Cannot divide by zero.")
        return self.operand1 / self.operand2

class Expression:
    def __init__(self, operand1, operand2, operator):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator
        self.operation = Operation(operand1, operand2)

    def evaluate(self):
        if self.operator == '+':
            return self.operation.add()
        elif self.operator == '-':
            return self.operation.subtract()
        elif self.operator == '*':
            return self.operation.multiply()
        elif self.operator == '/':
            return self.operation.divide()
        else:
            raise ValueError("Unsupported operator. Use +, -, *, or /.")

def main():
    # Example usage
    operand1 = float(input("Enter the first operand: "))
    operand2 = float(input("Enter the second operand: "))
    operator = input("Enter the operator (+, -, *, /): ")

    expression = Expression(operand1, operand2, operator)
    try:
        result = expression.evaluate()
        print(f"The result of {operand1} {operator} {operand2} is: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()