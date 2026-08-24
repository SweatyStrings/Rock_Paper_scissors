import random
print("enter 'y' to play and 'n' to stop the game")
i=input()
if i == "n":
 exit(0)
def game():
    player=input("please enter your choice(rock,paper,scissors):\n ")
    cchoice=["rock","paper","scissors"]
    computer=random.choice(cchoice)
    choice ={"player1":player,"computer1":computer}
    return choice

def result(player,computer):
    print(f"you chose {player}, the computer chose {computer}")
    if player == computer:
        return "it is a tie"
    elif player == "rock":
        if computer == "paper":
            return "you lose"
        else:
            return "you win"
    elif player == "paper":
            if computer == "scissors":
                return "you lose"
            else:
                return "you win"
    elif player == "scissors":
            if computer == "rock":
                return "you lose"
            else:
                return "you win"

while i != 'n':
    games=game()
    results=result(games["player1"],games["computer1"])
    print(results)
    print("input 'y' to play the game and 'n' to stop the game")
    i=input()