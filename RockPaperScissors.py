from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    print("Rock, Paper, Scissors ?\n")
    player = input()
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player,"\n")
        else:
            print("You win!", player, "smashes", computer,"\n")
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player,"\n")
        else:
            print("You win!", player, "covers", computer,"\n")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player,"\n")
        else:
            print("You win!", player, "cut", computer,"\n")
    else:
        print("That's not a valid play. Check your spelling!","\n")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]