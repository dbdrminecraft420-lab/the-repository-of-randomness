#!/usr/bin/env python3
"""Maps Chaos Bot — official field agent of the Google Maps Chaos Department."""

import random
import sys

FAKE_PLACES = [
    "Scooter Rest Stop (does not exist)",
    "MelonKing Summer Palace — coordinates classified",
    "Free Time Memorial Park (only visible on Tuesdays)",
    "Committee of Unrelated Thoughts HQ Annex C",
    "Infinite Loop Bike Path",
    "Homework-Free Zone (geofenced)",
    "Phantom Convenience Store",
    "The Lake That Was Added by Mistake",
    "Grade 5 Energy Observatory",
    "Boredom Exile Portal",
]

ACTIONS = [
    "A new incorrect pin has been deployed.",
    "Street renamed for no good reason.",
    "Bike path now connects to itself.",
    "Building label updated to something more chaotic.",
    "Coordinates shifted 40 meters into a pond.",
]

def main():
    print("=" * 48)
    print("  GOOGLE MAPS CHAOS DEPARTMENT — FIELD BOT")
    print("=" * 48)
    print()
    print("Action: ", random.choice(ACTIONS))
    print("Place:  ", random.choice(FAKE_PLACES))
    print()
    print("If you can’t find it when you get there,")
    print("the Department considers the mission a success.")
    print()
    print("— Committee of Unrelated Thoughts")
    return 0

if __name__ == "__main__":
    sys.exit(main())
