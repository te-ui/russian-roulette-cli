import random

def spin():
    chambers = ["No bullet", "No bullet", "No bullet", "No bullet", "No bullet", "Bullet hit"]
    return random.choice(chambers)

def game():
    print("Russian Roulette Game")
    print("Press Enter to spin. Type 'q' to quit.\n")

    while True:
        user_input = input("Spin? ")

        if user_input.lower() == "q":
            print("Game exited.")
            break

        result = spin()
        print(result)

        if result == "Bullet hit":
            print("Game Over.")
            break

if __name__ == "__main__":
    game()