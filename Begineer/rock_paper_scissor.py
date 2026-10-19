import random

def get_choices():
    player_choice=input("Enter a choice(rock,paper,scissors):")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    print(f"You chose {player} and computer chose {computer}")
    if player==computer:
        return "It's a tie!"
    elif player=="rock" and computer=="scissors":
        return "Rock smashes scissors! You win!"
    elif player=="paper" and computer=="rock":
        return "Paper covers rock! You win!"
    elif player=="scissors" and computer=="paper":
        return "Scissors cuts paper! You win!"
    else:
        return "You lose!"
    return "You lose!"

choices=get_choices()
pchoice=choices["player"]
cchoice=choices["computer"]
result=check_win(pchoice,cchoice)
print(result)