import tkinter as tk


def prepare_for_entry_name(event,  entry):
    entry.delete(0, tk.END)
    entry.configure(bg='white')


def prepare_for_entry_password(event,  entry):
    entry.delete(0, tk.END)
    entry.configure(bg='white', show='*')