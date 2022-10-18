import sqlite3
from tkinter import Tk

conn = sqlite3.connect("PIMS")
c = conn.cursor()

def staff_win(ID):
    SW = Tk()
    SW.title("Staff")

    # functions:
    """
    - view loaned items
    - update personal details
    """

    def logout_function():
        SW.destroy()
        from login_window import login_win
        login_win()

    def view_user_details():
        pass

    SW.mainloop()