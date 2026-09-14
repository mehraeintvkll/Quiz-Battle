ROUNDS: int = 5
TIME_LIMIT: int = 30
POINTS: int = 10
SPEED_BONUS: int = 3


class Question:
    def __init__(self, text: str, options: list[str], correct: str) -> None:
        self.__text: str = text
        self.__options: list[str] = options
        self.__correct: str = correct

    def is_correct(self, choice: str) -> bool:
        return choice.strip().upper() == self.__correct

    def correct_text(self) -> str:
        return self.__options["ABCD".index(self.__correct)]

    @property
    def text(self):
        return self.__text

    @property
    def options(self):
        return self.__options


class Match:
    def __init__(self, player1: str, player2: str, questions: list[Question]) -> None:

        if player1 == player2:
            raise ValueError("Unique Name per Player!")

        self.__players = [player1, player2]
        self.__questions = questions
        self.__scores = {player1: 0, player2: 0}

        self.__round = 0
        self.__answers = {}

    def start_round(self):
        self.__round += 1
        self.__answers = {}

        return self.__questions[self.__round - 1]

    def submit(self, player: str, choice: str, elapsed: float) -> None:
        self.__answers[player] = (choice, elapsed)

    def resolve_round(self) -> None:

        question = self.__questions[self.__round - 1]

        for player in self.__players:

            choice, elapsed = self.__answers[player]

            if elapsed > TIME_LIMIT:
                continue

            if question.is_correct(choice):
                self.__scores[player] += POINTS


        correct_players = []

        for player in self.__players:

            choice, elapsed = self.__answers[player]

            if elapsed <= TIME_LIMIT and question.is_correct(choice):
                correct_players.append((player, elapsed))

        if len(correct_players) == 2:

            correct_players.sort(key=lambda x: x[1])

            fastest_player = correct_players[0][0]

            self.__scores[fastest_player] += SPEED_BONUS

    def is_over(self) -> bool:
        return self.__round >= ROUNDS

    def winner(self):

        player1, player2 = self.__players

        if self.__scores[player1] == self.__scores[player2]:
            return None

        if self.__scores[player1] > self.__scores[player2]:
            return player1

        return player2

    @property
    def players(self):
        return self.__players

    @property
    def scores(self):
        return self.__scores