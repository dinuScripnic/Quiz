import scripnic_exercise_2_1 as se


# ask about nr of questions
def get_nr_question():
    """
    Asks the user about the number of question he wants.
    Return a string which is then put in url.
    """
    while True:
        try:
            nr_question = int(input('\nEnter number of questions: '))
            if (nr_question > 0) and (nr_question <= 50):
                nr_question = '?amount='+str(nr_question)
                break
            else:
                print('Number of questions should be less or equal to 50!')
        except ValueError:
            print('You have to enter a number!!!')
    return nr_question


def get_difficulty():
    """
    Asks the user about the difficulty of question he wants.
    Return a string which is then put in url.
    """   
    while True:
        try:
            difficulty = int(input('\nEnter 1 for Easy, 2 for Medium and 3 for Hard: '))
            if difficulty == 1:
                difficulty = '&difficulty=easy'
                break
            elif difficulty == 2:
                difficulty = '&difficulty=medium'
                break
            elif difficulty == 3:
                difficulty = '&difficulty=hard'
                break
            else:
                print('Invalid input, try once again!')
        except ValueError:
            print('You have to enter a number!!!')
    return difficulty


def get_topic(): 
    """
    Asks the user about the topic of question he wants.
    Return a string which is then put in url.
    """   
    # all the topics from which the user can choose
    print('\n1. Any Category\n2. General Knowledge\n3. Entertainment: Books\n4. Entertainment: Film\n5. Entertainment: Music\n6. Entertainment: Musicals & Theatres\n7. Entertainment: Television\n8. Entertainment: Video Games\n9. Entertainment: Board Games\n10. Science & Nature\n11. Science: Computers\n12. Science: Mathematics\n13. Mythology\n14. Sports\n15. Geography\n16. History\n17. Politics\n18. Art\n19. Celebrities\n20. Animals\n21. Vehicles\n22. Entertainment: Comics\n23. Science: Gadgets\n24. Entertainment: Japanese Anime & Manga\n25. Entertainment: Cartoon & Animations ')
    while True:
        try:
            topic = int(input('\nTopic: '))
            if topic == 1:
                topic = ''
                break   
            elif topic == 2:
                topic = '&category=9'
                break
            elif topic == 3:
                topic = '&category=10'
                break
            elif topic == 4:
                topic = '&category=11'
                break
            elif topic == 5:
                topic = '&category=12'
                break
            elif topic == 6:
                topic = '&category=13'
                break
            elif topic == 7:
                topic = '&category=14'
                break
            elif topic == 8:
                topic = '&category=15'
                break
            elif topic == 9:
                topic = '&category=16'
                break
            elif topic == 10:
                topic = '&category=17'
                break
            elif topic == 11:
                topic = '&category=18'
                break
            elif topic == 12:
                topic = '&category=19'
                break
            elif topic == 13:
                topic = '&category=20'
                break
            elif topic == 14:
                topic = '&category=21'
                break
            elif topic == 15:
                topic = '&category=22'
                break
            elif topic == 16:
                topic = '&category=23'
                break
            elif topic == 17:
                topic = '&category=24'
                break
            elif topic == 18:
                topic = '&category=25'
                break
            elif topic == 19:
                topic = '&category=26'
                break
            elif topic == 20:
                topic = '&category=27'
                break
            elif topic == 21:
                topic = '&category=28'
                break
            elif topic == 22:
                topic = '&category=29'
                break
            elif topic == 23:
                topic = '&category=30'
                break
            elif topic == 24:
                topic = '&category=31'
                break
            elif topic == 25:
                topic = '&category=32'
                break
            else:
                print('Invalid input, try once again!')

        except ValueError:
            print('You have to enter a number!!!')
    return topic


# get data from api
def get_questions(url):
    """
    get_questions(url)
    requires an url, from where it takes all the data and 
    """
    import requests
    print('Processing request...')
    questions = requests.get(url)
    questions = questions.json()
    return questions


def display_questions(questions, user_data):
    """
    display_question(file,data)
    file: a json file
    data: user_data
    Makes all the manipulations with quiz
    1. Displays the question
    2. Shuffle the results
    3. Ask user about result(u have to enter the number of answer)
    4. Checks if the result is right
    5. Calculate points
    """
    import random
    for question in questions['results']:
        print(f"\n{question['question']}")
        print()
        results = [values for values in question['incorrect_answers']]
        # i wanted to make it in one line, but if i put append or extend to list comprehension it gives result none
        results.append(question['correct_answer'])
        # shuffle answers
        random.shuffle(results)
        nr = 1
        for result in results:
            print(f'{nr}. {result}')
            nr += 1
        print()
        while True:
            try:
                response = int(input('Enter your answer: '))
                if response in range(0, 5) and results[response-1] in question['correct_answer']:
                    # point count
                    user_data[1]['points'] += 5
                    print(f"Correct! You now have {user_data[1]['points']} points.")
                    break
                elif response in range(1, 5) and results[response-1] in question['incorrect_answers']:
                    # point count
                    user_data[1]['points'] -= 3
                    print(f"Wrong! You now have {user_data[1]['points']}\nCorrect answer: {question['correct_answer']}")
                    break
                elif (response-1) not in range(1, 5):
                    print('Invalid input! Please, repeat your input!')
            except ValueError:
                print('You have to enter a number!!!')
    print('\nEnd of Quiz')
    print(f"\nGoodbye {user_data[0]}. Your current score ({user_data[1]['points']}) has been stored.")
    return user_data


def save_results(database, log_in, user_data):
    """
    save_results(file,user_name,user_data)
    Saves all the changes
    """
    database.update({log_in: user_data})


def welcome(name, points):
    """
    Welcomes user
    """
    print(f"\n\nWelcome to the Quiz {name}. You currently have {points} points.")


# open database
database = se.open_file()
# log in, get user data
user_data = se.main(database)
# welcome user
welcome(user_data[0], user_data[1]['points'])
# ask nr of question
nr_question = get_nr_question()
# ask difficulty
difficulty = get_difficulty()
# ask topic
topic = get_topic()
# create api
url = 'https://opentdb.com/api.php'+nr_question+difficulty+topic+'&type=multiple'
# get data from api
questions = get_questions(url)
# display question to user
display_questions(questions, user_data)
# save results
save_results(database, user_data[0], user_data[1])
# save data in database
se.save_file(database)
