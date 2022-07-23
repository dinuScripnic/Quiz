import base64
import tkinter as tk
from tkinter import ttk
from main_page import MainPage
category = ['Any Category', 'General Knowledge', 'Entertainment: Books', 'Entertainment: Film', 'Entertainment: Music',
            'Entertainment: Musicals & Theatres', 'Entertainment: Television', 'Entertainment: Video Games',
            'Entertainment: Board Games', 'Science & Nature', 'Science: Computers', 'Science: Mathematics', 'Mythology',
            'Sports', 'Geography', 'History', 'Politics', 'Art', 'Celebrities', 'Animals', 'Vehicles',
            'Entertainment: Comics', 'Science: Gadgets', 'Entertainment: Japanese Anime & Manga',
            'Entertainment: Cartoon & Animations ']


class SettingsWindow:

    def __init__(self, user):
        self.user = user
        self.window = tk.Tk()
        self.window.title('QUIZ by DS')
        self.window.geometry('410x220+650+450')
        self.window.iconbitmap('icon.ico')
        title = tk.Label(self.window, text='Quiz settings', font=('Equinox', 15, 'bold'), fg='#471de3')
        title.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        # nr questions
        number_label = tk.Label(self.window, text='Number of questions', font=('Equinox', 12))
        number_label.grid(row=1, column=0, padx=5, pady=5)
        nr_questions = tk.Scale(self.window, from_=1, to=50, orient=tk.HORIZONTAL, length=220, width=15)
        nr_questions.grid(row=1, column=1, padx=3, pady=3)
        # difficulty
        difficulty_label = tk.Label(self.window, text=' Question\'s difficulty', font=('Equinox', 12))
        difficulty_label.grid(row=2, column=0, padx=5, pady=5)
        difficulty_choose = tk.Scale(self.window, from_=1, to=3, orient=tk.HORIZONTAL, length=220, width=15)
        difficulty_choose.grid(row=2, column=1, padx=3, pady=5)
        # topic
        topics_label = tk.Label(self.window, text='Topic', font=('Equinox', 12), width=15)
        topics_label.grid(row=3, column=0, padx=5, pady=5)
        topics = ttk.Combobox(self.window, width=30, values=category)
        topics.configure(width=30, font=('Equinox', 10))
        topics.current(0)
        topics.grid(row=3, column=1, padx=5, pady=5)
        generate = tk.Button(self.window, text='Generate Quiz',
                             command=lambda number=nr_questions, difficulty=difficulty_choose, topic=topics:
                             self.get_url(number, difficulty, topic), font=('Equinox', 10), width=10)
        # center the button
        generate.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.window.mainloop()

    def get_url(self, number, difficulty, topic):
        import requests
        number = '?amount=' + str(number.get())
        difficulty = difficulty.get()
        if difficulty == 1:
            difficulty = '&difficulty=easy'
        elif difficulty == 2:
            difficulty = '&difficulty=medium'
        elif difficulty == 3:
            difficulty = '&difficulty=hard'
        topic = topic.get()
        if category.index(topic) + 1 == 1:
            topic = ''
        else:
            topic = '&category=' + str(category.index(topic) + 1 + 7)
        url = 'https://opentdb.com/api.php' + number + difficulty + topic + '&type=multiple&encode=base64'
        questions = requests.get(url)
        questions = questions.json()
        questions = questions['results']
        # decode base 64
        for question in questions:
            question['question'] = base64.b64decode(question['question']).decode('utf-8')
            question['correct_answer'] = base64.b64decode(question['correct_answer']).decode('utf-8')
            question['incorrect_answers'] = [base64.b64decode(answer).decode('utf-8') for answer in question['incorrect_answers']]
        self.window.destroy()
        MainPage(self.user, questions)
