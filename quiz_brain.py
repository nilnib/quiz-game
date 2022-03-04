class QuizBrain:
    def __init__(self,qbank):
        self.question_number = 0
        self.question_list = qbank
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"Your current score is {self.score}/{self.question_number} ")
        print(f"The correct answer was {correct_answer}.")
        print("\n")


    def next_question(self):
        q_no  = self.question_number
        question = self.question_list[self.question_number].text
        user_answer = input(f"Q{self.question_number+1}: {question} (True/False)?: " ).title()
        correct_ans = self.question_list[self.question_number].answer
        self.question_number += 1
        self.check_answer(user_answer,correct_ans)


        # if user_answer == self.question_list[q_no].answer :
        #     print("You are correct")
        #     self.score += 1
        #     print(f"Your score is {self.score}/{q_no +1} ")
        # else:
        #     print("Sorry!You are wrong")
        #     print (f"Your score remained same {self.score}/{q_no +1}")


        #Option 1
        # if q_no == len(self.question_list)-1:
        #     print("End of quiz!")
        #     return False
        # else:
        #     self.question_number += 1
        #     print("Next Question:")
        #     return True

