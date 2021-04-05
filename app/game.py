
from random import choice

choices = ["rock", "paper", "scissors"]

def determine_winner(choice1, choice2):
    """
    Will help to determine a winner of our game
    Params: choice1 and choice2 are both strings: one of "rock", "paper", or "scissors"
    """
    winners = {
        "rock":{
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }
    winning_choice = winners[choice1][choice2]
    return winning_choice


if __name__ == '__main__':
  
    # USER SELECTION
    u = input("Please choose either 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in choices:
        print("OOPS, TRY AGAIN")
        exit()

        
    # COMPUTER SELECTION
    c = choice(choices)
    print("COMPUTER CHOICE:", c)


    # DETERMINATION OF WINNER
    winner = determine_winner(u, c)
    if winner == u:
        print("YOU WON!")
    elif winner == c:
        print("COMPUTER WON!")
    elif winner == None:
        print("TIE!")

#   if u == c:
#       print("It's a tie!")
#   elif u == "rock" and c == "paper" or u == "paper" and c == "scissors" or u == "scissors" and c == "rock":
#       print("Sorry, the computer won.")
#   else:
#       print("Congrats, you win!")