
import random

def game():
    player = input("Please enter your choice (rock, paper, scissors):\n")
    cchoice = ["rock", "paper", "scissors"]
    computer = random.choice(cchoice)
    choice = {"player1": player, "computer1": computer}
    return choice

def result(player, computer):
    print(f"You chose {player}, the computer chose {computer}")

    if player == computer:
        return "It is a tie"
    elif player == "rock":
        if computer == "paper":
            return "You lose"
        else:
            return "You win"
    elif player == "paper":
        if computer == "scissors":
            return "You lose"
        else:
            return "You win"
    elif player == "scissors":
        if computer == "rock":
            return "You lose"
        else:
            return "You win"

print("Enter 'y' to play and 'n' to stop the game")

while True:
    i = input("Do you want to play? (y/n): ").lower()

    if i == "n":
        print("Thanks for playing!")
        break
    elif i == "y":
        games = game()
        results = result(games["player1"], games["computer1"])
        print(results)
    else:
        print("Please enter 'y' or 'n'.")
