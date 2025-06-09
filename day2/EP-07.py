# Input: Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Input: Ask the user for the operation they want to perform
operation = input("Choose an operation (+, -, *, /): ")

# Processing: Perform the selected operation
result = 0

if operation == "+":
    result = num1 + num2
elif operation == "-": 
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Check if the second number is not zero to avoid division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero.")
        exit()

# Output: Display the result
        #Result: 5+7 = 12
print(f"Result: {num1} {operation} {num2} = {result}")
