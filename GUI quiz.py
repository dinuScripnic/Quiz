import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
    quiz(user_data, questions)


def quiz(user_data, questions):
    def check():
        choice = check_var.get()
        output = 'none'
        if choice == 1:
            output = results[0]
        elif choice == 2:
            output = results[1]
        elif choice == 3:
            output = results[2]
        elif choice == 4:
            output = results[3]
        print(output)
    import random
    global choosing
    try:
        choosing.destroy()
    except:
        pass
    game = tk.Tk()
    game.title('QUIZ by DS')
    game.geometry('450x150+200+200')
    game.iconbitmap('icon.ico')
    info = tk.Label(game, text=f'Welcome to the Quiz {user_data[0]}. Have fun!', font=text_style)
    info.pack()
    for question in questions['results']:
        check_var = tk.IntVar()
        game_area = tk.Frame(game, highlightbackground="black", highlightthickness=1)
        question_text = tk.Label(game_area, text=question['question'])
        question_text.pack()
        results = [values for values in question['incorrect_answers']]
        results.append(question['correct_answer'])
        random.shuffle(results)
        tk.Radiobutton(game_area, text=results[0], variable=check_var, value=1, command=check).pack()
        tk.Radiobutton(game_area, text=results[1], variable=check_var, value=2, command=check).pack()
        tk.Radiobutton(game_area, text=results[2], variable=check_var, value=3, command=check).pack()
        tk.Radiobutton(game_area, text=results[3], variable=check_var, value=4, command=check).pack()


        game_area.pack()
    game.mainloop()




database = open_file()
log_in_window()

