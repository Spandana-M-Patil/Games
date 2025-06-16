# Number Guessing Game

Welcome to the Number Guessing Game! This is a simple Python game where you have to guess a randomly chosen number within a specified range. You have only 5 chances to guess the correct number. Good luck!

## Features

- Allows the user to set the lower and upper bounds for the random number.
- Provides feedback on each guess (too high or too low).
- Plays congratulatory music if the guess is correct.
- Plays a buzzer sound if the guess is incorrect.
- Uses the `colorama` library for colored text in the terminal.
- Uses the `pygame` library for playing sounds.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- `colorama` library
- `pygame` library

You can install the required libraries using pip:
```bash
pip install colorama pygame
```
## How to Run
1. Clone the repository
```bash
git clone https://github.com/Spandana-M-Patil/Guessing-Game.git
```
2. Ensure you have the congs.mp3 and buzz.mp3 files in the same directory as the script.
3. Run the script:
```bash
python GuessingGame.py
```
## How to play
1. Enter the lower and upper bounds for the number range.
2. Try to guess the randomly chosen number within the given range.
3. You have 5 chances to guess the correct number.
4. If your guess is correct, you will hear a congratulatory sound and see a success message.
5. If your guess is incorrect, you will hear a buzzer sound and get feedback to adjust your next guess.

## Example
```bash
Welcome!! Guessing number game!
Enter lower bound: 1
Enter higher bound: 10
Note: You have only 5 chances to guess. All the best!!
Guess a number: 5
Try again! You guessed too small.
Guess a number: 8
Try again! You guessed too large.
Guess a number: 7
Excellent!!
Congratulations! You did it in 3 tries.
```
