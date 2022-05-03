import tkinter as tk
from tkinter import ttk
category = ['Any Category', 'General Knowledge', 'Entertainment: Books', 'Entertainment: Film', 'Entertainment: Music',
            'Entertainment: Musicals & Theatres', 'Entertainment: Television', 'Entertainment: Video Games',
            'Entertainment: Board Games', 'Science & Nature', 'Science: Computers', 'Science: Mathematics', 'Mythology',
            'Sports', 'Geography', 'History', 'Politics', 'Art', 'Celebrities', 'Animals', 'Vehicles',
            'Entertainment: Comics', 'Science: Gadgets', 'Entertainment: Japanese Anime & Manga',
            'Entertainment: Cartoon & Animations ']


class SettingsWindow:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('QUIZ by DS')
        self.window.geometry('350x220+300+300')
        self.window.iconbitmap('icon.ico')
        # nr questions
        number_label = tk.Label(self.window, text='Number of questions')
        nr_questions = tk.Scale(self.window, from_=1, to=50, orient=tk.HORIZONTAL)
        # difficulty
        difficulty_label = tk.Label(self.window, text=' Question\'s difficulty')
        difficulty_choose = tk.Scale(self.window, from_=1, to=3, orient=tk.HORIZONTAL)
        # topic
        topics_label = tk.Label(self.window, text='Topic')
        topics = ttk.Combobox(self.window, width=30, values=category)
        topics.current(0)
        generate = tk.Button(self.window, text='Generate Quiz',
                             command=lambda number=nr_questions, difficulty=difficulty_choose, topic=topics:
                             self.get_url(number, difficulty, topic))
        number_label.pack()
        nr_questions.pack()
        difficulty_label.pack()
        difficulty_choose.pack()
        topics_label.pack()
        topics.pack()
        generate.pack()

        tk.mainloop()

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
        url = 'https://opentdb.com/api.php' + number + difficulty + topic + '&type=multiple'
        questions = requests.get(url)
        questions = questions.json()
        return questions
