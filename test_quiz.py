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

# Make 35 different quizzes
for quiz_num in range(35):
    # Create quiz and anwser sheet txt files
    question_file = open("capitalsquiz%s.txt" % (quiz_num + 1), "w")
    anwser_key_file = open("capitalquiz_anwsers%s.txt" % (quiz_num + 1), "w")
    # Make template
    question_file.write("Name:\n\nDate:\n\nPeriod\n\n")
    question_file.write((" "*20) + "State Capitals Quiz (Form%s)" % (quiz_num + 1))
    question_file.write("\n\n")
    #Make list of states, randomize
    states = list(capitals.keys())
    random.shuffle(states)
    # Make for loop with 50 questions
    for question_num in range(50):
    # Get the correct, anwser and 3 wrong anweser, put them in a new list with anweser options, randomize
        correct_anwser = capitals[states[question_num]]
        wrong_anwsers = list(capitals.values())
        del wrong_anwsers[wrong_anwsers.index(correct_anwser)]
        question_options = random.sample(wrong_anwsers, 3)
        question_options = question_options + [correct_anwser]
        random.shuffle(question_options)
    # 4 range for loop with anwser options and question
        question_file.write("%s. What is the capital of %s.\n" % (question_num + 1, states[question_num]))
        for i in range(4):
            question_file.write("%s. %s\n" % ("ABCD"[i], question_options[i]))
        question_file.write("\n")
        anwser_key_file.write("%s. %s\n" % ((question_num + 1), "ABCD"[question_options.index(correct_anwser)]))

question_file.close()
anwser_key_file.close()