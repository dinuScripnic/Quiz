import tkinter as tk
import database_func as db
from settings_window import SettingsWindow
from user import User
from register_window import RegisterWindow


class LogInWindow:

    def __init__(self):
        self.page = tk.Tk()
        self.page.title('QUIZ by DS')
        self.page.geometry('450x185+650+450')
        self.page.iconbitmap('icon.ico')

        welcome_text = tk.Label(self.page, text='Welcome to our quiz. Hope you\'ll have fun!',
                                font=('Equinox', 15, 'bold'), fg='#471de3')
        welcome_text.pack(pady=5)

        work_sector = tk.Frame(self.page, highlightbackground="black", highlightthickness=1)
        name_label = tk.Label(work_sector, text='Name: ', font=('Equinox', 10, 'bold'),  width=10)
        name_label.grid(row=0, column=0, padx=5, pady=5)
        password_label = tk.Label(work_sector, text='Password: ', font=('Equinox', 10, 'bold'), width=10)
        password_label.grid(row=1, column=0, padx=5, pady=5)
        name_entry = tk.Entry(work_sector, font=('Equinox', 10), width=25)
        name_entry.bind("<Button-1>", lambda e, entry=name_entry: self.prepare_entry(e, entry, ''))
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        password_entry = tk.Entry(work_sector, font=('Equinox', 10), show="*", width=25)
        password_entry.bind("<Button-1>", lambda e, entry=password_entry: self.prepare_entry(e, entry, '*'))
        password_entry.grid(row=1, column=1, padx=5, pady=5)
        register_button = tk.Button(work_sector, text='Register now!', command=self.register, font=('Equinox', 10), width=10)
        register_button.grid(row=2, column=0, padx=5, pady=5)
        work_sector.pack(pady=1)

        log_in_button = tk.Button(self.page, text='Log in', command=lambda name=name_entry, password=password_entry: self.logging_in(name, password), width=10, height=1, font=('Equinox', 10, 'bold'))
        log_in_button.pack(pady=5)

        tk.mainloop()

    def register(self):
        self.page.destroy()
        RegisterWindow()

    def prepare_entry(self, e, entry, show):
        entry.delete(0, tk.END)
        entry.configure(bg='white', show=show)

    def logging_in(self, name, password):
        user = db.get_user(name.get(), password.get())
        if isinstance(user, User):
            self.page.destroy()
            SettingsWindow(user)
        elif user == 'Wrong password':
            password.configure(bg='red', show='')
            password.delete(0, "end")
            password.insert(0, 'Wrong Password')
        elif user == 'User does not exist':
            name.configure(bg='red', show='')
            name.delete(0, "end")
            name.insert(0, 'User does not exist')
