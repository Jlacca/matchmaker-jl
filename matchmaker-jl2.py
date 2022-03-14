# Jeffrey Lacca
# Matchmaker LIte

from tkinter.messagebox import NO
from urllib import response


# Constants
INTRODUCTION = '''
Matchmaaker 2022

******************************************************
                    Matchmaker <3<3<3
          Helping you find ~~~luv~~~ since 2022
                    SweetHearts, Inc.
******************************************************

This nifty little code figures out if you and I are right for eachother.
You will answer 5 questions. To each question, answer 5
if you strongly agree, 4 if you agree, 3 if you neither
agree nor disagree, 2 if you disagree, and 1 if you
strongly disagree.

Let's get to it
'''
QUESTION = [
    'University of Alabama Football rocks!',
    'Blue Origin is better than SpaceX!',
    'Soda in a can is better than soda in a bottle!',
    'Goldendoodle is the best dog breed!',
    'Procrastination is good!',
]

COMPATABILITY_WEIGHTING = [
    # all questions are weighted at 20%
]
CR = [
    'Never gonna give you up!!',
    'So close!',
    'Sorry not today!'
]


DESIRED_RESPONSE = [
    5, # strongly agree
    1, # strongly disagree
    3, # neutral
    4, # agree
    2, # disagree
]

MAX_SCORE = 5 * len(QUESTION)

print(INTRODUCTION)

# Ask all quuestions

response = []
compatibility = []

for i in range(len(QUESTION)):
    while True:
        try:
            userResponse = int(input(QUESTION[i]))
            if userResponse>0 and userResponse<6:
                print("Response entered successfully...")
                break;
            else:
                print("Response should between 1 and 5...")      
        except ValueError:
            print("Please provide a whole number between 1 and 5...")
            continue

    response.append(userResponse)

    questionCompatibility = 5 - abs(userResponse - DESIRED_RESPONSE[i])
    compatibility.append(questionCompatibility)
    print("QUESTION %d compatibility: %d\n" % (i+1, questionCompatibility))

totalcompatibility = 0
for c in compatibility:
    totalcompatibility += c

totalcompatibility *= 100 / MAX_SCORE
print('Total Compatibility percentage : %d\n\n' % (totalcompatibility))
if totalcompatibility >= 90 and totalcompatibility<= 100:
    print (CR[0])
elif totalcompatibility >= 80 and totalcompatibility<= 89:
    print (CR[1])
else:
    print (CR[2])
    print ("")