# rockPaperScissors.py

# Import the random module (random choices)
import random

# Initialize game variables (**starting with CONSTANTS**)
WIN_SCORE = 3
lstMoves = ["rock", "paper", "scissors"]
iPlayerScore = 0
iComputerScore = 0
iRound = 0

# Start the game loop (w/ a while loop - until WIN_SCORE is reached, game continues)
while iPlayerScore < WIN_SCORE and iComputerScore < WIN_SCORE:
    sPlayer = input("\nrock, paper, or scissors? ").lower()#.strip()
    # Validate the player's move
    if sPlayer not in lstMoves:
        print("Invalid move. Try again.")
        continue

    iRound += 1
    sComputer = random.choice(lstMoves)
    print(f"Round {iRound}: You chose {sPlayer}, computer chose {sComputer}.")

    # Determine the winner of the round (using if/else statements)
    if sPlayer == sComputer:
        print("Tie!")
    elif sPlayer == "rock" and sComputer == "scissors":
        print("You win this round!")
        iPlayerScore += 1
    elif sPlayer == "paper" and sComputer == "rock":
        print("You win this round!")
        iPlayerScore += 1
    elif sPlayer == "scissors" and sComputer == "paper":
        print("You win this round!")
        iPlayerScore += 1
    else:
        print("Computer wins this round!")
        iComputerScore += 1

    print(f"Score: You {iPlayerScore} - Computer {iComputerScore}")

# Determine winner & print the result
if iPlayerScore == WIN_SCORE:
    print(f"\nYou won the game in {iRound} rounds!")
else:
    print(f"\nThe computer won the game in {iRound} rounds.")
