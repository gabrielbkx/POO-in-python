from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []

for question in question_data:
    questionText = question["question"]
    questionAnswer = question["correct_answer"]
    newQuestion = Question(q_text = questionText,q_answer = questionAnswer)
    questionBank.append(newQuestion)

quiz = QuizBrain(questionBank)

while quiz.stillHAsQuestion():
    quiz.nextQuestioon()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.questionNumber}")