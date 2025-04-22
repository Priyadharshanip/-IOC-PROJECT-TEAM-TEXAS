def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

# Example usage
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))
divide_numbers(num1, num2)
