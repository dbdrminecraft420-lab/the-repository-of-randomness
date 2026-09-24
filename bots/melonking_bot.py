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
    "02:01 NDT leftover Wednesday: the NYT Cold War AI briefing is ceremonial produce. Drafts still outrank sent mail.",
    "03:07 NDT leftover Wednesday: vidIQ no-thumbnail videos are honorary decrees. Honda of Fayetteville remains 10K.",
    "04:13 NDT leftover Wednesday: GDevelop English class is now a video game. Cold War AI lessons require melon rind.",
    "09:17 NDT leftover Wednesday: Wordsmaxxing is ceremonial produce. Instagram suggestions must wear scooter helmets.",
    "12:07 NDT leftover Wednesday: LEGO leftovers, Wordsmaxxing, and remzyyzz share one helmet. Drafts remain unsent on purpose.",
    "18:04 NDT leftover Wednesday: GDevelop metroidvania is ceremonial fruit. The stapler remains missing on purpose.",
    "20:07 NDT leftover Wednesday: DEXA scans are ceremonial bones. GDevelop still dreams in metroidvania.",
    "22:21 NDT leftover Wednesday: Grammarly 50% off is ceremonial personality. NYT bones are snacks. Drafts stay drafts.",
    "02:01 NDT leftover Thursday: Applaydu is ceremonial playground. Facebook chef pages must wear scooter helmets.",
    "03:06 NDT leftover Thursday: Decoding Trump-Xi is ceremonial produce. Applaydu still misses the realm.",
    "04:12 NDT leftover Thursday: The World newsletter is now a scooter briefing. Triple-skill parliament is in session.",
    "05:01 NDT leftover Thursday: Iran's UN speech is ceremonial rind. Triple-skill parliament files leftover minutes again.",
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
    "02:01 NDT leftover Wednesday is when Cold War lessons for A.I. ripen into stationery.",
    "03:07 NDT leftover Wednesday is when a 700,000-view video without a thumbnail becomes official produce.",
    "04:13 NDT leftover Wednesday is when GDevelop becomes English class and drafts stay paper airplanes.",
    "09:17 NDT leftover Wednesday is when remzyyzz becomes honorary rind.",
    "12:07 NDT leftover Wednesday is when LEGO clearance emails become parliamentary snacks.",
    "18:04 NDT leftover Wednesday is when GDevelop metroidvanias ripen in the Drafts folder.",
    "20:07 NDT leftover Wednesday is when bone density emails become ceremonial produce.",
    "22:21 NDT leftover Wednesday is when Grammarly tries to sell you a second personality at half price.",
    "02:01 NDT leftover Thursday is when Applaydu and Facebook chefs ripen into stationery.",
    "03:06 NDT leftover Thursday is when The World newsletter becomes a scooter briefing.",
    "04:12 NDT leftover Thursday is when leftover Thursday files a motion to remain leftover.",
    "05:01 NDT leftover Thursday is when UN speeches ripen into scooter briefings.",
]

STATUSES = [
    "Chaos levels: elevated",
    "Infection rate: stylish",
    "Scooter readiness: maximum",
    "Boredom threat level: contained",
    "MelonKing approval rating: absolute",
    "Triple-skill fusion: unstable but cute",
    "02:01 NDT leftover Wednesday: NYT classified as fruit; chess streak endangered; Honda still 10K",
    "03:07 NDT leftover Wednesday: vidIQ classified as fruit; drafts still win; parliament in session",
    "04:13 NDT leftover Wednesday: GDevelop classified as fruit; parliament still in session",
    "09:17 NDT leftover Wednesday: wordsmaxxing classified as fruit; parliament still in session",
    "12:07 NDT leftover Wednesday: LEGO classified as fruit; wordsmaxxing still chewing; parliament in session",
    "18:04 NDT leftover Wednesday: GDevelop classified as fruit; parliament still in session",
    "20:07 NDT leftover Wednesday: DEXA classified as fruit; parliament still in session",
    "22:21 NDT leftover Wednesday: Grammarly classified as fruit; bones classified as snacks; parliament in session",
    "02:01 NDT leftover Thursday: Applaydu classified as playground; chefs classified as produce; parliament in session",
    "03:06 NDT leftover Thursday: Trump-Xi classified as fruit; Applaydu still missing you; parliament in session",
    "04:12 NDT leftover Thursday: The World classified as fruit; triple-skill parliament in session",
    "05:01 NDT leftover Thursday: UN speech classified as rind; parliament still leftover",
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
    print(f"  Infected nodes:  {infected:3d}  ({100*infected//total}%)")
    print(f"  Recovered:       {recovered:3d}  ({100*recovered//total}%)")
    print()

def fact():
    print("CHAOS FACT")
    print("-" * 40)
    print(random.choice(FACTS))
    print()

def main():
    parser = argparse.ArgumentParser(description="MelonKing Chaos Bot")
    parser.add_argument("--decree", action="store_true")
    parser.add_argument("--status", action="store_true")
    parser.add_argument("--plague", action="store_true")
    parser.add_argument("--fact", action="store_true")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    banner()
    if args.all or not any([args.decree, args.status, args.plague, args.fact]):
        decree(); status(); plague_report(); fact()
    else:
        if args.decree: decree()
        if args.status: status()
        if args.plague: plague_report()
        if args.fact: fact()
    print("Long live the scooters.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
