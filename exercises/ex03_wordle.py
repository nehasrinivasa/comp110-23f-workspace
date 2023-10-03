"""EX03 - Structured Wordle Game!"""
__author__ = "730675654"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(search_str: str, single_chr: str) -> bool:
    """True if single character in second string is found at any index of the first string, otherwise it will return false"""
    assert len(single_chr) == 1
    counter: int = 0
    while counter < len(search_str):
        if search_str[counter] == single_chr:
            return True
        else:
            counter +=1
    return False

def emojified(guess_str: str, secret_word: str) -> str:
    """Returns emojified string with green, yellow, and white boxes"""
    assert len(guess_str) == len(secret_word)

    guess_counter: int = 0
    display_emoji: str = ""

    while guess_counter < len(guess_str):
        if guess_str[guess_counter] == secret_word[guess_counter]:
            display_emoji += str(GREEN_BOX)
            guess_counter += 1
        elif contains_char(secret_word, guess_str[guess_counter]):
            display_emoji += str(YELLOW_BOX)
        else:
            display_emoji += str(WHITE_BOX)
            guess_counter += 1
    return display_emoji

def input_guess(expected_length: int) -> str:
    """Checks the length of what the user inputted"""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} characters! Try again:")
    return user_guess
    
def main() -> None:
    """Where you enter the program and main game loop"""
    secret_word: str = "python"
    correct: bool = False
    turns: int = 1

    while turns <= 6 and correct is not True:
        print(f"=== Turn {turns}/6 ===")
        guess_str: str = input_guess(len(secret_word))
        print(emojified(input_guess, secret_word))
        if input_guess == secret_word:
            print(f"===You won in {turns}/6 ===")
        else:
            turns += 1
    if correct is not True:
        print("X/6 - Sorry, try again tomorrow!")    

if __name__ == "__main__":
    input_guess()    


