import tkinter as tk
import quiz_style as qs
# from register_window import RegisterWindow
import preparation as pr
import database_func as df


class LogInWindow:
    database = df.open_file()

    def __init__(self):
        self.database = database
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
        register_button = tk.Button(work_sector, text='Register now!', command=lambda: RegisterWindow)
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
        user_name = name.get()
        user_password = password.get()
        if user_name in self.database:
            if user_password == self.database[user_name]['password']:
                user_data = [user_name, self.database[user_name]]
                print('gudjob')
                # choose()
            else:
                password.configure(bg='red', show='')
                password.delete(0, "end")
                password.insert(0, 'Wrong Password')
                print('suck')
        else:
            name.configure(bg='red')
            name.delete(0, "end")
            name.insert(0, 'User not found')
            password.delete(0, "end")


class RegisterWindow(LogInWindow):

    def __init__(self):
        self.database = database
        self.window = tk.Toplevel()
        self.window.geometry('450x150+300+300')
        self.window.iconbitmap('icon.ico')

        register_message = tk.Label(self.window, text='Registering to our quiz!', font=('Equinox', 15, 'bold'),
                                    fg='#471de3')

        registration_sector = tk.Frame(self.window, highlightbackground="black", highlightthickness=1)
        name_label = tk.Label(registration_sector, text='Name: ')
        name_label.configure(font=qs.text_style)
        password_label = tk.Label(registration_sector, text='Password: ')
        password_label.configure(font=qs.text_style)
        password_label_confirm = tk.Label(registration_sector, text='Repeat Password: ')
        password_label_confirm.configure(font=qs.text_style)
        name_entry = tk.Entry(registration_sector)
        name_entry.configure(font=qs.entry_style)
        name_entry.bind("<Button-1>", lambda e, entry=name_entry: pr.prepare_for_entry_name(e, entry))
        password_entry = tk.Entry(registration_sector)
        password_entry.configure(font=qs.entry_style, show="*")
        password_entry.bind("<Button-1>", lambda e, entry=password_entry: pr.prepare_for_entry_password(e, entry))
        password_entry_confirm = tk.Entry(registration_sector)
        password_entry_confirm.configure(font=qs.entry_style, show="*")
        password_entry_confirm.bind("<Button-1>",
                                    lambda e, entry=password_entry_confirm: pr.prepare_for_entry_password(e, entry))
        registration_button = tk.Button(self.window, text='Confirm',
                                        command=lambda name=name_entry, password=password_entry,
                                        rpt_password=password_entry_confirm: self.registration(name, password, rpt_password),
                                        font=qs.button_style)

        name_label.grid(row=0, column=0, padx=5, pady=3)
        password_label.grid(row=1, column=0, padx=5, pady=3)
        password_label_confirm.grid(row=2, column=0, padx=5, pady=3)
        name_entry.grid(row=0, column=1, padx=5, pady=3)
        password_entry.grid(row=1, column=1, padx=5, pady=3)
        password_entry_confirm.grid(row=2, column=1, padx=5, pady=3)

        register_message.pack()
        registration_sector.pack()
        registration_button.pack()

        tk.mainloop()

    def registration(self, name, password, repeat_password):
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
                    # choose()
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

qwe = LogInWindow()
