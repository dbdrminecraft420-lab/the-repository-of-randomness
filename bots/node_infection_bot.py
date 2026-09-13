#!/usr/bin/env python3
"""Node Infection Bot — tiny plague status reporter for MelonKing systems."""

import random
import sys

def snapshot():
    sane = random.randint(8, 45)
    infected = random.randint(15, 60)
    recovered = random.randint(5, 35)
    total = sane + infected + recovered
    return sane, infected, recovered, total

def main():
    s, i, r, t = snapshot()
    print("NODE INFECTION BOT")
    print("=" * 36)
    print(f"  Sane:      {s:3d}  ({100*s//t}%)")
    print(f"  Infected:  {i:3d}  ({100*i//t}%)")
    print(f"  Changed:   {r:3d}  ({100*r//t}%)")
    print()
    if i > s:
        print("  Status: MelonKing advances.")
    elif i == 0:
        print("  Status: Temporary containment.")
    else:
        print("  Status: Contested territory.")
    print()
    print("Click more nodes. Watch chaos spread.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
