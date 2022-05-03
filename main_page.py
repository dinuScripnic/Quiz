import tkinter as tk
from quiz_functionality import QuizBrain
import quiz_style as qs
import log_in_window


class MainPage:

    def __init__(self, brain: QuizBrain):
        self.functionality = QuizBrain
        self.window = tk.Tk()
        self.window.title("iQuiz App")
        self.window.geometry("850x530")
        title = tk.Label(self.window, text="Quiz App", width=50, font=qs.text_style)
        title.place(x=0, y=2)


database = df.open_file()
