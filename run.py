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

guess_missing_word()