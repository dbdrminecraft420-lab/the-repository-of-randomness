#!/usr/bin/env python3
"""Nonsense Bot — produces confident useless output on demand."""

import random
import sys

LINES = [
    "The committee has adjourned into fog.",
    "Seriousness rating of this statement: 2/10.",
    "Quantum boredom repellent is currently out of stock.",
    "A green node blinked. Interpretation pending.",
    "bb bnbbnbbb remains the official language of the realm.",
    "This sentence is true only on Tuesdays.",
    "The Repository of Randomness accepts your resignation from order.",
    "Productive confusion has been achieved.",
    "Side effects may include sudden scooter ownership.",
    "Everything is fine. Everything is also not fine.",
]

def main():
    print("NONSENSE BOT")
    print("-" * 30)
    for _ in range(3):
        print("•", random.choice(LINES))
    print()
    print("— Dept. of Productive Confusion")
    return 0

if __name__ == "__main__":
    sys.exit(main())
