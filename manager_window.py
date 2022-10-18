import sqlite3
from tkinter import Tk

conn = sqlite3.connect("PIMS")
c = conn.cursor()

def manager_win(ID):
    MW = Tk()
    MW.title("Manager")

    # functions:
    """

    """

    def logout_function():
        MW.destroy()
        from login_window import login_win
        login_win()

    def view_user_details():
        pass

    MW.mainloop()