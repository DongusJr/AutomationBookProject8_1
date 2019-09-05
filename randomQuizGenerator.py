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

     #TODO: Shuffle the order of the states.

     #TODO: Loop through all 50 states, making question for each.