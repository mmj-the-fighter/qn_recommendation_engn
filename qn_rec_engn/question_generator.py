from recommendation_engine import RecommendationEngine


class QuestionGenerator:

    def __init__(self, question_bank):

        self.engine = RecommendationEngine(
            question_bank.all_questions()
        )

    def next_question(self):
        return self.engine.next_question()

    def submit_answer(self, question, correct):
        self.engine.submit_answer(question, correct)