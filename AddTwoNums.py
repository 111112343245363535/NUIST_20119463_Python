# Python program to add two numbers
# Author: Tan Zihao
# Using function
# Define a function to add two numbers
def add(a, b):
    # Convert to float and add
    result = float(a) + float(b)
    return result

# Get user input
a = input("First number: ")
b = input("Second number: ")
# Call the function
res = add(a, b)
print("The result is: ")
print(res)
