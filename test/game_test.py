

from app.game import determine_winner

def test_determination_of_the_winner():
    assert determine_winner("rock", "rock") == None
    assert determine_winner("rock", "paper")  == "paper"
    assert determine_winner("rock", "scissors") == ""

    assert determine_winner("paper", "rock")
    assert determine_winner("paper", "paper")
    assert determine_winner("paper", "scissors")

    assert determine_winner("scissors", "rock")
    assert determine_winner("scissors", "paper")
    assert determine_winner("scissors", "scissors")













