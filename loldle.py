# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:52:10 2023

@author: Andreas J. P.
"""

import json
from math import log


def match_on_property(champs, prop, value):
    matches = {"correct": [], "partial": [], "incorrect": []}
    for c in champs:
        if prop == "positions" and len(value) > 1 and c["championName"] == "Dr. Mundo":
            print("Dr. Mundo")
        if prop == "release_date":
            year1 = int(c[prop][:4])
            year2 = int(value[:4])
            if year1 == year2:
                matches["correct"].append(c)
            elif year1 > year2:
                matches["incorrect"].append(c)
            elif year1 < year2:
                matches["partial"].append(c)
        elif type(value) == list:
            sets = [set(c[prop]), set(value)]
            intersection = sets[0].intersection(sets[1])
            if len(intersection) == 0:
                matches["incorrect"].append(c)
            elif len(intersection) < max(map(len, sets)):
                matches["partial"].append(c)
            else:
                matches["correct"].append(c)
        else:
            if c[prop] == value:
                matches["correct"].append(c)
            else:
                matches["incorrect"].append(c)
    return matches


def match_champion(champs, champ):
    matches = {"": champs}
    for p in ["gender", "positions", "species", "resource",
              "range_type", "regions", "release_date"]:
        new_matches = {}
        for name, match in matches.items():
            match = match_on_property(match, p, champ[p])
            match = {name + "O": match["correct"],
                     name + "X": match["incorrect"],
                     name + "P": match["partial"]}
            new_matches.update(match)
        new_matches = {k: v for k, v in new_matches.items() if v}
        matches = new_matches
    return matches


def get_bits(matches):
    average = 0
    n_champs = sum(map(len, matches.values()))
    for label, match in matches.items():
        prop = len(match) / n_champs
        bits = log(1/prop, 2)
        average += prop * bits
    return average


def get_best_guesses(champs):
    for champ in champs:
        matches = match_champion(champs, champ)
        champ["bits"] = get_bits(matches)
    return sorted(champs, key=lambda c: -c["bits"])


if __name__ == "__main__":
    with open("resources/loldle-champ-data.json", "r") as file:
        champs = json.load(file)
        matches = match_on_property(champs, "positions", ["Jungle", "Middle"])
        # guesses = get_best_guesses(champs)
        # print("rank,champion,entropy")
        # for i, c in enumerate(guesses):
        #     print("{},{},{:.3f}".format(i+1, c["championName"], c["bits"]))
