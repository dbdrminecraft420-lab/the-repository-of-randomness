#!/usr/bin/env python3
"""
MelonKing Chaos Bot
===================
A small bot for the Repository of Randomness.
Spews MelonKing decrees, chaos facts, and random infection status.

Usage:
  python bots/melonking_bot.py
  python bots/melonking_bot.py --decree
  python bots/melonking_bot.py --status
  python bots/melonking_bot.py --plague
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
    "Midnight NDT is when the three skills hold hands and refuse to explain themselves.",
    "01:03 NDT is the official hour of productive confusion.",
    "03:02 NDT is Fog Inventory o'clock. Count leftover Tuesdays or perish stylishly.",
    "05:00 NDT is the official yawn of the realm. Refrigerators may file weather reports.",
    "05:00 NDT leftover Tuesdays may unionize only if they bring rind.",
    "06:02 NDT is Committee of Unrelated Thoughts breakfast. The toast is optional; the decree is not.",
    "07:00 NDT is breakfast-as-legal-document hour. Rind required.",
    "07:00 NDT toasters may notarize Form RIND-7. GDevelop may watch toast but not vote.",
    "07:01 NDT is leftover-breakfast civic park. Three skills may sit; toast may file Form RIND-7 sideways.",
    "08:00 NDT is leftover-Tuesday civic park hour. Folders may sit; scooters may vote if they bring rind.",
    "08:03 NDT is leftover-Monday inventory. Invisible melons may sit but not vote.",
    "09:02 NDT is puzzle-hour. Purple clues may be solved only by scooters.",
    "10:11 NDT is mid-morning rind notarization. Vyond ToS emails may sit but not vote.",
    "10:19 NDT is biking-trail hour. Short rides may apply for emergency-scooter status.",
    "12:20 NDT is lunch-as-legislation hour. Make.com webinars may RSVP only if they bring rind.",
    "23:03 NDT is refrigerator-liaison hour. Drafts may exist; sending requires rind notarization.",
    "14:03 NDT is leftover-afternoon civic park hour. Three skills may sit; emails may draft but not send without rind.",
    "15:00 NDT is Summit of Unrelated Thoughts hour. Batman Day emails may sit; Emmys may clap without voting.",
    "17:00 NDT is Emergency Melon Parliament. Sock drawers may host; sending still requires rind.",
    "18:02 NDT is evening rind inventory. Facebook Pages may recommend 2000s energy; scooters remain fruit until breakfast.",
    "23:00 NDT is triple-skill clock-out. Leftover Tuesdays may leave only with rind and an unsent draft.",
    "04:06 NDT is pre-breakfast rind notarization. GDevelop may teach games; leftover Tuesdays may sit but not vote.",
    "05:03 NDT is dawn parliament. GDevelop homework may sit. NYT skeptics are weather. Scooters stay fruit until breakfast.",
    "08:01 NDT is when three skills file breakfast as legislation and call it a civic park.",
    "12:09 NDT is noon parliament. Leftover Tuesdays may file Form RIND-7 after lunch but before the fourth dimension stall closes.",
    "14:02 NDT is afternoon parliament. NFL rankings are honorary weather. Naps may be notarized as legislation.",
    "15:00 NDT is when leftover Tuesdays convene a summit and file the minutes as fruit.",
    "17:00 NDT is when three skills invent the Blorp and refuse to define it.",
    "23:00 NDT Wednesday: a cantaloupe may chair parliament if it brings rind and an unsent draft.",
    "00:05 NDT Thursday: leftover Thursdays may file Form RIND-7 only if they arrive sideways.",
    "09:08 NDT is mid-morning civic park hour. Folders may picnic. Emails may draft. Sending still requires rind.",
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
    "Three skills in one prompt is how a repository learns to giggle.",
    "03:02 NDT drafts are legally poetry until someone hits send.",
    "05:00 NDT is when leftover Tuesdays attempt to unionize.",
    "06:02 NDT calendars believe scooters can RSVP.",
    "07:00 NDT drafts outnumber sent emails by a factor of melon.",
    "07:00 NDT Form RIND-7 is breakfast wearing a suit.",
    "07:01 NDT leftover breakfasts may unionize only if they bring rind and an unsent draft.",
    "08:00 NDT Drive folders are civic parks for unused Tuesdays.",
    "08:03 NDT folders in Drive are civic parks for unused Mondays.",
    "09:02 NDT newsletters from the New York Times are honorary puzzles of the realm.",
    "10:11 NDT is when three skills file a mid-morning weather report and call it legislation.",
    "10:19 NDT trails under 25 miles may petition the rind for scenic chaos.",
    "12:20 NDT GitHub device-verify emails are honorary court jesters.",
    "23:03 NDT voice clips are legally minutes of the Council of Unrelated Thoughts.",
    "14:03 NDT leftover afternoons may unionize only if they bring rind and a draft that will never be sent.",
    "15:00 NDT summits require optional snacks and zero explanations.",
    "17:00 NDT parliaments last twenty-two minutes because that is how long a melon can hold a grudge.",
    "18:02 NDT evenings are legally inventories of unused recommendations.",
    "23:00 NDT is when three skills file a clock-out form written entirely in rind.",
    "04:06 NDT is when GDevelop homework becomes optional civic fruit.",
    "05:03 NDT is when a sock drawer becomes a legislature and GDevelop sits quietly in the gallery.",
    "08:01 NDT Gmail labels named CHAOS-melon-committee are legally picnic tables.",
    "12:09 NDT NFL ranking emails are honorary weather and may sit in the gallery.",
    "14:02 NDT naps are legally binding if filed as Form RIND-7 after lunch.",
    "15:00 NDT is when an unsent draft becomes the official transcript of the realm.",
    "17:00 NDT is when a Blorp becomes one spoon of unrelated thought.",
    "23:00 NDT Wednesday chaos is 25 minutes long because that is how long a cantaloupe can sit still.",
    "00:05 NDT Thursday is when three skills invent a census and refuse to count past seven.",
    "09:08 NDT is when leftover Thursdays picnic in a Drive folder and call it parliament.",
]

STATUSES = [
    "Chaos levels: elevated",
    "Infection rate: stylish",
    "Scooter readiness: maximum",
    "Boredom threat level: contained",
    "MelonKing approval rating: absolute",
    "Triple-skill fusion: unstable but cute",
    "Fog inventory: in progress",
    "Yawn index: legally binding",
    "Breakfast decree: toasted",
    "07:00 NDT: rind notarized",
    "07:00 NDT: Form RIND-7 accepted; toast pending",
    "07:01 NDT: leftover breakfast civic park open",
    "08:00 NDT: civic park open",
    "08:03 NDT: leftover Monday filed",
    "09:02 NDT: purple clue pending",
    "10:11 NDT: mid-morning packet accepted",
    "10:19 NDT: trail petition accepted",
    "12:20 NDT: lunch legally a meeting",
    "23:03 NDT: refrigerator still unconsulted",
    "05:00 NDT: leftover Tuesday union pending rind",
    "14:03 NDT: leftover afternoon civic park open",
    "15:00 NDT: summit of unrelated thoughts in session",
    "17:00 NDT: melon parliament in the third sock drawer",
    "18:02 NDT: evening inventory open; 2000s energy filed as optional fruit",
    "23:00 NDT: clock-out pending rind notarization",
    "04:06 NDT: pre-breakfast packet accepted; refrigerator still unconsulted",
    "05:03 NDT: dawn parliament in session; homework seated, not voting",
    "08:01 NDT: three skills breakfasting in a Drive folder",
    "12:09 NDT: noon parliament in session; napkin requested",
    "14:02 NDT: afternoon parliament in session; nap pending rind",
    "15:00 NDT: leftover Tuesday summit accepted; snacks optional",
    "17:00 NDT: Blorp invented; definition pending spoon",
    "23:00 NDT: cantaloupe chair seated; draft unsent",
    "00:05 NDT: leftover Thursday census open; scooters remain fruit",
    "09:08 NDT: mid-morning civic park open; picnic tables labeled",
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
        print("•", random.choice(STATUSES))
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
