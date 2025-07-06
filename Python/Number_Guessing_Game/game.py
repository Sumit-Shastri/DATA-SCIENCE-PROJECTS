import random

def scoreBoard2P(player1, player2, player1Points, player2Points, round_num):
    print("\n--------- Scoreboard ---------")
    print(f"Round: {round_num}")
    print(f"{player1}: {player1Points} point(s)")
    print(f"{player2}: {player2Points} point(s)")
    print("-------------------------------\n")

def input2P():
    while True:
        player1 = input("Enter Player 1 Name (type '0' for Computer): ")
        player2 = input("Enter Plyer 2 Name (type '0' for Computer): ")

        if player1 == '0' and player2 == '0':
            print("Both players cannot be computers. Try again.\n")
            continue

        if player1 == '0':
            player1 = 'Computer'
        if player2 == '0':
            player2 = 'Computer'

        return player1, player2

def getGuesses(player1, player2):
    if player1 == 'Computer':
        player1Guess = random.randint(0, 100)
        print(f"{player1}'s Guess: {player1Guess}")
    else:
        player1Guess = int(input(f"{player1}'s Guess (0-100): "))

    if player2 == 'Computer':
        player2Guess = random.randint(0, 100)
        print(f"{player2}'s Guess: {player2Guess}")
    else:
        player2Guess = int(input(f"{player2}'s Guess (0-100): "))

    return player1Guess, player2Guess

def twoPlayer():
    print("\n*** Two Player Mode Selected ***\n")
    print("Note: Type '0' to set a player as Computer.")
    player1, player2 = input2P()

    rounds = int(input("\nHow many rounds do you want to play? "))
    player1Points = 0
    player2Points = 0

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")
        secret_number = random.randint(0, 100)

        player1Guess, player2Guess = getGuesses(player1, player2)

        print(f"\n The number was: {secret_number}")

        diff1 = abs(secret_number - player1Guess)
        diff2 = abs(secret_number - player2Guess)

        if diff1 < diff2:
            player1Points += 1
            print(f"{player1} was closer!")
        elif diff2 < diff1:
            player2Points += 1
            print(f" {player2} was closer!")
        else:
            print(" It's a tie! No points.")

        scoreBoard2P(player1, player2, player1Points, player2Points, round_num)

    print("\n=== Final Results ===")
    if player1Points > player2Points:
        print(f" {player1} wins the game!")
    elif player2Points > player1Points:
        print(f"{player2} wins the game!")
    else:
        print("It's a tie overall!")

def threePlayer():
    print("\n Three Player Mode is under development. Coming soon!")

def gameMode():
    while True:
        try:
            game_mode = int(input("Enter Mode Number (1 for 2 Players, 2 for 3 Players): "))
            if game_mode == 1:
                twoPlayer()
                break
            elif game_mode == 2:
                threePlayer()
                break
            else:
                print(" Invalid mode. Enter 1 or 2.\n")
        except ValueError:
            print(" Please enter a number (1 or 2).\n")

def main():
    print("\n Welcome to The NumGuess Game!")
    print("Up to 3 players can play (including Computer).\n")
    print("Select Mode:\n1. 2-Players\n2. 3-Players\n")
    gameMode()

main()
