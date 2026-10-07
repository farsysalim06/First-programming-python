# week 1 task
# maths quiz

# function 1: get information from the user

def get_user_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

# function 2: ask a question using a loop and if statement

def ask_question():
    score = 0
    tries = 0

    while tries < 3:
        answer = int(input("What is 5 + 5? "))

        if answer == 10:
            print("Correct!")
            score = 1
            break
        else:
            print("Wrong, try again.")
            tries += 1

    return score, tries


def show_result(name, age, score, tries):
    print("Name:", name)
    print("Age:", age)
    print("Score:", score)
    print("Tries:", tries)

    if score == 1:
        print("Great job!")
    else:
        print("Good luck next time!")


def main():
    user_name, user_age = get_user_info()
    final_score, final_tries = ask_question()
    show_result(user_name, user_age, final_score, final_tries)


main()










