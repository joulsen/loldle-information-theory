# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:52:10 2023

@author: Andreas J. P.
"""

import json

with open("resources/loldle-champ-data.json", "r") as file:
    champs = json.load(file)


def match_on_property(champs, prop, value):
    matches = {"correct": [], "partial": [], "incorrect": []}
    for c in champs:
        if prop == "release_date":
            year1 = int(c[prop][:4])
            year2 = int(value[:4])
            if year1 == year2:
                matches["correct"].append(c)
            elif year1 > year2:
                matches["incorrect"].append(c)
            elif year1 < year2:
                matches["partial"].append(c)
        else:
            sets = [set(c[prop]), set(value)]
            intersection = sets[0].intersection(sets[1])
            if len(intersection) == 0:
                matches["incorrect"].append(c)
            elif len(intersection) < max(map(len, sets)):
                matches["partial"].append(c)
            else:
                matches["correct"].append(c)
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


champname = "Garen"
champ = list(filter(lambda c: c["championName"] == champname, champs))[0]
import matplotlib.pyplot as plt



matches = match_champion(champs, champ)
lengths = {k: len(v) for k, v in matches.items()}
lengths = sorted(lengths.items(), key=lambda c: -c[1])
labels = [c[0] for c in lengths]
values = [c[1] for c in lengths]
fig, axis = plt.subplots(figsize=(20,6))
bar = axis.bar(range(len(lengths)), values)
axis.set_xticks(range(len(lengths)))
axis.set_xticklabels([c[0] for c in lengths], rotation=90)
axis.set_title(champ["championName"])
axis.set_ylim(0, max(values)+5)
mapping = {"O": "green", "X": "red", "P": "gold"}
for rect, label in zip(bar, labels):
    basex, basey = (rect.get_x(), rect.get_height()+0.5)
    for i, char in enumerate(label):
        axis.annotate("█", (basex, basey+0.8*i), color=mapping[char])
