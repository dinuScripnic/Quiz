import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from quiz_functionality import QuizBrain

category = ['Any Category', 'General Knowledge', 'Entertainment: Books', 'Entertainment: Film', 'Entertainment: Music',
            'Entertainment: Musicals & Theatres', 'Entertainment: Television', 'Entertainment: Video Games',
            'Entertainment: Board Games', 'Science & Nature', 'Science: Computers', 'Science: Mathematics', 'Mythology',
            'Sports', 'Geography', 'History', 'Politics', 'Art', 'Celebrities', 'Animals', 'Vehicles',
            'Entertainment: Comics', 'Science: Gadgets', 'Entertainment: Japanese Anime & Manga',
            'Entertainment: Cartoon & Animations ']
text_style = ('Bahnschrift', 12, 'bold')
button_style = ('Bahnschrift', 9)
entry_style = ('Bahnschrift', 11)


def open_file():
    import json
    try:
        data = open('database.json')
        database = json.load(data)
        return database
    except FileNotFoundError:
        database = {}
        return database


def prepare_for_entry_name(event,  entry):
    entry.delete(0, tk.END)
    entry.configure(bg='white')


def prepare_for_entry_password(event,  entry):
    entry.delete(0, tk.END)
    entry.configure(bg='white', show='*')


def registration(name, password, repeat_password):
    global database, user_data
    user_name = name.get()
    user_password = password.get()
    user_repeat_password = repeat_password.get()
    if len(user_password) < 8:
        password.configure(bg='red')
        password.delete(0, "end")
        password.insert(0, 'Passwords to short')
        repeat_password.delete(0, "end")
    else:
        if user_name not in database:
            if user_password == user_repeat_password:
                database.update({user_name: {"password": user_password, "points": 135}})
                user_data = [user_name, database[user_name]]
                choose()
            else:
                password.configure(bg='red')
                password.delete(0, "end")
                repeat_password.configure(bg='red', show='')
                repeat_password.delete(0, "end")
                password.insert(0, 'Passwords does not match')
                repeat_password.insert(0, 'Passwords does not match')
        else:
            name.configure(bg='red')
            name.delete(0, "end")
            name.insert(0, 'User already exits')


def logging_in(name, password):
    global database
    global database, user_data
    user_name = name.get()
    user_password = password.get()
    if user_name in database:
        if user_password == database[user_name]['password']:
            user_data = [user_name, database[user_name]]
            return user_data
            choose()
        else:
            password.configure(bg='red', show='')
            password.delete(0, "end")
            password.insert(0, 'Wrong Password')
    else:
        name.configure(bg='red')
        name.delete(0, "end")
        name.insert(0, 'User not found')
        password.delete(0, "end")


def log_in_window():
    global log_window
    log_window = tk.Tk()
    log_window.title('QUIZ by DS')
    log_window.geometry('450x150+200+200')
    log_window.iconbitmap('icon.ico')

    welcome_text = tk.Label(log_window, text='Welcome to our quiz. Hope you\'ll have fun!', font=('Equinox', 15, 'bold'), fg='#471de3')

    work_sector = tk.Frame(log_window, highlightbackground="black", highlightthickness=1)
    name_label = tk.Label(work_sector, text='Name: ')
    name_label.configure(font=text_style)
    password_label = tk.Label(work_sector, text='Password: ')
    password_label.configure(font=text_style)
    name_entry = tk.Entry(work_sector)
    name_entry.configure(font=entry_style)
    name_entry.bind("<Button-1>", lambda e, entry=name_entry: prepare_for_entry_name(e, entry))
    password_entry = tk.Entry(work_sector)
    password_entry.configure(font=entry_style, show="*")
    password_entry.bind("<Button-1>", lambda e, entry=password_entry: prepare_for_entry_password(e, entry))
    register_button = tk.Button(work_sector, text='Register now!', command=register)
    register_button.configure(font=button_style)

    log_in_button = tk.Button(log_window, text='Log in', font=button_style, command=lambda name=name_entry, password=password_entry: logging_in(name, password))

    name_label.grid(row=0, column=0, padx=5, pady=3)
    password_label.grid(row=1, column=0, padx=5, pady=3)
    name_entry.grid(row=0, column=1, padx=5, pady=3)
    password_entry.grid(row=1, column=1, padx=5, pady=3)
    register_button.grid(row=2, column=0, padx=5, pady=3)

    welcome_text.pack()
    work_sector.pack()
    log_in_button.pack()

    tk.mainloop()


def register():
    global log_window
    register_window = tk.Toplevel(log_window)
    register_window.geometry('450x150+300+300')
    register_window.iconbitmap('icon.ico')

    register_message = tk.Label(register_window, text='Registering to our quiz!', font=('Equinox', 15, 'bold'), fg='#471de3')

    registration_sector = tk.Frame(register_window, highlightbackground="black", highlightthickness=1)
    name_label = tk.Label(registration_sector, text='Name: ')
    name_label.configure(font=text_style)
    password_label = tk.Label(registration_sector, text='Password: ')
    password_label.configure(font=text_style)
    password_label_confirm = tk.Label(registration_sector, text='Repeat Password: ')
    password_label_confirm.configure(font=text_style)
    name_entry = tk.Entry(registration_sector)
    name_entry.configure(font=entry_style)
    name_entry.bind("<Button-1>", lambda e, entry=name_entry: prepare_for_entry_name(e, entry))
    password_entry = tk.Entry(registration_sector)
    password_entry.configure(font=entry_style, show="*")
    password_entry.bind("<Button-1>", lambda e, entry=password_entry: prepare_for_entry_password(e, entry))
    password_entry_confirm = tk.Entry(registration_sector)
    password_entry_confirm.configure(font=entry_style, show="*")
    password_entry_confirm.bind("<Button-1>", lambda e, entry=password_entry_confirm: prepare_for_entry_password(e, entry))
    registration_button = tk.Button(register_window, text='Confirm', command=lambda name=name_entry, password=password_entry, repeat_password=password_entry_confirm: registration(name, password, repeat_password), font=button_style)

    name_label.grid(row=0, column=0, padx=5, pady=3)
    password_label.grid(row=1, column=0, padx=5, pady=3)
    password_label_confirm.grid(row=2, column=0, padx=5, pady=3)
    name_entry.grid(row=0, column=1, padx=5, pady=3)
    password_entry.grid(row=1, column=1, padx=5, pady=3)
    password_entry_confirm.grid(row=2, column=1, padx=5, pady=3)

    register_message.pack()
    registration_sector.pack()
    registration_button.pack()


