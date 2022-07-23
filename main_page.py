import threading
import tkinter as tk
from quiz_functionality import QuizBrain
import database_func as db
import unicodedata


class MainPage:

    def __init__(self, user, questions):
        self.user = user
        self.functionality = QuizBrain(questions)
        self.window = tk.Tk()
        self.window.title("iQuiz App")
        self.window.geometry("850x300+650+450")
        self.window.iconbitmap('icon.ico')
        title = tk.Label(self.window, text="Quiz", width=200, font=("Equinox", 30), wraplength=150)
        title.pack(pady=10)
        # display the first question
        self.display_question()

    def next(self, user_answer, correct_answer):
        if self.functionality.has_more_questions():
            threading.Thread(target=self.functionality.check_answer, args=(user_answer, correct_answer)).start()
            self.frame.destroy()
            self.display_question()
        else:
            self.window.destroy()
            self.functionality.check_answer(user_answer, correct_answer)
            self.user.score = self.functionality.get_score()
            db.update_user(self.user)

    def display_question(self):
        self.frame = tk.Frame(self.window)
        self.frame.pack(pady=5)
        data = self.functionality.next_question()
        question = tk.Label(self.frame, text=data[0], width=100, font=("Equinox", 15))
        question.pack()
        r = tk.IntVar()
        r.set(0)
        for i in range(4):
            answer = tk.Radiobutton(self.frame, text=data[1][i], variable=r, value=i, font=("Equinox", 12))
            answer.pack()
        button = tk.Button(self.frame, text="Next", command=lambda r=r: self.next(user_answer=data[1][r.get()], correct_answer=data[2]), font=("Equinox", 10), width=10)
        button.pack(pady=5)
        self.window.mainloop()
