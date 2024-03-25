#importing the random module 
import random
#Generate a random number between 1 to 10
secret_number = random.randint(1, 10)
#maximum attempt allowed
max_attempt = 3
#function to display a welcome message
def welcome_message():
          print("\nWelcome to the Number Guessing Game")
          print(f"You have {max_attempt} attempts to guess the correct number ")
#Function for the recursion guessing
def guess_recursive(attempt_left):
          #get user input
          guess = int(input("\nGuess the number 1 to 10: "))
          #check the if guess is correct
          if guess == secret_number:
                    print("Congratulation You guessed the correct number")
          else:
                    print(f"Wrong guess. Attempt left: {attempt_left - 1}")
                    if attempt_left >1:
                              guess_recursive(attempt_left - 1)
                    else:
                              print(f"Sorry, You count't guess the number. The correct numb is {secret_number}")
welcome_message()
guess_recursive(max_attempt)
#print(f"memory address of secret number {secret_number} is {id(secret_number)})")