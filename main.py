from my_questions_list import Question, Calculate
from questions import questions_list
cal = Calculate()
game_on= True
Q = 1
no_repeat = []
questions_len = len(questions_list)
while game_on:
    if Q > questions_len:
        print(f"Thank you for playing the Quiz! Your final score is {cal.my_score}/{Q - 1}")
        break
    game = Question()
    question = game.question
    while question in no_repeat:
        game = Question()
        question = game.question
    # response = input(f"Q.{Q}: {game.question} (True/False): ")
    response = input(f"Q.{Q}: {question} (True/False): ")
    if response == game.answer:
        cal.right_answer(game.answer, Q)
        Q+=1
        no_repeat.append(question)
    elif response == "off":
        print (f"Thank you for playing the Quiz! Your final score is {cal.my_score}/{Q-1}")
        game_on = False
    else:
        cal.wrong_answer(game.answer, Q)
        Q += 1
        no_repeat.append(question)
