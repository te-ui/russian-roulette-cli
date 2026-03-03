import random

def spin():
    chambers = ["No bullet"] * 5 + ["Bullet hit"]
    return random.choice(chambers)

def game():
    print("=== Russian Roulette 2-Player Game ===\n")
    
    player1 = input("Enter Player 1 name: ")
    player2 = input("Enter Player 2 name: ")
    players = [player1, player2]
    turn = 0

    print("\nPress Enter to spin,bro. Type 'q' to quit.\n")
    
    while True:
        current_player = players[turn % 2]
        user_input = input(f"{current_player}'s turn: ")

        if user_input.lower() == "q":
            print("Game exited.")
            break

        result = spin()
        print(result)

        if result == "Bullet hit":
            print(f"\n💥 {current_player} got hit! Game Over.")
            break
        else:
            print(f"{current_player} survives!\n")

        turn += 1

if __name__ == "__main__":
    game()

