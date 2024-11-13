import re

try:
    with open('testfile.txt', 'r') as f:
        read = f.read()

    del_symbols = re.sub(r'[.,:;?]', '', read)
    words = del_symbols.split()
    words_length = len(words)

    print(f"Words: {words_length}")
    chars = len(del_symbols)
    print(f"Characters: {chars}")

    with open('testfile.txt', 'w') as f_2:
        f_2.write(del_symbols)

except FileNotFoundError:
    print("File not found")