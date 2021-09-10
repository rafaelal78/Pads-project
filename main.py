from tkinter import *
from dum import *
from PIL import ImageTk, Image

def login_win():
    login = Tk()
    login.geometry("500x600")
    PSB_logo = ImageTk.PhotoImage(Image.open("PIMS_image_folder/Primary-PSB-logo-resized.png"))

    def goto_register_win(event):
        login.destroy()
        registration_win()

    def goto_retrieve_PW_win(event):
        login.destroy()
        retrieve_PW_win()

    def login_command():
        pass

    display_logo = Label(login, image=PSB_logo)

    email_text = Label(login, text="Email")
    email_entry = Entry(login, width=55)
    blank0 = Label(login, text="")
    password_text = Label(login, text="Password")
    password_entry = Entry(login, width=55)
    blank1 = Label(login, text="")

    login_button = Button(login, text="Login")

    blank2 = Label(login, text="")
    forgot_password_clickable_text = Label(login, text="Forgot Password? Click Here")
    blank3 = Label(login, text="")
    register_clickable_text = Label(login, text="Don't have an account? Click Here")

    forgot_password_clickable_text.bind("<Button>", goto_retrieve_PW_win)
    register_clickable_text.bind("<Button>", goto_register_win)

    display_logo.grid(row=0, column=0, padx=170, pady=50, columnspan=100)

    email_text.grid(row=1, column=0, sticky=E, padx=30)
    email_entry.grid(row=1, column=1)
    blank0.grid(row=2, column=0, pady=10)
    password_text.grid(row=3, column=0)
    password_entry.grid(row=3, column=1, sticky=E)
    blank1.grid(row=4, column=0, pady=15)

    login_button.grid(row=5, column=1)

    blank2.grid(row=6, column=1, pady=20)
    forgot_password_clickable_text.grid(row=7, column=0, columnspan=3, sticky=W)
    blank3.grid(row=8, column=1, pady=5)
    register_clickable_text.grid(row=9, column=0, columnspan=3, sticky=W)

    login.mainloop()

def registration_win():
    reg = Tk()
    reg.geometry("400x400")

    blank0 = Label(reg)
    full_name_text = Label(reg, text="Full Name")
    blank1 = Label(reg)
    email_text = Label(reg, text="Email")
    blank2 = Label(reg)
    PW_text = Label(reg, text="Password")
    blank3 = Label(reg)
    confirm_PW_text = Label(reg, text="Confirm Password")
    blank4 = Label(reg)
    cal_text = Label(reg, text="Date Of Birth")
    cal = Calendar(reg, selectmode='day', year=2020, month=5, day=22)

    confirm_button = Button(reg, text="Confirm")

    blank0.grid(row=0, column=0, padx=10)
    full_name_text.grid(row=1, column=0)
    blank1.grid(row=2, column=0, padx=10)
    email_text.grid(row=3, column=0)
    blank2.grid(row=4, column=0, padx=10)
    PW_text.grid(row=5, column=0)
    blank3.grid(row=6, column=0, padx=10)
    confirm_PW_text.grid(row=7, column=0)
    blank4.grid(row=8, column=0, padx=10)
    cal_text.grid(row=9, column=0)
    cal.grid(row=10, column=0)

    reg.mainloop()

def retrieve_PW_win():
    RPW = Tk()

    RPW.mainloop()

def admin_win():
    AP = Tk()

    AP.mainloop()

login_win()