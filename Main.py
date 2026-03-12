import random

with open("wordle_words.txt", "r") as words_file:
    words = words_file.read().split("\n")
    words_file.close()