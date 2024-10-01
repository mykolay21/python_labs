from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_object = Question(question['question'],question['correct_answer'])
    question_bank.append(question_object)


# for i in question_bank:
#     print(i.text, i.answer)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have complited the quiz")
print(f"Your final score was :  {quiz.score} / {quiz.question_number}  ")
