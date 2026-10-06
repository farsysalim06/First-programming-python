x = 5
y = 10
operator = input("Enter an operator (+, -, *, /): ")
if operator == "+":
    result = x + y
elif operator == "-":
    result = x - y
elif operator == "*":
    result = x * y
elif operator == "/":
    if y != 0:
        result = x / y
    else:
        result = "Error: Division by zero"
print(result)
