import tkinter as tk
import quiz_style as qs
import preparation as pr
import database_func as db
from settings_window import SettingsWindow
from user import User
from register_window import RegisterWindow


class LogInWindow:
    db.create_database()

    def __init__(self):
        self.page = tk.Tk()
        self.page.title('QUIZ by DS')
        self.page.geometry('450x150+200+200')
        self.page.iconbitmap('icon.ico')

        welcome_text = tk.Label(self.page, text='Welcome to our quiz. Hope you\'ll have fun!',
                                font=('Equinox', 15, 'bold'), fg='#471de3')

        work_sector = tk.Frame(self.page, highlightbackground="black", highlightthickness=1)
        name_label = tk.Label(work_sector, text='Name: ')
        name_label.configure(font=qs.text_style)
        password_label = tk.Label(work_sector, text='Password: ')
        password_label.configure(font=qs.text_style)
        name_entry = tk.Entry(work_sector)
        name_entry.configure(font=qs.entry_style)
        name_entry.bind("<Button-1>", lambda e, entry=name_entry: pr.prepare_for_entry_name(e, entry))
        password_entry = tk.Entry(work_sector)
        password_entry.configure(font=qs.entry_style, show="*")
        password_entry.bind("<Button-1>", lambda e, entry=password_entry: pr.prepare_for_entry_password(e, entry))
        register_button = tk.Button(work_sector, text='Register now!', command=lambda: RegisterWindow())
        register_button.configure(font=qs.button_style)

        log_in_button = tk.Button(self.page, text='Log in', font=qs.button_style,
                                  command=lambda name=name_entry, password=password_entry: self.logging_in(name, password))

        name_label.grid(row=0, column=0, padx=5, pady=3)
        password_label.grid(row=1, column=0, padx=5, pady=3)
        name_entry.grid(row=0, column=1, padx=5, pady=3)
        password_entry.grid(row=1, column=1, padx=5, pady=3)
        register_button.grid(row=2, column=0, padx=5, pady=3)

        welcome_text.pack()
        work_sector.pack()
        log_in_button.pack()

        tk.mainloop()

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

LogInWindow()