def choose():
    global log_window, choosing
    try:
        log_window.destroy()
    except:
        pass
    choosing = tk.Tk()
    choosing.title('QUIZ by DS')
    choosing.geometry('350x220+300+300')
    choosing.iconbitmap('icon.ico')
    # nr questions
    number_label = tk.Label(choosing, text='Number of questions')
    nr_questions = tk.Scale(choosing, from_=1, to=50, orient=tk.HORIZONTAL)
    # difficulty
    difficulty_label = tk.Label(choosing, text=' Question\'s difficulty')
    difficulty_choose = tk.Scale(choosing, from_=1, to=3, orient=tk.HORIZONTAL)
    # topic
    topics_label = tk.Label(choosing, text='Topic')
    topics = ttk.Combobox(choosing, width=30, values=category)
    topics.current(0)
    generate = tk.Button(choosing, text='Generate Quiz', command=lambda number=nr_questions, difficulty=difficulty_choose, topic=topics: get_url(number, difficulty, topic))
    number_label.pack()
    nr_questions.pack()
    difficulty_label.pack()
    difficulty_choose.pack()
    topics_label.pack()
    topics.pack()
    generate.pack()

    choosing.mainloop()


def get_url(number, difficulty, topic):
    global database
    import requests
    number = '?amount='+str(number.get())
    difficulty = difficulty.get()
    if difficulty == 1:
        difficulty = '&difficulty=easy'
    elif difficulty == 2:
        difficulty = '&difficulty=medium'
    elif difficulty == 3:
        difficulty = '&difficulty=hard'
    topic = topic.get()
    if category.index(topic)+1 == 1:
        topic = ''
    else:
        topic = '&category='+str(category.index(topic)+1+7)
    url = 'https://opentdb.com/api.php'+number+difficulty+topic+'&type=multiple'
    questions = requests.get(url)
    questions = questions.json()
    return questions


class QuizInterface:

    def __init__(self, quiz_brain=QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("iQuiz App")
        self.window.geometry("850x530")

        # Display Title
        self.display_title()

        # Create a canvas for question text, and dsiplay question
        self.canvas = tk.Canvas(width=800, height=250)
        self.question_text = self.canvas.create_text(400, 125,
                                                     text="Question here",
                                                     width=680,
                                                     font=text_style
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        # Declare a StringVar to store user's answer
        self.user_answer = tk.StringVar()

        # Display four options (radio buttons)
        self.opts = self.radio_buttons()
        self.display_options()

        # To show whether the answer is right or wrong
        self.feedback = tk.Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback.place(x=300, y=380)

        # Next and Quit Button
        self.buttons()

        # Mainloop
        self.window.mainloop()

    def display_title(self):
        """To display title"""

        # Title
        title = tk.Label(self.window, text="iQuiz Application",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

        # place of the title
        title.place(x=0, y=2)

    def display_question(self):
        """To display the question"""

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def radio_buttons(self):
        """To create four options (radio buttons)"""

        # initialize the list with an empty list of options
        choice_list = []

        # position of the first option
        y_pos = 220

        # adding the options to the list
        while len(choice_list) < 4:

            # setting the radio button properties
            radio_btn = tk.Radiobutton(self.window, text="", variable=self.user_answer,
                                    value='', font=("ariel", 14))

            # adding the button to the list
            choice_list.append(radio_btn)

            # placing the button
            radio_btn.place(x=200, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return choice_list

    def display_options(self):
        """To display four options"""

        val = 0

        # deselecting the options
        self.user_answer.set(None)

        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in self.quiz.current_question.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    def next_btn(self):
        """To show feedback for each answer and keep checking for more questions"""

        # Check if the answer is correct
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Correct answer! \U0001F44D'
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = ('\u274E Oops! \n'
                                     f'The right answer is: {self.quiz.current_question.correct_answer}')

        if self.quiz.has_more_questions():
            # Moves to next to display next question and its options
            self.display_question()
            self.display_options()
        else:
            # if no more questions, then it displays the score
            self.display_result()

            # destroys the self.window
            self.window.destroy()

    def buttons(self):
        """To show next button and quit button"""

        # The first button is the Next button to move to the
        # next Question
        next_button = tk.Button(self.window, text="Next", command=self.next_btn,
                             width=10, bg="green", fg="white", font=("ariel", 16, "bold"))

        # placing the button on the screen
        next_button.place(x=350, y=460)

        # This is the second button which is used to Quit the self.window
        quit_button = tk.Button(self.window, text="Quit", command=self.window.destroy,
                             width=5, bg="red", fg="white", font=("ariel", 16, " bold"))

        # placing the Quit button on the screen
        quit_button.place(x=700, y=50)






# database = open_file()
# log_in_window()


