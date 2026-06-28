from question_bank import QuestionBank
from question_generator import QuestionGenerator


class Quiz:

    CHECK = "✓"
    CROSS = "✗"
    TROPHY = "🏆"
    QUESTION = "❓"

    def __init__(self):

        self.score = 0
        self.total = 0

        self.bank = QuestionBank()
        self.generator = QuestionGenerator(self.bank)

    def ask(self, question):

        print()
        print("=" * 70)
        print(f"{self.QUESTION}  Difficulty : {question.difficulty}")
        print("-" * 70)
        print(question.text)
        print()

        for i, option in enumerate(question.options, start=1):
            print(f"  {i}. {option}")

        while True:

            try:
                choice = int(input("\nYour answer (1-4): "))

                if 1 <= choice <= len(question.options):
                    break

            except ValueError:
                pass

            print(f"{self.CROSS} Invalid input. Please enter a number between 1 and 4.")

        correct = (choice - 1) == question.answer

        self.generator.submit_answer(question, correct)

        self.total += 1

        print()

        if correct:
            print(f"{self.CHECK} Correct!")
            self.score += 1
        else:
            print(f"{self.CROSS} Incorrect!")
            print(f"{self.CHECK} Correct Answer : {question.options[question.answer]}")

    def show_score(self):

        print()
        print("=" * 70)
        print(f"{self.TROPHY}  Quiz Finished")
        print("=" * 70)

        print(f"Score      : {self.score}/{self.total}")

        if self.total > 0:
            percentage = (self.score / self.total) * 100
            print(f"Percentage : {percentage:.1f}%")

        print("=" * 70)

    def run(self):

        print("=" * 70)
        print("              MCQ Quiz")
        print("=" * 70)

        while True:

            question = self.generator.next_question()

            if question is None:
                break

            self.ask(question)

        self.show_score()