from random import randint

player_wins = 0
computer_wins = 0
winning_score = 2

print(f"Let's play the game. The Winning score is {winning_score}")

while ((player_wins < winning_score) and (computer_wins < winning_score)):
    print(f"\nCurrent Score of Player : {player_wins}")
    print(f"Current Score of Computer : {computer_wins}\n")
    print("Give your best shot this time Player!")
    print("Important Note: Quit game anytime by entering `q` or `quit`\n")
    print('Available options: `rock`, `paper`, or scissors')
    player = input("Player, make your move: ").lower()
    if (player == 'quit' or player == 'q'):
        break

    random_number = randint(0,2)

    if (random_number == 0):
        computer = "rock"
    elif (random_number == 1):
        computer = "paper"
    elif (random_number == 2):
        computer = "scissors"
    else:
        print('Something wrong happened')

    print(f"\nYou played {player}")
    print(f"Computer plays {computer}" ) 

    if (player == computer):
        print("It's a tie!")
    elif (player == "rock"):
        if (computer == "scissors"):
            player_wins += 1
            print("Player wins!")
        elif (computer == "paper"):
            computer_wins += 1
            print("Computer wins!")
        else:
            print('Something wrong happened')
    elif (player == "paper"):
        if (computer == "rock"):
            player_wins += 1
            print("Player wins!")
        elif (computer == "scissors"):
            computer_wins += 1
            print("Computer wins!")
        else:
            print('Something wrong happened')
    elif (player == "scissors"):
        if (computer == "paper"):
            player_wins += 1
            print("Player wins!")
        elif (computer == "rock"):
            computer_wins += 1
            print("Computer wins!")	
        else:
            print('Something wrong happened')
    else:
        print("Please enter a valid move!")

if (player_wins > computer_wins):
    print('\nCongratulations Player for winning the game')
elif (computer_wins > player_wins):
    print('\nCongratulations Computer for winning the game')
elif (computer_wins == player_wins):
    print('\nThe overall game is a tie')
else:
    print('Something wrong happened')

print(f"\nFinal Score of Player : {player_wins}")
print(f"Final Score of Computer : {computer_wins}\n")
