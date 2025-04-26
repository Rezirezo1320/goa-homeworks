try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    if denominator == 0:
        raise ValueError("Division by zero is not allowed!")
    result = numerator / denominator
    print(f"Result: {result}")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception:
    print("Please enter valid numbers.")
finally:
    print("Operation complete.")





def apply_to_list(func, values):
    return [func(x) for x in values]
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_to_list(square, numbers)

print(squared_numbers)
