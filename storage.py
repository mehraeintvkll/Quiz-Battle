import json
import random

from Engine import Question , ROUNDS 

QUESTIONS_PATH = "questions.json"

class QuestionBank:
    def def __init__(self, path: str = QUESTIONS_PATH ) -> None:
      with open(path, "r", encoding="utf-8") as f:
        data: Any = json.load(f)

        self.__questions: list[Question] = []
        for item in data:
            question: Question = Question(
                text = item["question"],
                options = item["options"],
                correct = item["correct"]
            )
            self.__questions.append(question)



    def count(self) -> int:
        return len(self.__questions)



    def pick(self , n: int = ROUNDS) -> list(Questions):
        return random.sample(self.__questions, k=n)