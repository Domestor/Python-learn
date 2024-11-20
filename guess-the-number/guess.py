import random

def set_max_attempts(n):
    if n > 100:
        print("You have 5 attempts to guess!")
        return 5
    else:
        print("You have 3 attempts to guess!")
        return 3

def get_max_value():
    while True:
        try:
            n = int(input("Select the maximum value of the desired number(20 - 500): "))
            if n < 20:
                print("Error. the minimum value for the maximum value is 20")
                continue
            elif n > 500:
                print("The maximum value is 500. Adjusting to 500")
                print('')
                n = 500
            else:
                max_attempts = set_max_attempts(n)
                return n, max_attempts
        except ValueError:
            print("Error! you have not entered an integer")


def guess_number(n, random_num, max_attempts):
    attempts = 0

    while attempts < max_attempts:
        try:
            choice = int(input(f"Try to guess number (from 1 to {n}): "))
            attempts += 1
            if choice < random_num:
                print(f"The guessed number is greater than {choice}")
            elif choice > random_num:
                print(f"The guessed number is less than {choice}")
            else:
                print(f"You Win! Guessed number is {random_num}")
                break
        except ValueError:
            print("Error! you have not entered an integer")

    if attempts == max_attempts:
        print('')
        print(f"Game Over! You didn't guess the number. The correct number was: {random_num}.")
def main():
    n, max_attempts = get_max_value()
    random_num = random.randint(1, n)
    guess_number(n, random_num, max_attempts)

if __name__ == "__main__":
    main()