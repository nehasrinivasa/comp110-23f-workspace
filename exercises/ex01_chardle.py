"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730675654"

secret_word: str = input("Enter a 5-character word: ")
if len(secret_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    single_character: str = input("Enter a single character: ")
    if len(single_character) != 1:
        print("Error: Character must consist of 1 character")
        exit()
    else:
        print("Searching for " + single_character + " in " + secret_word)

counter: int = 0

if secret_word[0] == single_character:
    print (single_character + " is found at index 0")
    counter += 1

if secret_word[1] == single_character:
    print (single_character + " is found at index 1")
    counter += 1

if secret_word[2] == single_character:
    print (single_character + " is found at index 2")
    counter += 1

if secret_word[3] == single_character:
    print (single_character + " is found at index 3")
    counter += 1

if secret_word[4] == single_character:
    print (single_character + " is found at index 4")
    counter += 1

if counter == 0:
    print("No instances of " + single_character + " found in " + secret_word)
else:
    if counter == 1:
        print("1 instance of " + single_character + " found in " + secret_word)
    else:
        print(str(counter) + " instances of " + single_character + " found in " + secret_word)
