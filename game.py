from rich.console import Console
from engine import Question, Match
import time

console = Console()


questions = [

    Question(
        "Choose the biggest number",
        ["A) 10", "B) 20", "C) 15", "D) 12"],
        "B"
    ),

    Question(
        "Choose the lowest number",
        ["A) 10", "B) 20", "C) 15", "D) 12"],
        "A"
    ),

    Question(
        "Choose the even number",
        ["A) 10", "B) 21", "C) 15", "D) 12"],
        "D"
    ),

    Question(
        "Choose the biggest number",
        ["A) 25", "B) 30", "C) 15", "D) 20"],
        "B"
    ),

    Question(
        "Choose the lowest number",
        ["A) 8", "B) 18", "C) 5", "D) 12"],
        "C"
    )
]


def show_question(question):

    console.print(f"\n{question.text}", style="bold cyan")

    for option in question.options:
        print(option)


def main():

    console.print("=== Quiz Game ===", style="bold green")

    player1 = input("Player 1 Name: ")
    player2 = input("Player 2 Name: ")

    match = Match(player1, player2, questions)

    while not match.is_over():

        question = match.start_round()

        show_question(question)

        for player in match.players:

            console.print(f"\n{player}'s turn", style="yellow")

            start = time.time()

            answer = input("Answer: ").strip().upper()

            elapsed = time.time() - start

            match.submit(player, answer, elapsed)

        match.resolve_round()

        console.print("\nScores:", style="bold")

        for player in match.players:
            console.print(
                f"{player}: {match.scores[player]}",
                style="green"
            )

    winner = match.winner()

    console.print("\n=== Result ===", style="bold blue")

    if winner:
        console.print(f"Winner: {winner}", style="bold green")
    else:
        console.print("Draw!", style="bold yellow")


main()