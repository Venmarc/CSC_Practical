# Number-G-G

A fun and interactive number guessing game with multiple difficulty levels, scoring, hints, and statistics tracking.

## Features

- **Dynamic Difficulty Levels:** Easy, Normal, Hard, and Custom
- **Smart Attempt Calculation:** Attempts are dynamically calculated based on the number range using logarithmic complexity (ceil(log2(range)))
- **Scoring System:** Earn points based on difficulty level and attempts remaining
- **Hint System:**
  - Free even/odd hint (use once per game)
  - Range-narrowing hint (costs 3 attempts)
  - Directional feedback (too high/too low)
  - Distance-based feedback (hot/warm/cold)
- **Input Validation:** Robust error handling for invalid inputs
- **Customizable Range:** Set your own minimum and maximum numbers
- **Session Statistics:** Tracks wins, losses, total score, and win rate
- **Replay Mode:** Play multiple games and keep running stats

## How to Play

1. Run the game:
   ```bash
   python Number-guessing-game.py
   ```

2. Set your number range (or press Enter for defaults 1-100)

3. Choose a difficulty level:
   - **Easy:** Base attempts + 3 (score multiplier: 0.75x)
   - **Normal:** Base attempts (score multiplier: 1.0x)
   - **Hard:** Base attempts - 2 (score multiplier: 1.5x)
   - **Custom:** Choose your own number of attempts

4. Make your guesses and use hints strategically

5. Keep track of your score across multiple rounds

## Difficulty Examples

For a range of 1-100:
- Base attempts = ceil(log2(100)) = 7
- Easy: 10 attempts
- Normal: 7 attempts
- Hard: 5 attempts

For a range of 1-1000:
- Base attempts = ceil(log2(1000)) = 10
- Easy: 13 attempts
- Normal: 10 attempts
- Hard: 8 attempts

## Scoring

Points are calculated as: `(Attempts Remaining) × Difficulty Multiplier`

- Win with fewer attempts on higher difficulty = more points!

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library: `random`, `math`)
