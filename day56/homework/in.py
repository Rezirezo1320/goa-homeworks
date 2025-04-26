# 29) Access a specific element from the list
numbers = [10, 20, 30, 40, 50]
print("29) Second element:", numbers[1])  # Output: 20

# 30) Add an element to the list
items = ['apple', 'banana', 'cherry']
items.append('date')
print("30) Updated list:", items)  # Output: ['apple', 'banana', 'cherry', 'date']

# 31) Remove an element from the list
fruits = ['apple', 'banana', 'cherry', 'date']
fruits.remove('banana')
print("31) After removal:", fruits)  # Output: ['apple', 'cherry', 'date']

# 32) Create a list of squares
squares = [x**2 for x in range(1, 6)]
print("32) Squares:", squares)  # Output: [1, 4, 9, 16, 25]

# 33) Create a list of even numbers
evens = [x for x in range(2, 11) if x % 2 == 0]
print("33) Even numbers:", evens)  # Output: [2, 4, 6, 8, 10]

# 34) Filter odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7]
odds = [x for x in numbers if x % 2 != 0]
print("34) Odd numbers:", odds)  # Output: [1, 3, 5, 7]

# 35) Convert a list of strings to uppercase
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
print("35) Uppercase words:", upper_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# 36) Create a list of numbers squared if they are divisible by 2
numbers = [1, 2, 3, 4, 5, 6]
squared_evens = [x**2 for x in numbers if x % 2 == 0]
print("36) Squares of evens:", squared_evens)  # Output: [4, 16, 36]

# 37) Function to greet a user
def greet(name):
    print(f"37) Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
