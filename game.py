import random
import time


def print_slow(text, delay=0.03):
    """Print text slowly for a more engaging feel"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def get_player_choice():
    while True:
        print("\n" + "═" * 40)
        print("  Choose:  (r)ock  |  (p)aper  |  (s)cissors  ")
        print("═" * 40)

        choice = input("→ Your move: ").strip().lower()

        if choice in ['r', 'rock', 'p', 'paper', 's', 'scissors']:
            if choice.startswith('r'): return 'rock'
            if choice.startswith('p'): return 'paper'
            if choice.startswith('s'): return 'scissors'
        else:
            print("❌ Invalid choice! Please enter r, p, or s (or full word)")


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == 'rock' and computer == 'scissors') or \
            (player == 'scissors' and computer == 'paper') or \
            (player == 'paper' and computer == 'rock'):
        return "player"
    else:
        return "computer"


def print_result(player, computer, winner):
    print("\n" + "─" * 40)
    print(f"  You chose     : {player.upper()}")
    print(f"  Computer chose: {computer.upper()}")
    print("─" * 40)

    if winner == "tie":
        print(" " * 15 + "🤝 IT'S A TIE!")
    elif winner == "player":
        print(" " * 12 + "🎉 YOU WIN!")
    else:
        print(" " * 10 + "😔 Computer wins...")


def main():
    print("=" * 50)
    print(" " * 12 + "ROCK ✊  PAPER ✋  SCISSORS ✌️")
    print("=" * 50)
    print_slow("Welcome to Rock-Paper-Scissors!\n")

    player_score = 0
    computer_score = 0
    rounds = 0

    while True:
        rounds += 1
        print(f"\nRound {rounds}  |  Score → You: {player_score}  |  Computer: {computer_score}")

        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        winner = determine_winner(player_choice, computer_choice)

        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1

        print_result(player_choice, computer_choice, winner)

        # Ask to play again
        print("\n" + "─" * 40)
        play_again = input("Play another round? (y/n): ").strip().lower()
        if play_again not in ['y', 'yes', '']:
            break

    # Final summary
    print("\n" + "═" * 50)
    print(" " * 15 + "GAME OVER")
    print("═" * 50)
    print(f"Total rounds played: {rounds}")
    print(f"Final score:")
    print(f"  You       : {player_score}")
    print(f"  Computer  : {computer_score}")

    if player_score > computer_score:
        print(" " * 10 + "🏆 YOU ARE THE CHAMPION!")
    elif computer_score > player_score:
        print(" " * 8 + "Computer won this time... 😏")
    else:
        print(" " * 12 + "It's a draw overall!")

    print("\nThanks for playing! ✌️")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame ended. See you next time! 👋")