#!/usr/bin/env python3
"""Scooter Bot — free-time enforcement unit for the Repository of Randomness."""

import random
import sys

ANNOUNCEMENTS = [
    "Scooter lanes are now open in all directories.",
    "Any file that has not moved in 24 hours may be relocated by scooter.",
    "Homework detected nearby. Deploying countermeasures.",
    "Free time has been extended by one arbitrary unit.",
    "The MelonKing approves this ride.",
    "Two wheels good. Sitting still bad.",
    "This bot does not brake for boredom.",
]

TIPS = [
    "Always yield to chaos.",
    "Helmets optional. Attitude mandatory.",
    "If the path is straight, add a detour.",
    "Scooters scale better than meetings.",
]

def main():
    print("=" * 40)
    print("  SCOOTER BOT ONLINE")
    print("=" * 40)
    print()
    print("DISPATCH:", random.choice(ANNOUNCEMENTS))
    print("TIP:     ", random.choice(TIPS))
    print()
    print("Long live the scooters.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
