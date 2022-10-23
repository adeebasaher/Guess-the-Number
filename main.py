#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
#from replit import clear
import random
from art import logo
print(logo)

def easy_level():
  guesses = 9
  while guesses >= 0:
    user_guess = int(input("Type in your guess. "))
    if user_guess > chosen_number:
      print(f"Too high. \nGuess again.\nYou have {guesses} left.")
    elif user_guess < chosen_number:
      print(f"Too low.\nGuess again.\nYou have {guesses} left.")
    else:
      print("Congratulations! you guessed it right")
      break
    
    if guesses == 0:
      print("You're out of guesses. You lost")

    guesses -= 1

def hard_level():
  guesses = 4
  while guesses >= 0:
    user_guess = int(input("Type in your guess. "))
    if user_guess > chosen_number:
      print(f"Too high. \nGuess again.\nYou have {guesses} left.")
    elif user_guess < chosen_number:
      print(f"Too low.\nGuess again.\nYou have {guesses} left.")
    else:
      print("Congratulations! you guessed it right")
      break
    
    if guesses == 0:
      print("You're out of guesses. You lost")

    guesses -= 1
  

#clear()
print("Welcome to the number guessing game!!")

chosen_number = random.choice(range(1,101))

difficulty_level = input("Choose your difficulty level. Easy or hard.\n").lower()
if difficulty_level == "easy":
  easy_level()
elif difficulty_level == "hard":
  hard_level()
else:
  print("Invalid input")