import random
import math


def get_int(prompt, default=None, min_val=None, max_val=None):
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            return default
        try:
            v = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if min_val is not None and v < min_val:
            print(f"Please enter a number >= {min_val}.")
            continue
        if max_val is not None and v > max_val:
            print(f"Please enter a number <= {max_val}.")
            continue
        return v


def compute_base_attempts(low, high):
    size = high - low + 1
    return math.ceil(math.log2(size))


def choose_difficulty(low, high):
    base = compute_base_attempts(low, high)
    print("\nChoose difficulty:")
    print(f"  1) Easy   ({base + 3} attempts)")
    print(f"  2) Normal ({base} attempts)")
    print(f"  3) Hard   ({max(1, base - 2)} attempts)")
    print("  4) Custom")
    choice = get_int("Select 1-4 (default 2): ", default=2, min_val=1, max_val=4)
    if choice == 1:
        return "Easy", base + 3, 0.75
    if choice == 2:
        return "Normal", base, 1.0
    if choice == 3:
        return "Hard", max(1, base - 2), 1.5
    # custom
    custom = get_int("Enter number of attempts you want: ", min_val=1)
    return "Custom", custom, 1.0


def play_game():
    print("\nWelcome to the Number Guessing Game!")
    print("Press Enter to accept defaults when prompted.")
    low = get_int("Minimum number (default 1): ", default=1)
    high = get_int("Maximum number (default 100): ", default=100, min_val=low + 1)

    difficulty_name, max_attempts, difficulty_multiplier = choose_difficulty(low, high)

    secret = random.randint(low, high)
    attempts_used = 0
    used_even_hint = False

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"Difficulty: {difficulty_name} — you have {max_attempts} attempts.")

    while attempts_used < max_attempts:
        attempts_left = max_attempts - attempts_used
        print(f"\nAttempt {attempts_used + 1}/{max_attempts} — {attempts_left} left")
        print(f"Current range: {low} to {high}")

        # free even/odd hint once
        if not used_even_hint:
            h = input("Want a free even/odd hint? (y/n): ").strip().lower()
            if h == 'y':
                print("Hint: The number is EVEN." if secret % 2 == 0 else "Hint: The number is ODD.")
                used_even_hint = True

        # narrow-range hint costs 3 attempts
        if attempts_left >= 4:
            h2 = input("Want to narrow the range (costs 3 attempts)? (y/n): ").strip().lower()
            if h2 == 'y':
                size = high - low + 1
                half = size // 2
                if half > 0:
                    # Fix: Ensure we don't remove the range containing the secret
                    new_low_candidate = low + half
                    # Range to remove if we remove low: [low, new_low_candidate - 1]
                    
                    # If secret is in the lower half, we MUST remove the upper half
                    if secret < new_low_candidate:
                         remove_low = False
                    else:
                         # Secret is in the upper half (or exactly on boundary depending on logic), remove lower
                         remove_low = True

                    if remove_low:
                        new_low = new_low_candidate
                        print(f"Narrowed range: removing {low}-{new_low - 1}")
                        low = new_low
                    else:
                        new_high = high - half
                        print(f"Narrowed range: removing {new_high + 1}-{high}")
                        high = new_high
                    attempts_used += 3
                    continue

        # get guess
        guess = get_int(f"Enter your guess ({low}-{high}): ", min_val=low, max_val=high)
        attempts_used += 1

        if guess == secret:
            print(f"\nCorrect! You guessed the number in {attempts_used} attempts.")
            score = max(0, (max_attempts - attempts_used)) * difficulty_multiplier
            return True, attempts_used, score

        # give directional and distance hints
        if guess < secret:
            print("Too low.")
            low = max(low, guess + 1)
        else:
            print("Too high.")
            high = min(high, guess - 1)

        # distance hint
        dist = abs(secret - guess)
        if dist <= 3:
            print("You're HOT! Very close.")
        elif dist <= 10:
            print("You're warm.")
        else:
            print("You're cold.")

    # out of attempts
    print(f"\nOut of attempts! The number was {secret}.")
    return False, attempts_used, 0


def main():
    games_played = 0
    games_won = 0
    total_score = 0

    while True:
        games_played += 1
        print('\n' + '=' * 50)
        print(f"Game #{games_played}")
        print('=' * 50)
        won, used, score = play_game()
        if won:
            games_won += 1
            total_score += score
            print(f"You earned {score:.1f} points this round.")
        else:
            print("No points this round.")

        print(f"Current record: {games_won} wins out of {games_played}")
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            break

    print('\nFinal statistics')
    print('-' * 20)
    print(f"Games played: {games_played}")
    print(f"Games won:    {games_won}")
    print(f"Total score:  {total_score:.1f}")
    if games_played:
        print(f"Win rate:     {games_won / games_played * 100:.1f}%")
    print("Thanks for playing!")

if __name__ == '__main__':
    main()