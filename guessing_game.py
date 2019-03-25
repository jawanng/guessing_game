"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    top_score = 100
    play_again = 'y'
    while play_again.lower() == 'y':
      print("Welcome to the Number Guessing game")
      if top_score != 100:
        print("The current best score is {}.".format(top_score))
      target = random.randint(1,11)
      attempts = 1
      while 1:
        try:
          guess = int(input("Please guess a number:  "))
          if guess < 1 or guess > 10:
            raise ValueError
        except ValueError:
          print("Plese enter in a valid number between 1 and 10 inclusive")
        else:
          if guess > target:
            print("It's lower")
          elif guess < target:
            print("It's higher")
          else:
            print("Got it")
            print("It took you {} attempts".format(attempts))
            print("This round is now over")
            if attempts < top_score:
              top_score = attempts
            break
          attempts += 1
      play_again = input("Would you like to play again Y/N?  ")
      while play_again.lower() != 'y' and play_again.lower() != 'n':
        play_again = input("Invalid input.  Enter Y or N:  ")
   


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
