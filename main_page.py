import threading
import tkinter as tk
from quiz_functionality import QuizBrain
import quiz_style as qs
import database_func as db


class MainPage:

    def __init__(self, user, questions):
        self.user = user
        self.functionality = QuizBrain(questions)
        self.window = tk.Tk()
        self.window.title("iQuiz App")
        self.window.geometry("850x530")
        self.window.iconbitmap('icon.ico')
        title = tk.Label(self.window, text="Quiz App", width=50, font=qs.text_style)
        title.pack()
        # display the first question
        self.display_question()
        # self.window.mainloop()

    def next(self, user_answer, correct_answer):
        self.frame.destroy()
        # self.functionality.check_answer(user_answer, correct_answer)
        if self.functionality.has_more_questions():
            threading.Thread(target=self.functionality.check_answer, args=(user_answer, correct_answer)).start()
            self.display_question()
        else:
            self.functionality.check_answer(user_answer, correct_answer)
            self.window.destroy()
            self.user.score = self.functionality.get_score()
            db.update_user(self.user)

    def display_question(self):
        """Create a frame, in frame a label with question and 4 radiobutons for response, when user press a button answer is checked"""
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        data = self.functionality.next_question()
        question = tk.Label(self.frame, text=data[0], font=qs.text_style)
        question.pack()
        r = tk.IntVar()
        r.set(0)
        for i in range(4):
            answer = tk.Radiobutton(self.frame, text=data[1][i], variable=r, value=i, font=qs.text_style)
            answer.pack()
        button = tk.Button(self.frame, text="Next", command=lambda r=r: self.next(user_answer=data[1][r.get()], correct_answer=data[2]))
        button.pack()
        self.window.mainloop()
