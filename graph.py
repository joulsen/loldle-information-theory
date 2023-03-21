# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:50:45 2023

@author: Andreas J. P.
"""

import json
import matplotlib.pyplot as plt
from loldle import get_best_guesses


def plot_information_boxplot(guesses):
    fig, axis = plt.subplots(figsize=(10, 2))
    axis.boxplot([c["bits"] for c in guesses], vert=False, widths=0.4)
    axis.grid(axis="x")
    axis.set_yticks([])
    axis.set_xlabel("Information of guess [Bits]")
    for d in ["right", "top", "left"]:
        axis.spines[d].set_visible(False)
    return fig


def plot_best_worst(guesses, n):
    fig, axes = plt.subplots(2, 1, figsize=(6, 10), sharex=True)
    colors = ["#2B3467", "#EB455F"]
    for i, data in enumerate([guesses[:10], guesses[-10:]]):
        data = list(reversed(data))
        axes[i].barh(range(10), [c["bits"] for c in data], color=colors[i])
        axes[i].set_yticks(range(10))
        axes[i].set_yticklabels([c["championName"] for c in data])
        axes[i].grid(axis="x")
        for d in ["right", "top"]:
            axes[i].spines[d].set_visible(False)
    axes[0].set_title("Best 10 initial guesses for LoLdle", size=14)
    axes[1].set_title("Worst 10 initial guesses for LoLdle", size=14)
    axes[1].set_xlabel("Information of guess [Bits]", size=14)


if __name__ == "__main__":
    with open("resources/loldle-champ-data.json", "r") as file:
        champs = json.load(file)
    guesses = get_best_guesses(champs)
    plot_best_worst(guesses, 10)
    plt.savefig("graphs/best_worst.png", dpi=100, bbox_inches="tight")
    plot_information_boxplot(guesses)
    plt.savefig("results/information_boxplot.png",
                dpi=100, bbox_inches="tight")
