import random

def get_max_number():
    while True:
        try:
            n = int(input("Select the maximum value of the desired number(min 20): "))
            if n < 20:
                print("Error. the minimum value for the maximum value is 20")
                continue
            else:
                return n
        except ValueError:
            print("Error! you have not entered an integer")

def guess_number(n, random_num):
    while True:
        try:
            choice = int(input(f"Try to guess number (from 1 to {n}): "))
            if choice < random_num:
                print(f"The guessed number is greater than {choice}")
            elif choice > random_num:
                print(f"The guessed number is less than {choice}")
            else:
                print(f"You Win! Guessed number is {random_num}")
                break
        except ValueError:
            print("Error! you have not entered an integer")

def main():
    n = get_max_number()
    random_num = random.randint(1, n)
    guess_number(n, random_num)

if __name__ == "__main__":
    main()