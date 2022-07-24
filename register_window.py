import sqlite3
import tkinter as tk


class RegisterWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('350x190+650+450')
        self.window.iconbitmap('icon.ico')

        register_message = tk.Label(self.window, text='Registering to our quiz!', font=('Equinox', 15, 'bold'),
                                    fg='#471de3')

        registration_sector = tk.Frame(self.window, highlightbackground="black", highlightthickness=1)
        name_label = tk.Label(registration_sector, text='Name: ', font=('Equinox', 10, 'bold'), width=10)
        password_label = tk.Label(registration_sector, text='Password: ', font=('Equinox', 10, 'bold'), width=10)
        password_label_confirm = tk.Label(registration_sector, text='Repeat Password: ', font=('Equinox', 10, 'bold'))
        name_entry = tk.Entry(registration_sector, width=25, font=('Equinox', 10))
        name_entry.bind("<Button-1>", lambda e, entry=name_entry: self.prepare_entry(e, entry, ''))
        password_entry = tk.Entry(registration_sector, width=25, font=('Equinox', 10), show='*')
        password_entry.bind("<Button-1>", lambda e, entry=password_entry: self.prepare_entry(e, entry, '*'))
        password_entry_confirm = tk.Entry(registration_sector, show='*', width=25, font=('Equinox', 10))
        password_entry_confirm.bind("<Button-1>",
                                    lambda e, entry=password_entry_confirm: self.prepare_entry(e, entry, '*'))

        name_label.grid(row=0, column=0, padx=5, pady=5)
        password_label.grid(row=1, column=0, padx=5, pady=5)
        password_label_confirm.grid(row=2, column=0, padx=5, pady=5)
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        password_entry.grid(row=1, column=1, padx=5, pady=5)
        password_entry_confirm.grid(row=2, column=1, padx=5, pady=5)

        registration_button = tk.Button(self.window, text='Confirm',
                                        command=lambda name=name_entry, password=password_entry,
                                        rpt_password=password_entry_confirm: self.registration(name, password, rpt_password), width=10, font=('Equinox', 10, 'bold'))

        go_back_button = tk.Button(self.window, text='Go back', command=self.go_back, width=10, font=('Equinox', 10))
        register_message.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        registration_sector.grid(row=1, column=0, padx=10, pady=5, columnspan=2)
        go_back_button.grid(row=2, column=0, padx=5, pady=5)
        registration_button.grid(row=2, column=1, padx=5, pady=5)

        tk.mainloop()

    def go_back(self):
        self.window.destroy()
        from log_in_window import LogInWindow
        LogInWindow()

    def prepare_entry(self, event, entry, show):
        entry.delete(0, tk.END)
        entry.configure(bg='white', show=show)

    def registration(self, name, password, repeat_password):
        user_name = name.get()
        user_password = password.get()
        user_repeat_password = repeat_password.get()
        if len(user_password) < 8:
            password.configure(bg='red')
            password.delete(0, "end")
            password.insert(0, 'Passwords to short')
            repeat_password.delete(0, "end")
        else:
            try:
                if user_password == user_repeat_password:
                    import database_func as db
                    from user import User
                    from settings_window import SettingsWindow
                    db.create_user(user_name, user_password)
                    user = User(user_name, user_password)
                    self.window.destroy()
                    SettingsWindow(user)
                else:
                    password.configure(bg='red')
                    password.delete(0, "end")
                    password.insert(0, 'Passwords do not match')
                    repeat_password.delete(0, "end")
            except sqlite3.IntegrityError:
                name.configure(bg='red')
                name.delete(0, "end")
                name.insert(0, 'User already exists')
