from questions import questions_list
import random


class Question:
    my_score = 0

    def __init__(self):
        key, value = random.choice(list(questions_list.items()))
        self.question = key
        self.answer = value

class Calculate(Question):
    def increment(self):
        self.my_score += 1
        return self.my_score

    def right_answer(self, answer, count):
        score = self.increment()
        print ("you got it right!")
        print (f"The correct answer was: {answer}")
        print (f"Your current score is: {score}/{count}")

    def wrong_answer(self, answer, count):
        print("That's wrong.")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.my_score}/{count}")
