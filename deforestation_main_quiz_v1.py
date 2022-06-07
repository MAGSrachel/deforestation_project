score = 0
# the dictionary for the quiz
quiz = {'question': 'What is the cause of deforestation?', 'answers': 'a', 'question2':
        'Why is the forest important?', 'answer2': 'b', 'question3': 'Why do deforestation happen?', 'answer3': 'c',
        'question4': 'What are the aftermath of the effects', 'answer4': 'd', 'question5': 'How to reduce '
                                                                                           'deforestation?',
        'answer5': 'e', 'question6': 'Why should be care about deforestation?', 'answer6': 'f'}

# list of answers where the user will see the list of answers
list_of_answer = ["A = Human activity", "B = The forest is a water cycle, soil, home to many animals and the source of"
                                        "oxygen, water and clean water which is what living beings need to survive."
                                        "erosion, and act as an important buffer against climate change.",
                  "C = The reasons for deforestation are logging, agriculture, cattle ranching, overpopulation, etc.",
                  "D = Plant a tree, use less paper, reuse paper or cardboard"]

# main


user_question = input(quiz['question'])
if user_question == quiz['answers']:
    score += 1
    print("Correct! ")
elif user_question == quiz:
    print("Wrong answer")
else:
    print("Please choose one of the option")

user_question = input(quiz['question2'])
if user_question == quiz['answer2']:
    print("Correct! ")
    score += 1
elif user_question == quiz:
    print("Wrong answer")
else:
    print("Please choose one of the option")

user_question = input(quiz['question3'])
if user_question == quiz['answer3']:
    score += 1
    print("Correct! ")
else:
    print("Wrong answer")

user_question = input(quiz['question4'])
if user_question == quiz['answer4']:
    score += 1
    print("Correct! ")
else:
    print("Wrong answer")

user_question = input(quiz['question5'])
if user_question == quiz['answer5']:
    score += 1
    print("Correct! ".format(score))
else:
    print("Wrong answer")

user_question = input(quiz['question6'])
if user_question == quiz['answer6']:
    score += 1
    print("Correct! ".format(score))
else:
    print("Wrong answer")

print("You have {}/6".format(score))
