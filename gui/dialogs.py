from tkinter import messagebox


def show_error(message):
    messagebox.showerror(
        "Error",
        message
    )


def show_info(message):
    messagebox.showinfo(
        "Information",
        message
    )


def ask_yes_no(message):
    return messagebox.askyesno(
        "Confirmation",
        message
    )