ROUNDS: int = 5 # هر مسابقه چند راند
TIME_LIMIT: int = 30 # مهلت هر جواب، به ثانیه
POINTS: int = 10 # امتیاز جواب درست
SPEED_BONUS: int = 3 # بونوس سریع‌ترین درست‌جواب

class Question:
    def __init__(self, text: str, options: list[str], correct: str) -> None:
        self.__text: str = text
        self.__options: list[str] = options
        self.__correct: str = correct

    def is_correct(self, choice: str) -> bool:
        return choice.strip().upper() == self.__correct

    def correct_text(self) -> str:
        return self.__options["ABCD".index(self.__correct)]

class Match:
    def __init__(self, player1: str, player2: str, questions: list[Question]) -> None:
        if player1 == player2:
            raise ValueError("Unique Name per Player!")

        self.__players: list[str] = [player1, player2]
        self.__questions: list[Question] = questions
        self.__scores: dict[str , int] = {player1:0 , player2:0}
        self.__round: int = 0
        self.__answers: dict = {}

    def start_round(self):
        self.__round += 1
        self.__answers = {}
        return self.__questions[self.__round - 1]

    def submit(self, player: str, choice: str, elapsed: float) -> None :
        self.__answers[player] = (choice, elapsed)

    def resolve_round(self) -> None:
        question: Question = self.__questions[self.__round - 1]

        for player in self.__players:
            choice, elapsed = self.__answers[player]
            
            if elapsed > TIME_LIMIT:
                self.__scores[player] += 0

            elif question.is_correct(choice):
                self.__scores[player] += POINTS

    def is_over(self) -> bool:
        return self.__round > ROUNDS

    def winner(self) -> str | None:
        player1, player2 = self.__palyers
        
        if self.__scores[player1] == self.__scores[player2]:
            return None

        if self.__scores[player1] > self.__scores[player2]:
            return player1
        else:
            return player2

            