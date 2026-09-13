#!/usr/bin/env python3
"""Tiny chaos seed generator for the Repository of Randomness."""
import random

SEEDS = [
    "scooter",
    "melon",
    "chaos",
    "grade5",
    "free-time",
    "keyboard-smash",
    "node-infected",
    "royal-decree",
    "boredom-banned",
    "watermelon-crown",
]

def main():
    print("CHAOS SEED:", "-".join(random.sample(SEEDS, 3)))
    print("Use it to name your next file, commit, or rebellion.")

if __name__ == "__main__":
    main()
