import json
from pathlib import Path

from question import Question


class QuestionBank:

    def __init__(self, question_directory="questions"):

        self.question_directory = Path(question_directory)

        self.easy = self.load("easy.json", "Easy")
        self.moderate = self.load("moderate.json", "Moderate")
        self.hard = self.load("hard.json", "Hard")

    def load(self, filename, difficulty):

        with open(self.question_directory / filename, encoding="utf-8") as f:
            data = json.load(f)

        questions = []

        for q in data:
            questions.append(
                Question(
                    difficulty,
                    q["text"],
                    q["options"],
                    q["answer"]
                )
            )

        return questions

    def all_questions(self):
        return self.easy + self.moderate + self.hard