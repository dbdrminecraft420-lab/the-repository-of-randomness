# the-repository-of-randomness

A sanctuary for chaos, scooters, and the MelonKing.

## Contents

| File | What it is |
|------|------------|
| `melonking-plague-game.html` | Interactive chaos infection game (open in browser) |
| `bots/melonking_bot.py` | Command-line MelonKing Chaos Bot |
| `.github/workflows/chaos-bot.yml` | GitHub Action that runs the bot on a schedule |

## Play the game

Open `melonking-plague-game.html` in any browser:
- Click nodes to infect them
- Press **Start Simulation**
- Watch chaos spread

## Run the bot locally

```bash
python bots/melonking_bot.py          # full chaos report
python bots/melonking_bot.py --decree # one royal decree
python bots/melonking_bot.py --plague # fake plague snapshot
python bots/melonking_bot.py --status # realm status
```

## GitHub Action

The chaos bot runs automatically:
- Every Sunday (scheduled)
- On every push to `main`
- Manually from the **Actions** tab (workflow_dispatch)

---

*Long live the scooters.*
