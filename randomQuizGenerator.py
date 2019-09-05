#! python
#randomQuizGenerator.py - A project from the Automate the borings stuff in Python

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
 'Wyoming': 'Cheyen'}

#Create 35 different quizzes
 for quiz_num in range(35):
     #TODO: Create the quiz and anwser key files.
     # Make quiz and anwser_key files
     quiz_file = open('capitalsquiz%s.txt' % (quiz_num + 1), 'w')
     anweser_key_file = open('capitalquiz_anwsers%s.txt' % (quiz_num + 1), 'w')

    quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quiz_file.write((" " * 20) + "State Capitals Quiz (Form% s)" % (quiz_num + 1), "w")
    quiz_file.write("\n\n")

    #Make a list of the capitals
    states = list(capitals.keys())
    random.shuffle(states)  #shuffle them
     #TODO: Write out the header for the quiz.
     # Loop through the 50 questions and make 1 right anwser and 3 wrong anwsers
     for question_num in range(50):
         correct_anwser = capitals[states[question_num]]
         wrong_anwsers = list(capitals.values())
         del wrong_anwsers[wrong_anwsers.index(correct_anwser)]  # Remove the right anwser from the wrong anwsers
         wrong_anwsers = random.sample(wrong_anwsers, 3)         # Take 3 wrong anwser from the list
         anwser_options = wrong_anwsers + [correct_anwser]       # Add the wrong anwsers and add the correct anwser
         random.shuffle(anwser_options)                          # Shuffle the options so the correct anwser is not always D

     #TODO: Shuffle the order of the states.

     #TODO: Loop through all 50 states, making question for each.