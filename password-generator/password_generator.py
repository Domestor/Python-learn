import random
import string


letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
all_characters = letters + digits + punctuation

MAX_LENGTH = 45
MIN_LENGTH = 5

try:
    length = int(input("Select password length ({MIN_LENGTH} - {MAX_LENGTH}): "))

    if length < MIN_LENGTH or length > MAX_LENGTH:
        print(f"Invalid length. Please enter a length between {MIN_LENGTH} and {MAX_LENGTH}")
    else:
        random_password = ''.join(random.choices(all_characters, k=length))
        print(f"Generated password: {random_password}")
except ValueError:
    print("Please enter an integer")