from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    questions = Question(question["text"], question["answer"])
    question_bank.append(questions)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've competed the quiz")
print(f"Your final score was {quiz.score} / {quiz.question_number}")





