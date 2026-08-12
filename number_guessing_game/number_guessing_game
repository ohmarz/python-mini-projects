import random

import time

print("-----"*20)
print()
print("===== ===== ===== ===== ===== ===== 🔢NUMBER GUESSING GAME🔢 ===== ===== ===== ===== ===== ===== ===")


print()
def number(total_guesses):
    num = random.randint(1,100)
    round_guesses = 0

    while True:
        guess = input("Guess a number between 1 and 100 (q to quit)🔢: ").lower()

        if guess == "q":
            return total_guesses, round_guesses, num

        round_guesses += 1
        total_guesses += 1

        try:
            guess_int = int(guess)
        except ValueError:
            time.sleep(0.3)
            print("*****"*20)
            print("Please enter a NUMBER!🔢")
            continue
        if guess_int == num:
            time.sleep(0.5)
            print()
            print("*****" * 20)
            print("CORRECT!🎯✔️")
            print("*****" * 20)
            break
        elif guess_int > num:
            print("WRONG❌!")
            time.sleep(0.3)
            print("Too high⬆️")
        else:
            print("WRONG❌!")
            time.sleep(0.3)
            print("Too low⬇️")
    return total_guesses, round_guesses, num


# this built-in Python variable allows to run the code directly
if __name__ == "__main__":
    total_guesses = 0
    while True:
        total_guesses, round_count, target_num = number(total_guesses)
        time.sleep(1)
        print()
        print("*****" * 20)
        print(f"This round has {round_count} guesses, the target number was {target_num}")
        print("*****" * 20)

        time.sleep(0.5)
        print()
        play_again = input("Do you want to play again? (y/n)🥲: ").strip().lower()
        if play_again != "y":
            time.sleep(1)
            print()
            print("*****" * 20)
            time.sleep(0.5)
            print(f"Total guesses for all rounds: {total_guesses}🥳")
            print("THANK YOU FOR PLAYING!🥰")
            print("*****" * 20)
            time.sleep(1)
            break
