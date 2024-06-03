# Rock, Paper, Scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# User Input
player_pick = input("ROCK, PAPER, or SCISSORS: ")
#print(f"You picked {player_pick.upper()}")

game = ["ROCK", "PAPER", "SCISSORS"]
num_game = len(game)
rand_game = random.randint(0, num_game - 1)

# Test to show computer rand picked value
#print(f"Computer picked {game[rand_game]}")

# Other Test to print computer rand picked value
#print(game[rand_game])

# Test to print user picked value
#print(player_pick)


if(f"{player_pick.upper()}" == f"{game[rand_game]}"):                               # First If to test for Tie Games
    if(f"{player_pick.upper()}" == "ROCK" and f"{game[rand_game]}" == "ROCK"):      # First Nested If to test for ROCK against ROCK     
        print(f"You picked {player_pick.upper()}")
        print(rock)
        print(f"Computer picked {game[rand_game]}")
        print(rock)
        print("====================")
        print("TIE GAME")
        print("====================")
    elif(f"{player_pick.upper()}" == "PAPER" and f"{game[rand_game]}" == "PAPER"):      # Second Nested If to test for PAPER against PAPER
        print(f"You picked {player_pick.upper()}")
        print(paper)
        print(f"Computer picked {game[rand_game]}")
        print(paper)
        print("====================")
        print("TIE GAME")
        print("====================")
    elif(f"{player_pick.upper()}" == "SCISSORS" and f"{game[rand_game]}" == "SCISSORS"):       # Final Nested If to test for SCISSORS against SCISSORS
        print(f"You picked {player_pick.upper()}")
        print(scissors)
        print(f"Computer picked {game[rand_game]}")
        print(scissors)
        print("====================")
        print("TIE GAME")
        print("====================")
    else:
        print("ERROR: TRY AGAIN")
elif(f"{player_pick.upper()}" == "ROCK" and f"{game[rand_game]}" == "PAPER"):       # First elif to test for ROCK against PAPER
    print(f"You picked {player_pick.upper()}")
    print(rock)
    print(f"Computer picked {game[rand_game]}")
    print(paper)
    print("====================")
    print("YOU LOSE!")
    print("====================")
elif(f"{player_pick.upper()}" == "ROCK" and f"{game[rand_game]}" == "SCISSORS"):       # Second elif to test for ROCK against SCISSORS
    print(f"You picked {player_pick.upper()}")
    print(rock)
    print(f"Computer picked {game[rand_game]}")
    print(scissors)
    print("====================")
    print("YOU WIN!")
    print("====================")
elif(f"{player_pick.upper()}" == "PAPER" and f"{game[rand_game]}" == "SCISSORS"):       # Third elif to test for PAPER against SCISSORS
    print(f"You picked {player_pick.upper()}")
    print(paper)
    print(f"Computer picked {game[rand_game]}")
    print(scissors)
    print("====================")
    print("YOU LOSE!")
    print("====================")
elif(f"{player_pick.upper()}" == "PAPER" and f"{game[rand_game]}" == "ROCK"):       # Fourth elif to test for PAPER against ROCK
    print(f"You picked {player_pick.upper()}")
    print(paper)
    print(f"Computer picked {game[rand_game]}")
    print(rock)
    print("====================")
    print("YOU WIN!")
    print("====================")
elif(f"{player_pick.upper()}" == "SCISSORS" and f"{game[rand_game]}" == "ROCK"):       # Fifth elif to test for SCISSORS against ROCK
    print(f"You picked {player_pick.upper()}")
    print(scissors)
    print(f"Computer picked {game[rand_game]}")
    print(rock)
    print("====================")
    print("YOU LOSE!")
    print("====================")
elif(f"{player_pick.upper()}" == "SCISSORS" and f"{game[rand_game]}" == "PAPER"):       # Final elif to test for SCISSORS against PAPER
    print(f"You picked {player_pick.upper()}")
    print(scissors)
    print(f"Computer picked {game[rand_game]}")
    print(paper)
    print("====================")
    print("YOU WIN!")
    print("====================")
else:
    print("ERROR: TRY AGAIN.")



