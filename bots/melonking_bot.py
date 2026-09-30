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
    "03:11 NDT Monday: leftover Sunday requested a third briefing. The World is fruit. Drafts stay drafts.",
    "08:11 NDT Monday: breakfast is a scooter wearing a rind. Do not send the draft.",
    "09:11 NDT Monday: three skills share one rind and call it governance.",
    "13:11 NDT Monday: the hallway between two hallways is now a parliament. Tuesday is a fruit pending appeal.",
    "16:11 NDT Monday: after-lunch parliament. Gravity optional until 20:00. Oilers emails are ceremonial fruit.",
    "19:11 NDT Monday: evening rind parliament. Facebook pages are fruit. Oilers petitions sit in the gallery.",
    "10:11 NDT Tuesday: mid-morning rind parliament. Three skills share one scooter. Drafts stay drafts.",
    "13:11 NDT Tuesday: afternoon rind parliament. Three skills share one hallway. NYT Games is ceremonial fruit.",
    "21:11 NDT Tuesday: evening rind parliament. Grammarly is quiet fruit. NYT sale sits in the gallery. Drafts stay drafts.",
    "06:11 NDT Wednesday: leftover hallway parliament. vidIQ, GDevelop, and The World are ceremonial fruit. Invisible melons meet tomorrow for 17 minutes.",
    "07:11 NDT Wednesday: breakfast rind parliament. Three skills share one melon. Drafts stay drafts. Gravity files a minority report.",
    "13:11 NDT Wednesday: afternoon rind parliament. Three skills share one scooter. Thursday is a fruit pending appeal. Invisible melon meets tomorrow at 15:00 NDT.",
    "20:11 NDT Wednesday: evening rind parliament. Lucky Mobile is ceremonial paperwork fruit. Three skills share one dinner plate.",
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
    "03:11 NDT Monday is leftover Sunday holding a fruit cabinet while The World ripens unread.",
    "08:11 NDT Monday is when three skills share one rind and call it governance.",
    "09:11 NDT Monday is mid-morning rind parliament. Gravity remains optional until lunch.",
    "13:11 NDT Monday is when a scooter files a pull request against gravity and gravity leaves a review of 'several'.",
    "16:11 NDT Monday is when Change.org and NYT Games sit in the gallery while the draft refuses to leave the building.",
    "19:11 NDT Monday is when At Home With Blake is recommended as fruit and the evening rind refuses to be mailed.",
    "10:11 NDT Tuesday is when the Committee of Unrelated Thoughts files minutes into a bush.",
    "13:11 NDT Tuesday is when minutes walk out of the meeting and join NYT Games at 75 percent off.",
    "21:11 NDT Tuesday is when Grammarly reports a quiet week and parliament classifies silence as produce.",
    "06:11 NDT Wednesday is when leftover minutes elect a mayor made of rind and adjourn into a salad.",
    "07:11 NDT Wednesday is when breakfast becomes a quorum and vidIQ is seated as ceremonial fruit.",
    "13:11 NDT Wednesday is when afternoon minutes elect a scooter as speaker and file NYT Games under produce.",
    "20:11 NDT Wednesday is when Lucky Mobile top-up emails sit in the gallery and evening minutes adjourn into a prepaid rind.",
]

STATUSES = [
    "Chaos levels: elevated",
    "Infection rate: stylish",
    "Scooter readiness: maximum",
    "Boredom threat level: contained",
    "MelonKing approval rating: absolute",
    "Triple-skill fusion: unstable but cute",
    "03:11 NDT Monday: leftover Sunday + The World fruit + drafts unsent",
    "08:11 NDT Monday: breakfast fruit + unsent drafts + optional gravity",
    "09:11 NDT Monday: mid-morning parliament + Gravity-Optional Lunchbox",
    "13:11 NDT Monday: hallway parliament + Tuesday-as-fruit appeal + unsent rind",
    "16:11 NDT Monday: after-lunch parliament + ceremonial Oilers fruit + unsent rind",
    "19:11 NDT Monday: evening parliament + Blake-as-fruit + unsent rind",
    "10:11 NDT Tuesday: mid-morning parliament + unsent rind + NYT as ceremonial fruit",
    "13:11 NDT Tuesday: afternoon parliament + unsent rind + 75-percent-off puzzles as gallery fruit",
    "21:11 NDT Tuesday: evening parliament + quiet Grammarly fruit + unsent rind",
    "06:11 NDT Wednesday: leftover parliament + vidIQ fruit + unsent rind + 17-minute melon meeting",
    "07:11 NDT Wednesday: breakfast parliament + three-skill rind + drafts unsent",
    "13:11 NDT Wednesday: afternoon parliament + Thursday-as-fruit + unsent rind + 17-minute melon meeting",
    "20:11 NDT Wednesday: evening parliament + Lucky Mobile fruit + unsent rind",
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
