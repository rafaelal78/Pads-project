import time
from tkcalendar import Calendar
from tkinter import Tk, Label, messagebox, Entry, Button, W, N

def registration_win():
    window_registration = Tk()
    window_title = "Registration"
    window_registration.title(window_title)
    window_size = "500x570"
    window_registration.geometry(window_size)

    def return_to_login():
        window_registration.destroy()
        from login_window import login_win
        login_win()

    def register():
        Label(window_registration, text="                                  ").grid(row=2, column=1, sticky=N)
        Label(window_registration, text="                                  ").grid(row=4, column=1, sticky=N)
        Label(window_registration, text="                                  ").grid(row=6, column=1, sticky=N)
        Label(window_registration, text="                                  ").grid(row=8, column=1, sticky=N)

        full_name = full_name_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        date_of_birth = cal.get_date()

        #    Verifies if the entries are filled, if not, passes on a message
        if full_name == "":
            Label(window_registration, text="Fill In The Entry", fg="red").grid(row=2, column=1, sticky=N)
        if email == "":
            Label(window_registration, text="Fill In The Entry", fg="red").grid(row=4, column=1, sticky=N)
        if password == "":
            Label(window_registration, text="Fill In The Entry", fg="red").grid(row=6, column=1, sticky=N)
        if confirm_password == "":
            Label(window_registration, text="Fill In The Entry", fg="red").grid(row=8, column=1, sticky=N)

        #   If four of the entries are filled goes on the next stage
        if full_name and email != "" and password != "" and confirm_password != "":

            #   If the password_entry and confirm_password_entry match, goes on to the next stage,
            #   if not, passes on a message beneath both entries "Passwords Don't Match"
            if password == confirm_password:
                full_name_entry.config(state="disabled")
                email_entry.config(state="disabled")
                password_entry.config(state="disabled")
                confirm_password_entry.config(state="disabled")

                #   Calls in these methods from another file
                from Classes import employee
                import sqlite3
                import random

                '''
                
                    Open the database with the name PIMS
                
                '''

                conn = sqlite3.connect("PIMS")
                c = conn.cursor()

                def insert_emp(emp):
                    with conn:
                        c.execute("INSERT INTO employee VALUES"
                                  "(:employee_ID, :full_name, :email, :password, :date_of_birth, :employee_type, :loan_total_cost)",
                                  {'employee_ID': emp.ID, "full_name": emp.name, "email": emp.email,
                                   "password": emp.password, "date_of_birth": emp.DoB,
                                   "employee_type": emp.ET, "loan_total_cost": 0})

                rand_emp_int = random.randint(111111111, 555555555)  # 9 digits

                #   Passes on the message that the user has been successfully created and integrated in
                #   the database. After these, the database is closed, close in this window and opens
                #   login_win()
                insert_emp(employee(rand_emp_int, full_name, email, password, date_of_birth, "staff"))
                response = messagebox.showinfo("Registered", "You've successfully registered")
                if response:
                    window_registration.destroy()
                    conn.close()
                    from login_window import login_win
                    login_win()
            else:
                Label(window_registration, text="Passwords Don't Match", fg="red").grid(row=6, column=1, sticky=N)
                Label(window_registration, text="Passwords Don't Match", fg="red").grid(row=8, column=1, sticky=N)
        else:
            pass

    # Texts
    label_full_name = "Full Name:"
    label_email = "Email:"
    label_password = "Password:"
    label_confirm_password = "Confirm Password:"
    label_date_of_birth = "Date of Birth:"

    current_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    year = current_date[0:4]
    month = current_date[5:7]
    day = current_date[8:10]
    year_int = int(year)
    month_int = int(month)
    day_int = int(day)

    # Labels
    blank0 = Label(window_registration)
    lbl_full_name = Label(window_registration, text=label_full_name)
    blank1 = Label(window_registration)
    lbl_email = Label(window_registration, text=label_email)
    blank2 = Label(window_registration)
    lbl_password = Label(window_registration, text=label_password)
    blank3 = Label(window_registration)
    lbl_confirm_password = Label(window_registration, text=label_confirm_password)
    blank4 = Label(window_registration)
    lbl_date_of_birth = Label(window_registration, text=label_date_of_birth)
    blank5 = Label(window_registration)

    # Entries
    full_name_entry = Entry(window_registration, width=60)
    email_entry = Entry(window_registration, width=60)
    password_entry = Entry(window_registration, width=60, show="*")
    confirm_password_entry = Entry(window_registration, width=60, show="*")

    # Others
    cal = Calendar(window_registration, selectmode='day', year=year_int, month=month_int, day=day_int)
    back_button = Button(window_registration, text="Back", command=return_to_login)
    confirm_button = Button(window_registration, text="Confirm", command=register)

    # Grids
    blank0.grid(row=0, column=0)
    lbl_full_name.grid(row=1, column=0, sticky=W)
    blank1.grid(row=2, column=0, pady=10)
    lbl_email.grid(row=3, column=0, sticky=W)
    blank2.grid(row=4, column=0, pady=10)
    lbl_password.grid(row=5, column=0, sticky=W)
    blank3.grid(row=6, column=0, pady=10)
    lbl_confirm_password.grid(row=7, column=0, sticky=W)
    blank4.grid(row=8, column=0, pady=10)
    lbl_date_of_birth.grid(row=9, column=0, sticky=W)
    blank5.grid(row=11, column=0, pady=10)

    full_name_entry.grid(row=1, column=1, sticky=W)
    email_entry.grid(row=3, column=1, sticky=W)
    password_entry.grid(row=5, column=1, sticky=W)
    confirm_password_entry.grid(row=7, column=1, sticky=W)

    cal.grid(row=10, column=1, pady=5)
    back_button.grid(row=12, column=0)
    confirm_button.grid(row=12, column=1)

    window_registration.mainloop()