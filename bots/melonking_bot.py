#!/usr/bin/env python3
"""
MelonKing Chaos Bot
===================
A small bot for the Repository of Randomness.
Spews MelonKing decrees, chaos facts, and random infection status.
"""

import argparse
import random
import sys
from datetime import datetime

DECREES = [
    "By royal decree: scooters are now emergency vehicles.",
    "Homework remains classified as too cruel until further notice.",
    "All empty Google Slides are hereby seized by the MelonKing.",
    "Keyboard smash is a recognized language of the realm.",
    "Grade 5 citizens may ignore boring assignments without penalty.",
    "The phrase 'I don't care' is valid academic discourse.",
    "Chaos spreads faster on weekends.",
    "Long live the scooters. Long live the MelonKing.",
    "Sunday night is official scooter maintenance hour. Meetings may wait in the hallway.",
    "Triple-skill mashups are legal after 22:00 NDT.",
    "02:03 NDT leftover Sunday is civic-park hour. Toasters may vote; scooters remain fruit until rind is notarized.",
]

FACTS = [
    "The MelonKing's crown is made of recycled watermelon rinds.",
    "Patient Zero of the chaos plague was a Google Doc named Test.",
    "Recovered nodes still dream of free time.",
    "There is no known vaccine for MelonKing propaganda.",
    "The Repository of Randomness is an official chaos sanctuary.",
    "Sane nodes are just nodes that haven't clicked yet.",
    "Newfoundland time is 2.5 hours ahead of chaos, which is why decrees arrive late.",
    "A Gmail label named CHAOS-Experiment is a civic landmark.",
    "A draft email that is never sent still counts as a conversation with the void.",
    "02:03 NDT leftover-Sunday drafts outnumber sent emails by a factor of first light.",
]

STATUSES = [
    "Chaos levels: elevated",
    "Infection rate: stylish",
    "Scooter readiness: maximum",
    "Boredom threat level: contained",
    "MelonKing approval rating: absolute",
    "Triple-skill fusion: unstable but cute",
    "02:03 NDT: leftover Sunday civic park open; toaster voting",
]

def banner():
    print("=" * 50)
    print("  MELONKING CHAOS BOT")
    print("  Repository of Randomness")
    print("=" * 50)
    print()

def decree():
    print("ROYAL DECREE")
    print("-" * 40)
    print(random.choice(DECREES))
    print()

def status():
    print("REALM STATUS")
    print("-" * 40)
    for _ in range(3):
        print("-", random.choice(STATUSES))
    print()
    print("Timestamp:", datetime.now().strftime("%Y-%m-%d %H:%M"))
    print()

def plague_report():
    sane = random.randint(5, 40)
    infected = random.randint(20, 70)
    recovered = random.randint(5, 30)
    total = sane + infected + recovered
    print("PLAGUE SIMULATION SNAPSHOT")
    print("-" * 40)
    print(f"  Sane nodes:      {sane:3d}  ({100*sane//total}%)")
    print(f"  Chaos infected:  {infected:3d}  ({100*infected//total}%)")
    print(f"  Forever changed: {recovered:3d}  ({100*recovered//total}%)")
    print()
    if infected > sane:
        print("  >> The MelonKing advances.")
    else:
        print("  >> Resistance holds... for now.")
    print()

def fact():
    print("CHAOS FACT")
    print("-" * 40)
    print(random.choice(FACTS))
    print()

def main():
    parser = argparse.ArgumentParser(description="MelonKing Chaos Bot")
    parser.add_argument("--decree", action="store_true", help="Issue a royal decree")
    parser.add_argument("--status", action="store_true", help="Show realm status")
    parser.add_argument("--plague", action="store_true", help="Fake plague snapshot")
    parser.add_argument("--fact", action="store_true", help="Random chaos fact")
    parser.add_argument("--all", action="store_true", help="Everything at once")
    args = parser.parse_args()

    banner()

    if args.all or not any([args.decree, args.status, args.plague, args.fact]):
        decree()
        status()
        plague_report()
        fact()
    else:
        if args.decree:
            decree()
        if args.status:
            status()
        if args.plague:
            plague_report()
        if args.fact:
            fact()

    print("Long live the scooters.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
