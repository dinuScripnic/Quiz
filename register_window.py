import sqlite3
import tkinter as tk
import quiz_style as qs
import preparation as pr
import database_func as db
from user import User
from settings_window import SettingsWindow


class RegisterWindow:
    def __init__(self):
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