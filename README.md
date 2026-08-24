# Rock Paper Scissors Game 🎮

A simple **Rock, Paper, Scissors** game written in Python. The player plays against the computer, which randomly chooses rock, paper, or scissors.

## Features

* Play Rock, Paper, Scissors against the computer.
* The computer makes a random choice.
* Displays both the player's and computer's choices.
* Determines whether the player wins, loses, or ties.
* Allows the player to play multiple rounds.
* The game can be stopped at any time.

## Requirements

* Python 3.x
* No external libraries are required. The program uses Python's built-in `random` module.

## How to Run

1. Make sure Python is installed on your computer.
2. Save the code in a file, for example:

```text
rock_paper_scissors.py
```

3. Open a terminal in the directory containing the file.
4. Run:

```bash
python rock_paper_scissors.py
```

## How to Play

When the program starts, enter:

```text
y
```

to play or:

```text
n
```

to exit.

During the game, enter one of the following choices:

```text
rock
paper
scissors
```

The computer will randomly select one of the three choices.

### Game Rules

* Rock beats Scissors
* Scissors beats Paper
* Paper beats Rock
* The same choices result in a tie

For example:

```text
please enter your choice(rock,paper,scissors):
rock

you chose rock, the computer chose scissors
you win
```

After each round, you can choose whether to play again:

```text
input 'y' to play the game and 'n' to stop the game
```

## Code Overview

### `game()`

The `game()` function:

* Gets the player's choice.
* Creates a list of possible computer choices.
* Randomly selects the computer's choice.
* Returns both choices in a dictionary.

### `result(player, computer)`

The `result()` function compares the player's choice with the computer's choice and returns:

* `you win`
* `you lose`
* `it is a tie`

### Main Game Loop

The `while` loop allows the game to continue until the player enters `n`.

## Possible Improvements

Some improvements that could be added in the future:

* Validate user input so invalid choices are rejected.
* Keep track of the player's score and computer's score.
* Add a best-of-three or best-of-five mode.
* Make input case-insensitive (`Rock`, `ROCK`, and `rock`).
* Add a replay option after each round.
* Improve the user interface with colors or ASCII art.

## License

This project is free to use and modify for learning and educational purposes.
