def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a* b
def divide(a, b):
    if b == 0:
        return "error:cannot divide by zero"
    return a / b
def get_operation():
    print("/nwhat operation do you want?")
    print("1. Add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    choice = input("enter 1, 2, 3, or 4: ")
    return choice
keep_going = True

while keep_going:
    #get numbers from user
    number1 = float(input("enter the first number: "))
    number2 = float(input("enter the second number"))
    #get operation from user
    operation = get_operation()
    #do the calculation
    if operation == "1":
        result = add(number1, number2)
    elif operation == "2":
        result = subtract(number1, number2)
    elif operation == "3":
        result = multiply(number1, number2)
    elif operation == "4":
       result = divide(number1, number2)
    else:
        result = "invalid choice"
    #show the result
    print("/nresult", result)

    #ask if they want to continue
    again = input("/ndo you want to do another calaculation? (yes or no): ")
    if again.lower() != "yes":
       keep_going = False

    print("thank you for using the calculator")


    