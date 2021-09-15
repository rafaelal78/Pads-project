from tkinter import *
from dum import *
from PIL import ImageTk, Image

conn = sqlite3.connect("PIMS")
c = conn.cursor()

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employee VALUES"
                  "(:employee_ID, :full_name, :email, :password, :date_of_birth, :employee_type, :loan_total_cost)",
                  {'employee_ID': emp.ID , "full_name": emp.name, "email": emp.email,
                   "password": emp.password, "date_of_birth": emp.DoB,
                   "employee_type": emp.ET, "loan_total_cost": 0})

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
    RPW.geometry("360x210")
    RPW.title("Retrieve Password")

    def details_wind(email):
        email_entry.delete(0, "end")

        top = Toplevel()
        top.geometry("270x200")

        get_emps_ID = c.execute("SELECT employee_ID FROM employee WHERE email=:email",
                                {'email': email}).fetchone()

        get_emps_name = c.execute("SELECT full_name FROM employee WHERE email=:email",
                                  {'email': email}).fetchone()

        get_emps_email = c.execute("SELECT email FROM employee WHERE email=:email",
                                   {'email': email}).fetchone()

        get_emps_pas = c.execute("SELECT password FROM employee WHERE email=:email",
                                 {'email': email}).fetchone()

        emps_ID_text = "Employee ID: " + str(get_emps_ID[0])
        emps_name_text = "Employee full name: " + str(get_emps_name[0])
        emps_email_text = "Employee email: " + str(get_emps_email[0])
        emps_pas_text = "Employee password: " + str(get_emps_pas[0])

        def back_to_login_window():
            top.destroy()
            RPW.destroy()
            login_win()

        def close_details_wind():
            top.destroy()

        blank_0 = Label(top, pady=10)
        emp_id = Label(top, text=emps_ID_text)
        emp_name = Label(top, text=emps_name_text)
        emp_email = Label(top, text=emps_email_text)
        emp_pas = Label(top, text=emps_pas_text)
        blank_1 = Label(top, pady=10)

        login_win_button = Button(top, text="Login Window", command=back_to_login_window)
        close_win_button = Button(top, text="Close", command=close_details_wind)

        blank_0.grid(row=0, column=0, columnspan=2)
        emp_id.grid(row=1, column=0, columnspan=2, stick=W)
        emp_name.grid(row=2, column=0, columnspan=2, stick=W)
        emp_email.grid(row=3, column=0, columnspan=2, stick=W)
        emp_pas.grid(row=4, column=0, columnspan=2, stick=W)
        blank_1.grid(row=5, column=0, columnspan=2, stick=W)
        login_win_button.grid(row=6, column=0)
        close_win_button.grid(row=6, column=1, padx=70)

    def ver_email():
        Label(RPW, text="                                ").grid(row=2, column=1, sticky=N)
        if email_entry.get() != "":
            if c.execute("SELECT email FROM employee WHERE email=:email",
                                {'email': email_entry.get()}).fetchone()[0] is not None:
                details_wind(email_entry.get())
            else:
                Label(RPW, text="Invalid Email", fg="red").grid(row=2, column=1, sticky=N)
        else:
            Label(RPW, text="Invalid Email", fg="red").grid(row=2, column=1, sticky=N)


    blank0 = Label(RPW)
    email_text = Label(RPW, text="Email")

    email_entry = Entry(RPW, width=45)

    blank1 = Label(RPW)
    confirm_button = Button(RPW, text="Confirm", command=ver_email)

    blank0.grid(row=0, column=0, pady=30)
    email_text.grid(row=1, column=0, padx=10, sticky=W)
    email_entry.grid(row=1, column=1)
    blank1.grid(row=2, column=0, pady=20)
    confirm_button.grid(row=3, column=1)

    RPW.mainloop()
    
def admin_win():
    AP = Tk()

    AP.mainloop()

def manager_win():
    MW = Tk()

    MW.mainloop()

def staff_win():
    SW = Tk()

    SW.mainloop()

login_win()

conn.close()
