# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 15:26:03 2023

@author: Andreas
"""

import json
from loldle import get_best_guesses, match_champion

n = 5

with open("resources/loldle-champ-data.json", "r") as file:
    champs = json.load(file)

print("LoLdle Interactive solver")
print("Keys:\n O: Correct\n X: Incorrect\n P: Partially correct")
print("Guess year > Actual year: Incorrect (X)")
print("Guess year < Actual year: Partially incorrect (P)")
pool = champs

while True:
    best_guesses = get_best_guesses(pool)
    print(f"\nPossible guesses: {len(pool)}")
    print("Bits, Champion")
    for champ in best_guesses[0:n]:
        print("{:4.2f}: {}".format(champ["bits"], champ["championName"]))
    if len(pool) > 1:
        guess = input("\nGuess which champion?\n")
        guess = [c for c in pool if c["championName"].lower() == guess.lower()][0]
        matches = match_champion(pool, guess)
        outcome = input("What is the outcome?\n")
        pool = matches[outcome]
    else:
        break
