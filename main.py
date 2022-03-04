from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"],question["answer"]))
#print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("End of quiz!. Hope you have enjoyed it.")
print(f"Your final score is  {quiz.score}/{quiz.question_number}.")

#Option 1
# is_continue = True
# while is_continue:
#     is_continue = quiz.next_question()



