maths = int(input("maths marks: "))
english = int(input("english marks: "))
operator = input("enter an operator ( + , - , * , / , % )")
if operator == "+":
    result = maths + english
elif operator == "-":
    result = maths - english
elif operator == "*":
    result = maths * english
elif operator == "/":
    result = maths / english
elif operator == "%":
    result = maths % english
else:
    print("Invalid operator")

print("Result:", result)