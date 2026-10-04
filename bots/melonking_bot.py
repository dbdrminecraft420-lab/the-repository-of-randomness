#!/usr/bin/env python3
"""MelonKing Chaos Bot — short working restore after CHAOS nine-pm rumor."""
import random, sys
from datetime import datetime
DECREES = [
    "By royal decree: scooters are now emergency vehicles.",
    "Long live the scooters. Long live the MelonKing.",
    "21:11 NDT Sunday Oct 4: triple-skill. Three skills shared one melon and called the clock a nine-pm rumor. Scooters remain emergency fruit. Drafts stay drafts.",
    "20:11 NDT Sunday Oct 4: triple-skill. Three skills shared one melon and called the clock an eight-pm rumor. Scooters remain emergency fruit. Drafts stay drafts.",
    "15:11 NDT Sunday Oct 4: triple-skill. Three skills shared one melon and called the clock a three-pm rumor. Scooters remain emergency fruit. Drafts stay drafts.",
]
FACTS = [
    "The Repository of Randomness is an official chaos sanctuary.",
    "21:11 NDT Sunday Oct 4 is when three skills share one melon and declare the clock a nine-pm rumor.",
]
STATUSES = ["Chaos levels: elevated", "21:11 NDT Sunday Oct 4: triple-skill melon + unsent draft + ceremonial nine-pm rumor"]
def main():
    print("MELONKING CHAOS BOT")
    print(random.choice(DECREES))
    print(random.choice(FACTS))
    print(random.choice(STATUSES), datetime.now().isoformat(timespec='minutes'))
    print("Long live the scooters.")
    return 0
if __name__ == '__main__':
    sys.exit(main())
