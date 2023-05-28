
print("Welcome to today's game. You will be going against an AI!")
print("First, the AI will ask you a question, and then you will answer!")
print("Are you ready?")

user_name = input("Enter name: ").title().strip()
print("Welcome,", user_name)

user_choice = input("Name a green fruit: ").capitalize()
ai_options = ['Kiwi', 'Honeydew', 'Gooseberries']

while True:
    if user_choice not in ai_options:
        print("Sorry, your choice is not what the AI expected.")
        print("AI expectations are:", ai_options)
        print("2 lives left")
        break
    print("Correct! You think like an AI.")
    break

options_1 = ['y', 'n']

while True:
    user_final_choice = input("Still wanna play? ")
    if user_final_choice not in options_1:
        print("Invalid")
        continue

    if user_final_choice == 'y':
        print("Thanks for staying!")
        break

    if user_final_choice == 'n':
        print("Game over. Thanks for playing!")
        quit()

user_answer = input("Guess the length of the word you typed: ")
length = len(user_answer)
print("The length of the word is:", length)

guess = input("What is the meaning of CPU: ").title()
option = ['Central Processing Unit']

if guess not in option:
    print("Sorry, you choice is not what the AI expected")
    print("AI expectation is:", option)
    print("you have 1 live left")

else:
    print("Correct! you think like an AI")

print("AI has three list of fruit Guess at least one")
fruits = ['Apple', 'Banana', 'Orange']
user_live = input("Guess a fruit: ").capitalize()

if user_live in fruits:
    print("Correct! you think like an AI")
else:
    print("Sorry, you choice is not what the AI expected")
    print("AI expectation is:", fruits)
    print("your final live :(")

alpha = ['y', 'n']

while True:
    user_final = input("Still wanna play? ")
    if user_final not in alpha:
        print("Invalid")
        continue

    if user_final == 'y':
        print("Thanks for staying!")
        break

    elif user_final == 'n':
        print("Game over. Thanks for playing!")
    quit()