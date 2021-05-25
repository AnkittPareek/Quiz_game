from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    i = question_data.index(item)
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))

quiz = QuizBrain(question_bank)
quiz.start_quiz()