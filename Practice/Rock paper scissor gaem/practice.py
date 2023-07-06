# Rock Paper Scissor Game
from random import randint
choices = ["rock", "paper", "scissor"]

# Rules

# 1, rock - paper -> paper win
# 2, rock - scissor -> rock win
# 3, paper - scissor -> scissor win


# Tasks

# Player inputs a choice
# System randomly select one
# If both select same option, then its a tie
# If its different then find find winner by the above rules

player=input("Select an option: ")
position=randint(0,2)
system=choices[position]

print(system)

if player == system:
    print("its a tie")
elif player == "rock":
    if system == "scissor":
        print("player win")
    elif system == "paper":
        print("system win")
elif player == "paper":
    if system == "rock":
        print("player win")
    elif system == "scissor":
        print("system win")
elif player == "scissor":
    if system == "paper":
        print("player win")
    elif system == "rock":
        print("system win")
else:
    print("Select a valid choice")



