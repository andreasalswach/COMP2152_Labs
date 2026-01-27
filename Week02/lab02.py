import random

# Defining an array with 3 game options: Rock, Paper, Scissors
choices = ["Rock", "Paper", "Scissors"]

# Asking player to enter their choice and storing the input in a variable
playerChoice = input ("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")

# Type conversion - converting the string to an integer
playerChoice = int(playerChoice)

# Error Handling
# Checking if the player's choice is valid within the range of 1 to 3
# if not valid print out error message3

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3.")
else:
    computerChoice = random.randint(1, 3) # Generating a random choice for the computer between 1 and 3

    playerChoice = choices[playerChoice - 1] # Indexing the choices array to get the player's choice string
    computerChoice = choices[computerChoice - 1] # Indexing the choices array to get the computer's choice string

    print("You chose: ", playerChoice) 
    print("Computer chose: ", computerChoice) 

    # Nested If Statement to determine the winner using if/elif/else
    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice == 0 and computerChoice == 2:
        print("Rock beats scissors - You win!")
    elif playerChoice == 1 and computerChoice == 0:
        print("Paper beats Rock - You win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Scissors beats paper - You win!")
    else:
        print("You lose!")
        







