# Define a function: Calculate the product of three numbers
#Author: Tan Zihao
def multiply_three_nums(a, b, c):
    return a * b * c

# Test the program
if __name__ == "__main__":
    # Input three numbers (example: you can modify the values to test)
    num1 = 2
    num2 = 3
    num3 = 4
    # Call the function to calculate the product
    result = multiply_three_nums(num1, num2, num3)
    # Output the result
    print(f"The product of the three numbers {num1}, {num2}, {num3} is: {result}")
