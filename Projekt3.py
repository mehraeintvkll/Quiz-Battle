from rich.console import Console

console = Console()


fragen = [
    ("Choose the biggest number",["A) 10", "B) 20", "C) 15", "D) 12"],"B"),
    ("Choose the lowest number",["A) 10", "B) 20", "C) 15", "D) 12"],"A"),
    ("Choose the even number",["A) 10", "B) 21", "C) 15", "D) 12"],"D"),
    ("Choose the biggest number",["A) 25", "B) 30", "C) 15", "D) 20"],"B"),
    ("Choose the lowest number",["A) 8", "B) 18", "C) 5", "D) 12"],"C")
]


def show_menu():
    console.print("\n--- Main Menu ---", style="bold")
    print("1 - Start Game")
    print("2 - Exit")

    choice = input("Choose: ").strip()

    return choice


def show_question(frage, optionen):
    console.print(f"\n{frage}", style="bold")

    for option in optionen:
        print(option)


def play_game():
    punkte = 0
    richtige_antworten = 0

    for frage, optionen, richtig_antwort in fragen:

        show_question(frage, optionen)

        answer = input(" ").strip().upper()

        if answer == richtig_antwort:

            console.print("Richtig geantwortet", style="bold green")

            punkte += 10
            richtige_antworten += 1

        else:

            console.print("Falsch", style="bold red")

            punkte -= 3

    return punkte, richtige_antworten


def show_result(punkte, richtige_antworten):

    prozent = (richtige_antworten / len(fragen)) * 100

    console.print("\n--- Ergebnis ---", style="bold green")

    console.print(f"Deine Punkte: {punkte}", style="blue")

    console.print(f"Richtige Antworten: " f"{richtige_antworten} von {len(fragen)}", style="bold")

    console.print(f"Du hast {prozent}% richtig beantwortet.", style="bold purple")


def main():

    while True:

        choice = show_menu()

        if choice == "1":

            punkte, richtige_antworten = play_game()

            show_result(punkte, richtige_antworten)

        elif choice == "2":
            console.print("\nAuf Wiedersehen!", style="bold yellow")

            break

        else:
            console.print("Falsche Auswahl!", style="bold red")


main()
