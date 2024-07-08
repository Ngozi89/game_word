import random


def guess_word():
    choose = ["dish", "rules", "video", "shoulder"]
    return random.choice(choose)


print( guess_word() )