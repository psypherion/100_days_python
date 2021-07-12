from question_model import Question
from data import question_data_2
from quiz_brain import QuizBrain
from art import quiz_logo, welcome
print(welcome)
print(quiz_logo)
question_bank = []
for i in range (0, len(question_data_2)) :
    dict_ = question_data_2[i]
    q_text = dict_['question']
    q_ans = dict_['correct_answer']
    new_question = Question(q_text,q_ans)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
while quiz.still_has_question() :
    quiz.next_question()
print("You've completed the quiz . ")
print(f"your final score was : {quiz.score}/{quiz.question_number}")