from math import sqrt

class RecommendationEngine:
    """
     based on failure rate based weighting from UP (an irc user)
     Glossary
     =======
     total : total number of questions in each category
     failed: number of questions not answered in each category
     failrate: fraction of failed questions in each category
     weights: weights of the categories
     probs: probabilities of the categories
     delta: small offset to prevent division by zero
     recAvail: recommendation available (is false when all of the questions are asked)
     index: index of the next question 
     questions: array where all the questions are partioned according to category
     categoryOffsets: starting location of each category  in questions array
     asked: number of questions asked for each category
    """
    def __init__(self, questions):
        self.total = [0.0, 0.0, 0.0]
        self.failed = [0.0, 0.0, 0.0]
        self.failRate = [0.0, 0.0, 0.0]
        self.weights = [0.0, 0.0, 0.0]
        self.probs = [0.0, 0.0, 0.0]
        self.delta = 0.001
        self.recAvail = True
        self.nextCat = 0
        self.categoryOffsets = [0, 0, 0]
        self.asked = [0, 0, 0]
        self.questions = questions
        qi  = 0
        for q in questions:
            match q.difficulty:
                case "Easy": self.total[0] = self.total[0] + 1
                case "Moderate": self.total[1] = self.total[1] + 1
                case "Hard": self.total[2] = self.total[2] + 1
            if self.total[0] == 1:
                self.categoryOffsets[0] = qi
            elif self.total[1] == 1:
                self.categoryOffsets[1] = qi
            elif self.total[2] == 1:
                self.categoryOffsets[2] = qi
            qi = qi + 1
        self.index = 0

    def next_question(self):
        if self.index >= len(self.questions):
            return None
        if(self.recAvail == False):
            return None
        question = self.questions[self.index]
        return question


    def submit_answer(self, question, correct):

        """
        Called after every question.

        Later you can use this information to update
        your recommendation model.
        """
        
        match question.difficulty:
                case "Easy": 
                    self.asked[0] = self.asked[0] + 1
                case "Moderate":
                    self.asked[1] = self.asked[1] + 1
                case "Hard":
                    self.asked[2] = self.asked[2] + 1
        
        if correct==False:
            match question.difficulty:
                case "Easy": 
                    self.failed[0] = self.failed[0] + 1
                    self.failRate[0] = self.failed[0] / self.total[0]
                case "Moderate":
                    self.failed[1] = self.failed[1] + 1
                    self.failRate[1] = self.failed[1] / self.total[1]
                case "Hard":
                    self.failed[2] = self.failed[2] + 1
                    self.failRate[2] = self.failed[2] / self.total[2]
        
        wtsum = 0.0
        for k in range(0,3):
            wtConfidence = 1.0 / sqrt(1+self.asked[k])
            self.weights[k] = wtConfidence * max(0.0001, min(1.0 / (1.0 + self.failRate[k]), 1.0))
            wtsum = wtsum + self.weights[k]; 
        
        for k in range(0,3):
            self.probs[k] = self.weights[k]  / wtsum
            
        probsum = 0.0
        for i in range(0,3):
            if self.asked[i] >= self.total[i]:
                self.probs[i] = 0
            probsum = probsum + self.probs[i]

        print("Updated Probabilities")
        print("P(Ez) ", self.probs[0])
        print("P(Mo) ", self.probs[1])
        print("P(Hd) ", self.probs[2])
        
        if (probsum < 0.000001):
            self.recAvail = False
            return

        self.nextCat = self.probs.index(max(self.probs))
        self.recAvail = True
        self.index = self.categoryOffsets[self.nextCat] + self.asked[self.nextCat]
        return
