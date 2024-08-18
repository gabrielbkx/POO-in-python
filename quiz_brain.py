class QuizBrain():

    def __init__(self,q_list):
        self.questionNumber = 0
        self.score = 0
        self.questionList = q_list
    def nextQuestioon(self):
        currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber += 1
        userAnswer = input(f"Q{self.questionNumber} : {currentQuestion.text}: (true/false): ")
        self.checkanswer(userAnswer,currentQuestion.answer)

    def stillHAsQuestion(self):
        return self.questionNumber < len(self.questionList)

    def checkanswer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it!")
        else:
            print("That's wrong!")
        print(f"The correct answer is {correct_answer}")
        print(f"yor current score is: {self.score}/{self.questionNumber}")
        print("\n")
