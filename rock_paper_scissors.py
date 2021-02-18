import random

user_input = input("rock, paper or scissors? ").lower()

def user_choice():

    if (user_input == 'rock' or user_input == 'paper' or user_input == 'scissors'):
        return user_input
    else:
        print("Please enter rock paper or scissors!")

def ai_choice(ai_input = random.randint(0,2)):
    return {0:'rock',
    1:'paper',
    2: 'scissors'}.get(ai_input)

ai_rps_choices = ['rock', 'paper','scissors']
ai_random_choice = random.choice(ai_rps_choices)

user_choice()
ai_input = ai_choice()

def battle():
    if (user_input == "rock"):
        if (ai_input == 'rock'):
            print("You chose rock \nAI chose rock. \nYou tied.")
        elif (ai_input == 'paper'):
            print("You chose rock \nAI chose paper. \nAI Won.")
        elif (ai_input == 'scissors'):
            print("You chose rock \nAI chose scissors. \nYou Won.")
    elif (user_input == 'paper'):
        if (ai_input == 'paper'):
            print("You chose paper \nAI chose paper. \nYou tied.")
        elif (ai_input == 'rock'):
            print("You chose paper \nAI chose rock. \nYou Won.")
        elif (ai_input == 'scissors'):
            print("You chose paper \nAI chose scissors. \nAI Won.")
    elif (user_input == 'scissors'):
        if (ai_input == 'scissors'):
            print("You chose scissors \nAI chose scissors. \nYou tied.")
        elif (ai_input == 'paper'):
            print("You chose scissors \nAI chose paper. \nYou Won.")
        elif (ai_input == 'rock'):
            print("You chose scissors \nAI chose rock. \nAI Won.")
    else:
        print('please print rock paper or scissors!')

battle()