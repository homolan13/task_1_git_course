# This is a simple calculator program.

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

# Task 1: Implement a function for Exponentiation operation, similar to the existing functions above.
# Task 2: Create an interactive user input for the calculator, allowing the user to pick an operation and input numbers.

x = int(input('what is your first number'))
y = int(input('what is your second number'))

operation = input('Write the operation to perform: add, subtract, multipy, divide')

if operation == 'add':
   print(add(x,y))
elif operation == 'subtract':
   print(subtract(x,y))
elif operation == 'multiply':
   print(multiply(x,y))
elif operation == 'divide':
   print(divide(x,y))