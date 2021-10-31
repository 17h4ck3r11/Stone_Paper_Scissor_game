import random

ai = ["stone", "paper", "scissor"]

print("/*RULES FOR THE GAME*/")
print("You have 3 chances.")
print("You Score will show at the end of the game")
print("Enter the key for corresponding choice :\n\t1. s --> stone\n\t2. p --> paper\n\t3. sc --> scissor")

lose = 1
score = 0

while True:

    if lose == 3:
        break

    ai_choice = ai[random.randint(0, 2)]
    user_choice = input("Enter your choice : ")
    print()

    if ai_choice == 'stone':

        if user_choice == 's':
            print("Computer choice : Stone\nYour choice : Stone\nMatch Draw!!")

        elif user_choice == 'sc':
            print("Computer choice : Stone\nYour choice : Scissor\nComputer Wins!!")
            lose += 1

        elif user_choice == 'p':
            print("Computer choice : Stone\nYour choice : Paper\nYou Wins!!")
            score += 10

        else:
            print("Invalid choice")

    elif ai_choice == 'paper':

        if user_choice == 's':
            print("Computer choice : Paper\nYour choice : Stone\nComputer Wins!!")
            lose += 1

        elif user_choice == 'sc':
            print("Computer choice : Paper\nYour choice : Scissor\nYou Wins!!")
            score += 10

        elif user_choice == 'p':
            print("Computer choice : Paper\nYour choice : Paper\nMatch Draw!!")

        else:
            print("Invalid choice")

    else:

        if user_choice == 's':
            print("Computer choice : Scissor\nYour choice : Stone\nYou Wins!!")
            score += 10

        elif user_choice == 'sc':
            print("Computer choice : Scissor\nYour choice : Scissor\nMatch Draw!!")

        elif user_choice == 'p':
            print("Computer choice : Scissor\nYour choice : Paper\nComputer Wins!!")
            score += 10

        else:
            print("Invalid choice")

    print()

print("Total Score :", score)
