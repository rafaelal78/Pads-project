from tkinter import *
import time
from tkcalendar import Calendar
from PIL import ImageTk, Image
from tkinter import messagebox

def login_win():
    login = Tk()
    login.geometry("500x600")
    PSB_logo = ImageTk.PhotoImage(Image.open("Primary-PSB-logo-resized.png"))

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
    window_registration = Tk()
    window_title = "Registration"
    window_registration.title(window_title)
    window_size = "400x400"
    window_registration.geometry(window_size)

    label_first_name = "First Name"
    label_last_name = "Last Name"
    label_email = "Email"
    label_password = "Password"
    label_confirm_password = "Confirm Password"
    label_date_of_birth = "Date of Birth"

    lbl_first_name = Label(window_registration, text=label_first_name)
    lbl_first_name.grid(column=0, row=0)
    txt_first_name = Entry(window_registration, width=10)
    txt_first_name.grid(column=1, row=0)

    lbl_last_name = Label(window_registration, text=label_last_name)
    lbl_last_name.grid(column=0, row=1)
    txt_last_name = Entry(window_registration, width=10)
    txt_last_name.grid(column=1, row=1)

    lbl_email = Label(window_registration, text=label_email)
    lbl_email.grid(column=0, row=2)
    txt_email = Entry(window_registration, width=10)
    txt_email.grid(column=1, row=2)

    lbl_password = Label(window_registration, text=label_password)
    lbl_password.grid(column=0, row=3)
    txt_password = Entry(window_registration, width=10)
    txt_password.grid(column=1, row=3)

    lbl_confirm_password = Label(window_registration, text=label_confirm_password)
    lbl_confirm_password.grid(column=0, row=4)
    txt_confirm_password = Entry(window_registration, width=10)
    txt_confirm_password.grid(column=1, row=4)

    current_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    year = current_date[0:4]
    month = current_date[5:7]
    day = current_date[8:10]
    year_int = int(year)
    month_int = int(month)
    day_int = int(day)

    print(year_int,month_int,day_int)

    lbl_date_of_birth = Label(window_registration, text=label_date_of_birth)
    lbl_date_of_birth.grid(column=0, row=5)
    cal = Calendar(window_registration, selectmode='day',year=year_int, month=month_int,day=day_int)
    cal.grid(pady=5)

    def clicked():
        first_name = txt_first_name.get()
        last_name = txt_last_name.get()
        email = txt_email.get()
        password = txt_password.get()
        confirm_password = txt_confirm_password.get()
        date_of_birth = cal.get_date()
        Validation = 0

        if first_name == "":
            info_1 = "Please fill in the first name"
            messagebox.showinfo("Message title", info_1)
            Validation += 1

        if last_name == "":
            info_2 = "Please fill in the last name"
            messagebox.showinfo("Message title", info_2)
            Validation += 1

        if email == "":
            info_3 = "Please fill in the email"
            messagebox.showinfo("Message title", info_3)
            Validation += 1

        if password == "":
            info_4 = "Please fill in the password"
            messagebox.showinfo("Message title", info_4)
            Validation += 1

        if confirm_password == "":
            info_5 = "Please fill in the confirm password"
            messagebox.showinfo("Message title", info_5)
            Validation += 1

        if confirm_password != password:
            info_6 = "The confirm password is not match with the password"
            messagebox.showinfo("Message title", info_6)
            Validation += 1

        if date_of_birth == "":
            info_7 = "Please fill in the date ot birth"
            messagebox.showinfo("Message title", info_7)
            Validation += 1

        user_info_list = []
        user_info_list.append(first_name)
        user_info_list.append(last_name)
        user_info_list.append(email)
        user_info_list.append(password)
        user_info_list.append(confirm_password)
        user_info_list.append(date_of_birth)

        print(user_info_list)
        if Validation == 0:
            print(user_info_list)
            return user_info_list
        else:
            info_8 = "There are {} errors in the data".format(Validation)
            messagebox.showinfo("Message title", info_8)


    btn = Button(window_registration, text="Confirm", command=clicked)
    btn.grid(column=1, row=6)

    window_registration.mainloop()

def retrieve_PW_win():
    RPW = Tk()

    RPW.mainloop()

def admin_win():
    AP = Tk()

    AP.mainloop()

login_win()