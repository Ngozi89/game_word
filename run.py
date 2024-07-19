import random


def guess_word():
    choose = ["dish", "rules", "video", "shoulder"]
    return random.choice(choose) # Return random words from the string

def word_status(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    return display

# Find the word to be guessed 
def guess_missing_word():
    missing_word = guess_word()
    guessed_letters = []
    attempts = 7

    print("Guess Missing Letters")
    print("*********")
    print("Missing Word:", word_status(missing_word, guessed_letters))

# Loop to allow players contiune guessing as long as there's attempt left
    while attempts > 0:

        guess = input("Guess A Letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single leter.")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter.")
            continue

        guessed_letters.append(guess)

        if guess not in missing_word:
            attempts -= 1
            print(f"No letter '{guess}' occurs in the word.")
            print(f"You have {attempts} attempts remainng.")
        else:
            occurrences = missing_word.count(guess)
            print(f"Letter '{guess}' occurs {occurrences} times.")

        current_status = word_status(missing_word, guessed_letters)
        print("Missing Letter:", current_status)


        if "_" not in current_status:
            print("Congratulation! You guessed correctly.")
            break
    
    if "_" in current_status:
        print(f"You have no attempts left!  The word was: {missing_word}")



guess_missing_word()