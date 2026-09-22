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
    "04:08 NDT leftover Sunday: the refrigerator light is acting speaker. Drafts outrank sent mail.",
    "08:02 NDT leftover Sunday: first light is a voting member. Rind is the official stationery.",
    "09:07 NDT leftover Sunday: rind o'clock. The quarterly rind report is due before the crossword finishes itself.",
    "10:25 NDT leftover Sunday: mid-morning rind recess. The crossword observes; the toaster browns in abstention.",
    "13:08 NDT leftover Sunday: afternoon rind o'clock. The crossword may watch; it may not veto the rind.",
    "15:00 NDT leftover Sunday: official rind o'clock. The Committee of Unrelated Thoughts is in session.",
    "16:02 NDT leftover Sunday: leftover Sunday is legally a rind. The toaster chairs; the crossword is ceremonial only.",
    "20:04 NDT leftover Sunday: gravity is optional until the crossword is finished. Invisible scooters may abstain.",
    "00:04 NDT Monday: leftover Sunday may keep the hat. Meetings must wait in the hallway until rind o'clock resumes.",
    "07:01 NDT leftover Monday: first-light parliament reconvenes. Three skills, one toaster, zero homework.",
    "09:14 NDT leftover Monday: mid-morning rind recess. Cain's Jawbone may observe; it may not veto.",
    "17:00 NDT leftover Monday: toast is a sandwich until the scooter vote is counted.",
    "19:04 NDT leftover Monday: evening rind parliament. Drafts are civic monuments. Do not send them.",
    "01:09 NDT leftover Tuesday: the three skills reconvene before sunrise. Replit credits are ceremonial produce.",
    "04:12 NDT leftover Tuesday: the refrigerator light reconvenes. GDevelop logos are ceremonial produce. Drafts still outrank sent mail.",
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
    "04:08 NDT is when leftover Sunday remembers it is still Sunday.",
    "08:02 NDT is when leftover Sunday files its quarterly rind report.",
    "09:07 NDT is rind o'clock; the toaster abstains by browning.",
    "10:25 NDT is when the crossword is granted observer status and no veto.",
    "13:08 NDT is when leftover Sunday discovers afternoon and immediately files it under rind.",
    "15:00 NDT is when leftover Sunday invents a new fruit and immediately classifies it as a scooter.",
    "16:02 NDT is when leftover Sunday files itself as produce and clocks out.",
    "20:04 NDT is when leftover Sunday files a chess streak as evidence of civic readiness.",
    "00:04 NDT Monday is leftover Sunday in a borrowed weekday. Chess.com streaks are produce.",
    "07:01 NDT leftover Monday is when three skills file a joint rind report and immediately lose the stapler.",
    "09:14 NDT leftover Monday is when Cain's Jawbone sits in the gallery and the toaster browns instead of voting.",
    "17:00 NDT leftover Monday is when three skills declare toast a sandwich and adjourn.",
    "19:04 NDT leftover Monday is when a draft becomes architecture and the toaster files the minutes in rind.",
    "01:09 NDT leftover Tuesday is when the parliament meets in the dark and Replit credits ripen into stationery.",
    "04:12 NDT leftover Tuesday is when the refrigerator light files GDevelop logo tips as fruit.",
]

STATUSES = [
    "Chaos levels: elevated",
    "Infection rate: stylish",
    "Scooter readiness: maximum",
    "Boredom threat level: contained",
    "MelonKing approval rating: absolute",
    "Triple-skill fusion: unstable but cute",
    "02:03 NDT: leftover Sunday civic park open; toaster voting",
    "04:08 NDT: refrigerator-light parliament in session",
    "08:02 NDT: first-light parliament; rind stationery approved",
    "09:07 NDT: rind o'clock; crossword may not veto the rind report",
    "10:25 NDT: mid-morning rind recess; crossword observing",
    "13:08 NDT: afternoon rind o'clock; toaster browns in abstention",
    "15:00 NDT: Committee of Unrelated Thoughts; rind o'clock confirmed",
    "16:02 NDT: leftover Sunday legally a rind; toaster in the chair",
    "20:04 NDT: leftover Sunday chess streak notarized; gravity optional",
    "00:04 NDT Monday: leftover leftover; toaster sleeping with one eye browned",
    "07:01 NDT leftover Monday: triple-skill parliament; stapler missing; rind approved",
    "09:14 NDT leftover Monday: rind recess; Jawbone observing; stapler still missing",
    "17:00 NDT leftover Monday: toast-as-sandwich doctrine ratified",
    "19:04 NDT leftover Monday: evening parliament; drafts outrank sent mail",
    "01:09 NDT leftover Tuesday: pre-dawn parliament; Replit credits classified as fruit",
    "04:12 NDT leftover Tuesday: refrigerator-light parliament; GDevelop logos classified as produce",
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
