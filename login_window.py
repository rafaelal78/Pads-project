from tkinter import Label, Entry, Button, Tk, N, E, W
from PIL import ImageTk, Image


def login_win():
    login = Tk()
    login.title("Login")
    login.geometry("500x600")

    try:
        PSB_logo = ImageTk.PhotoImage(Image.open("PIMS_image_folder/Primary-PSB-logo-resized.png"))
    except:
        PSB_logo = ImageTk.PhotoImage(Image.open("PIMS_files/PIMS_image_folder/Primary-PSB-logo-resized.png"))


    def goto_register_win(event):
        login.destroy()
        from registration_window import registration_win
        registration_win()

    def goto_retrieve_PW_win(event):
        login.destroy()
        from retrieve_password_window import retrieve_PW_win
        retrieve_PW_win()

    def login_command():
        Label(login, text="                            ").grid(row=2, column=1, sticky=N)
        Label(login, text="                            ").grid(row=4, column=1, sticky=N)

        if email_entry.get() == "":
            Label(login, text="Enter An Email", fg="red").grid(row=2, column=1, sticky=N)

        if password_entry.get() == "":
            Label(login, text="Enter A Password", fg="red").grid(row=4, column=1, sticky=N)

        #   Goes to another stage if both entries are filled
        if email_entry.get() != "" and password_entry.get() != "":

            import sqlite3

            conn = sqlite3.connect("PIMS")
            c = conn.cursor()

            get_emps_email = c.execute("SELECT email FROM employee WHERE email=:email",
                                       {'email': email_entry.get()}).fetchone()

            #   Sees if the email exists, if not, passes on a message beneath email entry "Invalid Password"
            #   else, goes on the next stage.
            try:
                if email_entry.get() == get_emps_email[0] and get_emps_email[0] != None:

                    get_emps_pas = c.execute("SELECT password FROM employee WHERE password=:password",
                                             {'password': password_entry.get()}).fetchone()

                    #   If the password entry is not the same as the password in the database,
                    #   passes on a message beneath the password entry "Invalid Password", else,
                    #   goes on the next stage
                    try:
                        if password_entry.get() == get_emps_pas[0] and get_emps_pas[0] != None:
                            get_emps_type = c.execute("SELECT employee_type FROM employee WHERE email=:email",
                                                      {'email': email_entry.get()}).fetchone()[0]
                            get_emps_ID = c.execute("SELECT employee_ID FROM employee WHERE email=:email",
                                                    {'email': email_entry.get()}).fetchone()[0]

                            #   Looks at column name employee_type to see of employee is staff, manager or admin,
                            #   if employee is of a certain type, opens the respective window and closes databases
                            #   as well as this window; login window.

                            #   Uses email to use user's ID to open respective window.
                            if get_emps_type == "staff":
                                login.destroy()
                                conn.close()
                                from staff_window import staff_win
                                staff_win(get_emps_ID)
                            elif get_emps_type == "manager":
                                login.destroy()
                                conn.close()
                                from manager_window import manager_win
                                manager_win(get_emps_ID)
                            else:
                                login.destroy()
                                conn.close()
                                from administrator_window import admin_win
                                admin_win(get_emps_ID)
                    except:
                        Label(login, text="Invalid Password", fg="red").grid(row=4, column=1, sticky=N)
            except:
                Label(login, text="Invalid Email", fg="red").grid(row=2, column=1, sticky=N)
        else:
            pass

    display_logo = Label(login, image=PSB_logo)

    #   Label
    email_text = Label(login, text="Email")
    blank0 = Label(login, text="")
    password_text = Label(login, text="Password")
    blank1 = Label(login, text="")
    blank2 = Label(login, text="")
    forgot_password_clickable_text = Label(login, text="Forgot Password? Click Here")
    blank3 = Label(login, text="")
    register_clickable_text = Label(login, text="Don't have an account? Click Here")

    #   Entries
    email_entry = Entry(login, width=55)
    password_entry = Entry(login, width=55, show="*")

    #   Button
    login_button = Button(login, text="Login", command=login_command)

    #   Binds
    forgot_password_clickable_text.bind("<Button>", goto_retrieve_PW_win)
    register_clickable_text.bind("<Button>", goto_register_win)

    #   Grids
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
