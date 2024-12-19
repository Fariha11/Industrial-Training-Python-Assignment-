# main.py
from math_operations import add_numbers
from string_operations import reverse_string

# Using the math_operations module
num1 = 8
num2 = 12
print(f"The sum of {num1} and {num2} is: {add_numbers(num1, num2)}")

# Using the string_operations module
text = "World"
print(f"The reverse of '{text}' is: '{reverse_string(text)}'")
