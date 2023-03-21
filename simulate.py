# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 17:17:53 2023

@author: Andreas J. P.
"""

from loldle import get_best_guesses, match_champion
from tqdm import tqdm
import json


def simulate(pool, target):
    guesses = []
    while True:
        candidates = get_best_guesses(pool)
        guess = candidates[0]
        guesses.append(guess["championName"])
        if guess == target:
            return guesses
        else:
            pools = match_champion(pool, guess)
            for l, p in pools.items():
                if target in p:
                    pool = p


if __name__ == "__main__":
    with open("resources/loldle-champ-data.json", "r") as file:
        champs = json.load(file)
    guesses = {}
    for champ in tqdm(champs):
        guesses[champ["championName"]] = simulate(champs, champ)

    max_guesses = max(map(len, guesses.values()))
    guess_header = ",".join(["guess" + str(i+1) for i in range(max_guesses)])
    with open("results/guess-order.csv", "w") as file:
        file.write(f"target,guesses_amount,{guess_header}\n")
        for target, guess in guesses.items():
            file.write(f"{target},{len(guess)},")
            for i in range(max_guesses):
                if i < len(guess):
                    file.write(guess[i])
                if i < max_guesses-1:
                    file.write(',')
            file.write('\n')
