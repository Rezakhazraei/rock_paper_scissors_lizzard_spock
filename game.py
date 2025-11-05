# This should be the output for this game.
#================================
#Rock Paper Scissors Lizard Spock
#================================

#1) ✊
#2) ✋
#3) ✌️
#4) 🦎
#5) 🖖
#Pick a number: 3

#You chose: ✌️
#CPU chose: ✌️
#It's a tie!

import random

print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================")

choices = {
    1: "✊",  # Rock
    2: "✋",  # Paper
    3: "✌️",  # Scissors
    4: "🦎",  # Lizard
    5: "🖖"   # Spock}
}

print("#1) ✊")
print("#2) ✋")
print("#3) ✌️")
print("#4) 🦎")
print("#5) 🖖")

user_choice = int(input("Pick a number: "))

if user_choice not in choices:
    print("Invalid choice. Please pick a number between 1 and 5.")
    exit()

user_choice_text = choices[user_choice]
print(f"You chose: {user_choice_text}")

cpu_choice = random.randint(1, 5)
cpu_choice_text = choices[cpu_choice]
print(f"CPU chose: {cpu_choice_text}")

if user_choice == cpu_choice:
    print("It's a tie!")
else:
    winning_combinations = {
        1: [3, 4],  # Rock crushes Scissors and Lizard
        2: [1, 5],  # Paper covers Rock and disproves Spock
        3: [2, 4],  # Scissors cuts Paper and decapitates Lizard
        4: [2, 5],  # Lizard eats Paper and poisons Spock
        5: [1, 3]   # Spock vaporizes Rock and smashes Scissors
    }

    if cpu_choice in winning_combinations[user_choice]:
        print("You win!")
    else:
        print("CPU wins!")