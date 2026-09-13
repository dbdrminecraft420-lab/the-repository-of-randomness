#!/usr/bin/env python3
"""Infinity Bot — multiplies chaos by an unreasonable amount."""
import random
import sys

MULTIPLIERS = ["♾️x", "maximum", "too much", "yes", "all of it", "Grade 5 energy squared"]

MESSAGES = [
    "Chaos coefficient has been raised.",
    "Scooter velocity set to unbounded.",
    "Boredom detected and vaporized.",
    "The repository accepts your surrender to disorder.",
    "Free time has entered a recursive loop.",
    "MelonKing approval rating: ♾️",
]

def main():
    print("=" * 44)
    print("  INFINITY BOT — CHAOS MULTIPLIER")
    print("=" * 44)
    print()
    print("Mode:     ", random.choice(MULTIPLIERS))
    print("Dispatch: ", random.choice(MESSAGES))
    print()
    print("Long live the scooters. Forever.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
