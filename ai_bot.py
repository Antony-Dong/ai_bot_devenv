

import requests
import random

def guess_daily(guess, size=5):
    url="https://wordle.votee.dev:8000/daily"
    params = {
        "guess": guess,
        "size": size
    }
    response = requests.get(url, params=params)
    return response.json()

def guess_random(guess, size=5, seed=None):
    url="https://wordle.votee.dev:8000/random"
    params = {
        "guess": guess,
        "size": size,
        "seed": seed
    }
    response = requests.get(url, params=params)
    return response.json()

def guess_word(word, guess):
    url=f"https://wordle.votee.dev:8000/word/{word}"
    params = {
        "guess": guess,
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

def test_api_endpoints():
    print("Testing /daily with guess:", "apple")
    daily=guess_daily("apple")
    print(daily)

    print("Testing /random with guess:", "apple")
    random=guess_random("apple", seed=42)
    print(random)

    print("Testing /word with word and guess:", "apple")
    word_guess=guess_word("apple", "apple")
    print(word_guess)


def refine_guesses(initial_guess, feedback):
    new_guess=list(initial_guess)
    for f in feedback:
        slot = f['slot']
        guess = f['guess']
        result = f['result']

        if result=="present" or result =="absent":
            new_guess[slot] = chr(((ord(new_guess[slot]) - 97 + 1) % 26) + 97)
    return "".join(new_guess)



def play_guess_daily(size):
    potential_words="abcdefghijklmnopqrstuvwxyz"
    current_guess =potential_words[:size]  # Start with the first 'size' letters of the alphabet
    round_num = 1
    print(f"Attempt {round_num}: Starting guess: {current_guess}\n")
    
    while True:       
        feedback = guess_daily(current_guess, size=size)
        if feedback:
            if all(f['result'] == 'correct' for f in feedback):
                print(f"Correct guess! The word is: {current_guess}\n")
                break

            current_guess = refine_guesses(current_guess, feedback)
            round_num += 1
            print(f"Attempt {round_num}: Next guess: {current_guess}\n")
        else:
            print("Failed to get a valid response from the API")
            break


def play_guess_random(size,seed):
    potential_words="abcdefghijklmnopqrstuvwxyz"
    current_guess =potential_words[:size]  # Start with the first 'size' letters of the alphabet
    if seed is None:
        seed = random.randint(0, 10000)  # Generate a random seed if not provided
    else:
        seed = seed
    round_num = 1
    print(f"Attempt {round_num}: Starting guess: {current_guess}\n")
    
    while True:
        feedback = guess_random(current_guess, size=size, seed=seed)
        if feedback:
            if all(f['result'] == 'correct' for f in feedback):
                print(f"Correct guess! The word is: {current_guess}\n")
                break

            current_guess = refine_guesses(current_guess, feedback)
            round_num += 1
            print(f"Attempt {round_num}: Next guess: {current_guess}\n")
        else:
            print("Failed to get a valid response from the API")
            break

def play_guess_word(target_word):
    target_word=target_word.lower()
    current_guess="apple"
    round_num=1
    print(f"Attempt {round_num}: Starting guess: {current_guess}\n")
    
    while True:
        feedback=guess_word(target_word, current_guess)
        if feedback:
            if all(f['result'] == 'correct' for f in feedback):
                print(f"Correct guess! The word is: {current_guess}\n")
                break

            current_guess= refine_guesses(current_guess, feedback)
            round_num += 1
            print(f"Attempt {round_num}: Next guess: {current_guess}\n")
        else:
            print("Failed to get a valid response from the API")
            break

def user_input_mode():
    choice = input("Please enter the number of the mode you want to play: ")
    while choice not in ["1", "2", "3"]:
        print("Invalid choice. Please enter 1, 2, or 3.")
        choice = input("Please enter the number of the mode you want to play: ")
    return choice


def main():
    print("" \
    "Welcome to the AI Bot Word Guessing Game!\n" \
    "You can choose from the following modes:\n" \
    "1. Daily Guess\n" \
    "2. Random Guess\n" \
    "3. Word Guess\n" )

    choice=user_input_mode()   

    if choice == "1":
        print("You chose Daily Guess mode.")
        size=int(input("Enter the size of the word (default is 5): ") or 5)
        play_guess_daily(size)
    elif choice == "2":
        print("You chose Random Guess mode.")
        size=int(input("Enter the size of the word (default is 5): ") or 5)
        seed = input("Enter a seed for randomization (default is random): ")
        if seed.isdigit():
            seed = int(seed)
        else:
            seed = None
        play_guess_random(size,seed)
    elif choice == "3":
        print("You chose Word Guess mode.")
        target_word = input("Enter the target word with 5 letters (default is 'arpon'): ") or "arpon"
        if len(target_word) != 5:
            print("The word is not 5 letters long. Defaulting to 'arpon'.")
            target_word = "arpon"
        print(f"Target word is: {target_word}")
        play_guess_word(target_word)



if __name__ == "__main__":
    main()