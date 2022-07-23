import random
from tkinter import messagebox


class QuizBrain:

    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.correct_answers = 0
        self.questions = questions
        self.current_question = None

    def has_more_questions(self):
        """To check if the quiz has more questions"""

        return self.question_no < len(self.questions)

    def next_question(self):
        """Get the next question by incrementing the question number"""

        self.current_question = self.questions[self.question_no]
        self.question = self.current_question['question']
        self.correct_answer = self.current_question["correct_answer"]
        self.answers = self.current_question["incorrect_answers"]
        self.answers.append(self.correct_answer)
        random.shuffle(self.answers)
        self.question_no += 1
        return self.question, self.answers, self.correct_answer

    def check_answer(self, user_answer, correct_answer):
        """Check the user's answer against the correct answer and maintain the score"""

        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct!", "You are correct!")
            self.correct_answers += 1
            self.score += 5
        else:
            messagebox.showerror("Incorrect!", "You are incorrect!\nThe correct answer is: " + correct_answer)
            self.score -= 3

    def get_score(self):
        """Get the number of correct answers, wrong answers, and score percentage."""
        messagebox.showinfo("Quiz Results", f"You answered {self.correct_answers} questions out of {self.question_no} correctly. Your score is {int(self.correct_answers) / int(self.question_no) * 100}%.")
        return self.score