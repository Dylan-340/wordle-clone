# ⬛, 🟩, 🟨


import random
from os import system


with open("wordle_words.txt", "r") as words_file:
    words = words_file.read().split("\n")
    words_file.close()

system("clear")

print("(ctrl+c to exit)\n\nWordle")


while True:

    game_boxes = ["⬛⬛⬛⬛⬛", "⬛⬛⬛⬛⬛", "⬛⬛⬛⬛⬛", "⬛⬛⬛⬛⬛", "⬛⬛⬛⬛⬛", "⬛⬛⬛⬛⬛"]
    correct_word = random.choice(words)
    for i in game_boxes:
        print(i)
    


    guessed_word = input("Enter your first guess: ").lower()
    
    
    

    



