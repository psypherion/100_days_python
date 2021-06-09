'''
This Module are made to :
1.Ask The question
2.Check If the answer was correct
3.check if we are already in the end of the quiz
'''
class QuizBrain :
    def __init__(self,question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    def next_question(self):
        item = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {item.text}. (True/False)? : ")
        self.check_answer(user_answer,item.answer)
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Right!")
        else :
            print("Fuck Off")
            print(f"Correct Answer was : {correct_answer}")
        print(f"Your Current Score Is : {self.score}/{self.question_number}")