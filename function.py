def greet(name):
    print("hello, " , name)
    print("welcome to my program")

greet ("alice")
greet ("hunter")
greet ("simplicity")


def add_numbers(a, b):
    result = a + b
    return result

answer = add_numbers(5, 3)
print("5 + 3 =", answer)

def make_full_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name

name = make_full_name("lost", "hunter")
print("full name:", name)


