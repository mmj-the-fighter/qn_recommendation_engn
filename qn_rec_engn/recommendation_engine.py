class RecommendationEngine:

    """
    Replace this class with your adaptive recommendation algorithm.
    """

    def __init__(self, questions):

        self.questions = questions
        self.index = 0

    def next_question(self):

        if self.index >= len(self.questions):
            return None

        question = self.questions[self.index]

        self.index += 1

        return question

    def submit_answer(self, question, correct):

        """
        Called after every question.

        Later you can use this information to update
        your recommendation model.
        """

        pass