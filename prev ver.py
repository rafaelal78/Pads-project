from tkinter import *
from tkinter import messagebox
import sqlite3
import time
import random
from datetime import date
from PIL import ImageTk, Image
from tkcalendar import Calendar
from Classes import *

conn = sqlite3.connect("PIMS")
c = conn.cursor()

rand_emp_int = random.randint(111111111, 555555555)  # 9 digits
rand_item_int = random.randint(555555555, 999999999)  # 9 digits


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employee VALUES"
                  "(:employee_ID, :full_name, :email, :password, :date_of_birth, :employee_type, :loan_total_cost)",
                  {'employee_ID': emp.ID, "full_name": emp.name, "email": emp.email,
                   "password": emp.password, "date_of_birth": emp.DoB,
                   "employee_type": emp.ET, "loan_total_cost": 0})


def insert_item(item):
    with conn:
        c.execute("INSERT INTO item VALUES"
                  "(:item_ID, :item_name, :item_cost, :number_of_items, :date_of_purchase, :threshold_value,"
                  ":description, :item_type)",
                  {'item_ID': item.ID, "item_name": item.name, "item_cost": item.cost,
                   "number_of_items": item.number, "date_of_purchase": item.DoP,
                   "threshold_value": item.TV, "description": item.DP, "item_type": item.IT})


def login_win():
    login = Tk()
    login.title("Login")
    login.geometry("500x600")
    PSB_logo = ImageTk.PhotoImage(Image.open("PIMS_image_folder/Primary-PSB-logo-resized.png"))

    def goto_register_win(event):
        login.destroy()
        registration_win()

    def goto_retrieve_PW_win(event):
        login.destroy()
        retrieve_PW_win()

    def login_command():
        Label(login, text="                            ").grid(row=2, column=1, sticky=N)
        Label(login, text="                            ").grid(row=4, column=1, sticky=N)

        if email_entry.get() == "":
            Label(login, text="Enter An Email", fg="red").grid(row=2, column=1, sticky=N)

        if password_entry.get() == "":
            Label(login, text="Enter A Password", fg="red").grid(row=4, column=1, sticky=N)

        if email_entry.get() != "" and password_entry.get() != "":

            get_emps_email = c.execute("SELECT email FROM employee WHERE email=:email",
                                       {'email': email_entry.get()}).fetchone()
            try:
                if email_entry.get() == get_emps_email[0] and get_emps_email[0] != None:

                    get_emps_pas = c.execute("SELECT password FROM employee WHERE password=:password",
                                             {'password': password_entry.get()}).fetchone()
                    try:
                        if password_entry.get() == get_emps_pas[0] and get_emps_pas[0] != None:
                            get_emps_type = c.execute("SELECT employee_type FROM employee WHERE email=:email",
                                                      {'email': email_entry.get()}).fetchone()[0]
                            get_emps_ID = c.execute("SELECT employee_ID FROM employee WHERE email=:email",
                                                    {'email': email_entry.get()}).fetchone()[0]
                            if get_emps_type == "staff":
                                login.destroy()
                                staff_win(get_emps_ID)
                            elif get_emps_type == "manager":
                                login.destroy()
                                manager_win(get_emps_ID)
                            else:
                                login.destroy()
                                admin_win(get_emps_ID)
                    except:
                        Label(login, text="Invalid Password", fg="red").grid(row=4, column=1, sticky=N)
            except:
                Label(login, text="Invalid Email", fg="red").grid(row=2, column=1, sticky=N)
        else:
            pass

    display_logo = Label(login, image=PSB_logo)

    email_text = Label(login, text="Email")
    email_entry = Entry(login, width=55)
    blank0 = Label(login, text="")
    password_text = Label(login, text="Password")
    password_entry = Entry(login, width=55, show="*")
    blank1 = Label(login, text="")

    login_button = Button(login, text="Login", command=login_command)

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
    window_size = "500x570"
    window_registration.geometry(window_size)

    def return_to_login():
        window_registration.destroy()
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

        if full_name == "":
            Label(window_registration, text="Fill In The Entry", fg="red").grid(row=2, column=1, sticky=N)
        if email == "":
            Label(window_registration, text="Fill In The Entry", fg="red").grid(row=4, column=1, sticky=N)
        if password == "":
            Label(window_registration, text="Fill In The Entry", fg="red").grid(row=6, column=1, sticky=N)
        if confirm_password == "":
            Label(window_registration, text="Fill In The Entry", fg="red").grid(row=8, column=1, sticky=N)

        if full_name and email != "" and password != "" and confirm_password != "":
            if password == confirm_password:
                full_name_entry.config(state="disabled")
                email_entry.config(state="disabled")
                password_entry.config(state="disabled")
                confirm_password_entry.config(state="disabled")

                insert_emp(employee(rand_emp_int, full_name, email, password, date_of_birth, "staff"))
                response = messagebox.showinfo("Registered", "You've successfully registered")
                if response:
                    window_registration.destroy()
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


def retrieve_PW_win():
    RPW = Tk()
    RPW.geometry("360x210")
    RPW.title("Retrieve Password")

    def back_to_login():
        RPW.destroy()
        login_win()

    def details_wind(email):
        email_entry.delete(0, "end")
        get_emps_email = c.execute("SELECT email FROM employee WHERE email=:email",
                                   {'email': email}).fetchone()

        get_emps_pas = c.execute("SELECT password FROM employee WHERE email=:email",
                                 {'email': email}).fetchone()

        emps_email_text = "Email: " + str(get_emps_email[0])
        emps_pas_text = "Password: " + str(get_emps_pas[0])

        info = emps_email_text + "\n" + emps_pas_text + "\nWould You Like To Go Back To Login Window?"

        response = messagebox.askyesno("Password Retrieval", info)

        if response == 1:
            RPW.destroy()
            login_win()
        else:
            pass

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
    back_button = Button(RPW, text="Back", command=back_to_login)
    confirm_button = Button(RPW, text="Confirm", command=ver_email)

    blank0.grid(row=0, column=0, pady=30)
    email_text.grid(row=1, column=0, padx=10, sticky=W)
    email_entry.grid(row=1, column=1)
    blank1.grid(row=2, column=0, pady=20)
    back_button.grid(row=3, column=0, sticky=W)
    confirm_button.grid(row=3, column=1)

    RPW.mainloop()


def personal_details(ID):
    emp_ID = c.execute("SELECT employee_ID FROM employee WHERE employee_ID=:employee_ID",
                       {'employee_ID': ID}).fetchone()
    emp_FN = c.execute("SELECT full_name FROM employee WHERE employee_ID=:employee_ID", {'employee_ID': ID}).fetchone()
    emp_email = c.execute("SELECT email FROM employee WHERE employee_ID=:employee_ID", {'employee_ID': ID}).fetchone()
    emp_PW = c.execute("SELECT password FROM employee WHERE employee_ID=:employee_ID", {'employee_ID': ID}).fetchone()
    emp_DoB = c.execute("SELECT date_of_birth FROM employee WHERE employee_ID=:employee_ID",
                        {'employee_ID': ID}).fetchone()

    PD = Tk()
    PD.title("Employee Details")
    PD.geometry("400x400")

    def change_FN():
        CFN = Toplevel()
        CFN.geometry("400x150")
        CFN.title("Update Employee detail")

        def confirm_change():
            Label(CFN, text="                                ").grid(row=2, column=1, sticky=N)
            if FN_ent.get() != "":
                response = messagebox.askyesno("Confirm Change?", "Are you sure to make the change?")
                if response == 1:
                    with conn:
                        c.execute("""UPDATE employee SET full_name=:full_name
                                    WHERE email=:email""", {'email': emp_email[0], 'full_name': FN_ent.get()})
                    messagebox.showinfo("Success!", "Full Name successfully changed!")
                    CFN.destroy()
                    PD.destroy()
                    admin_win(emp_ID[0])
                else:
                    pass
            else:
                Label(CFN, text="Fill In The Entry", fg="red").grid(row=2, column=1, sticky=N)

        blank_0 = Label(CFN)
        FN_lbl = Label(CFN, text="First Name:")
        FN_ent = Entry(CFN, width=50)
        blank_1 = Label(CFN)

        close_window = Button(CFN, text="Close", command=CFN.destroy)
        confirm_button = Button(CFN, text="Confirm", command=confirm_change)

        blank_0.grid(row=0, column=1, pady=15)
        FN_lbl.grid(row=1, column=0)
        FN_ent.grid(row=1, column=1)
        blank_1.grid(row=2, column=0, pady=10)

        close_window.grid(row=3, column=0)
        confirm_button.grid(row=3, column=1)

    def change_email():
        CE = Toplevel()
        CE.geometry("400x150")
        CE.title("Update Employee detail")

        def confirm_change():
            Label(CE, text="                                ").grid(row=2, column=1, sticky=N)
            if email_ent.get() != "":
                response = messagebox.askyesno("Confirm Change?", "Are you sure to make the change?")
                if response == 1:
                    with conn:
                        c.execute("""UPDATE employee SET email=:email
                                    WHERE employee_ID=:employee_ID""",
                                  {'employee_ID': emp_ID[0],
                                   'email': email_ent.get()})
                    messagebox.showinfo("Success!", "Email successfully changed!")
                    CE.destroy()
                    PD.destroy()
                    admin_win(emp_ID[0])
                else:
                    pass
            else:
                Label(CE, text="Fill In The Entry", fg="red").grid(row=2, column=1, sticky=N)

        blank_0 = Label(CE)
        email_lbl = Label(CE, text="Email:")
        email_ent = Entry(CE, width=50)
        blank_1 = Label(CE)

        close_window = Button(CE, text="Close", command=CE.destroy)
        confirm_button = Button(CE, text="Confirm", command=confirm_change)

        blank_0.grid(row=0, column=1, pady=15)
        email_lbl.grid(row=1, column=0)
        email_ent.grid(row=1, column=1)
        blank_1.grid(row=2, column=0, pady=10)

        close_window.grid(row=3, column=0)
        confirm_button.grid(row=3, column=1)

    def change_PW():
        CPW = Toplevel()
        CPW.geometry("400x150")
        CPW.title("Verify Password")

        def ver_PW():
            Label(CPW, text="                                ").grid(row=2, column=1, sticky=N)
            emp_PW = c.execute("SELECT password FROM employee WHERE employee_ID=:employee_ID",
                               {'employee_ID': ID}).fetchone()
            if PW_ent.get() != "":
                if PW_ent.get() == emp_PW[0]:
                    CPW.destroy()
                    password_change()
                else:
                    Label(CPW, text="Invalid Password", fg="red").grid(row=2, column=1, sticky=N)
            else:
                Label(CPW, text="Fill In The Entry", fg="red").grid(row=2, column=1, sticky=N)

        def password_change():
            CC = Toplevel()
            CC.geometry("420x145")
            CC.title("Verify Password")

            def confirm_change():
                Label(CC, text="                                ").grid(row=2, column=1, sticky=N)
                Label(CC, text="                                ").grid(row=4, column=1, sticky=N)

                if password_ent.get() == "":
                    Label(CC, text="Fill in the entry", fg="red").grid(row=2, column=1, sticky=N)
                if confirm_password_ent.get() == "":
                    Label(CC, text="Fill in the entry", fg="red").grid(row=4, column=1, sticky=N)

                if password_ent.get() != "" and confirm_password_ent.get() != "":
                    if password_ent.get() == confirm_password_ent.get():
                        response = messagebox.askyesno("Confirm Change?", "Are you sure to make the change?")
                        if response == 1:
                            with conn:
                                c.execute("""UPDATE employee SET password=:password
                                            WHERE employee_ID=:employee_ID""",
                                          {'employee_ID': emp_ID[0],
                                           'password': password_ent.get()})
                            messagebox.showinfo("Success!", "Password successfully changed!")
                            CC.destroy()
                            PD.destroy()
                            admin_win(emp_ID[0])
                    else:
                        Label(CC, text="Passwords don't match!", fg="red").grid(row=4, column=1, sticky=N)
                else:
                    pass

            blank_one = Label(CC)
            password_lbl = Label(CC, text="Password:")
            blank_two = Label(CC)
            confirm_password_lbl = Label(CC, text="Confirm Password:")
            blank_three = Label(CC)

            password_ent = Entry(CC, width=50, show="*")
            confirm_password_ent = Entry(CC, width=50, show="*")

            con_button = Button(CC, text="Confirm", command=confirm_change)
            close_button = Button(CC, text="Close", command=CC.destroy)

            blank_one.grid(row=0, column=0)
            password_lbl.grid(row=1, column=0, sticky=W)
            blank_two.grid(row=2, column=0)
            confirm_password_lbl.grid(row=3, column=0, sticky=W)
            blank_three.grid(row=4, column=0)

            password_ent.grid(row=1, column=1)
            confirm_password_ent.grid(row=3, column=1)

            close_button.grid(row=5, column=0)
            con_button.grid(row=5, column=1)

        blank_0 = Label(CPW)
        PW_lbl = Label(CPW, text="Password:")
        PW_ent = Entry(CPW, width=50, show="*")
        blank_1 = Label(CPW)

        close_window = Button(CPW, text="Close", command=CPW.destroy)
        confirm_button = Button(CPW, text="Confirm", command=ver_PW)

        blank_0.grid(row=0, column=1, pady=15)
        PW_lbl.grid(row=1, column=0)
        PW_ent.grid(row=1, column=1)
        blank_1.grid(row=2, column=0, pady=10)

        close_window.grid(row=3, column=0)
        confirm_button.grid(row=3, column=1)

    def change_DoB():
        CDoB = Toplevel()
        CDoB.geometry("330x260")
        CDoB.title("Update Employee detail")

        def change_DoB():
            response = messagebox.askyesno("Confirm Change?", "Are you sure to make the change?")
            if response == 1:
                with conn:
                    c.execute("""UPDATE employee SET date_of_birth=:date_of_birth
                                    WHERE employee_ID=:employee_ID""",
                              {'employee_ID': emp_ID[0],
                               'password': cal.get_date()})
                messagebox.showinfo("Success!", "Date of birth successfully changed!")
                CDoB.destroy()
                PD.destroy()
                admin_win(emp_ID[0])
            else:
                pass

        blank_0 = Label(CDoB)
        blank_1 = Label(CDoB)

        cal = Calendar(CDoB, selectmode='day')

        prev_win = Button(CDoB, text="Close", command=CDoB.destroy)
        confirm_button = Button(CDoB, text="Confirm", command=change_DoB)

        blank_0.grid(row=0, column=0)
        cal.grid(row=1, column=1)
        blank_1.grid(row=2, column=0)
        prev_win.grid(row=3, column=0)
        confirm_button.grid(row=3, column=1)

    def back():
        PD.destroy()
        admin_win(emp_ID[0])

    emp_ID_txt = "Employee's ID: " + str(emp_ID[0])
    emp_FN_txt = "Employee's First Name: " + str(emp_FN[0])
    emp_email_txt = "Employee's Email: " + str(emp_email[0])
    emp_PW_txt = "Employee's Password: " + str(len(emp_PW[0]) * "*")
    emp_DoB_txt = "Employee's Date of Birth: " + str(emp_DoB[0])

    blank0 = Label(PD)
    update_inst_lbl = Label(PD, text="Press on ○ to update")
    employee_ID = Label(PD, text=emp_ID_txt)
    blank1 = Label(PD)
    full_name = Label(PD, text=emp_FN_txt)
    blank2 = Label(PD)
    email = Label(PD, text=emp_email_txt)
    blank3 = Label(PD)
    password = Label(PD, text=emp_PW_txt)
    blank4 = Label(PD)
    date_of_birth = Label(PD, text=emp_DoB_txt)
    blank5 = Label(PD)

    upd_emp_FN = Button(PD, text="○", command=change_FN)
    upd_emp_email = Button(PD, text="○", command=change_email)
    upd_emp_PW = Button(PD, text="○", command=change_PW)
    upd_emp_DoB = Button(PD, text="○", command=change_DoB)

    back_button = Button(PD, text="Back", command=back)

    blank0.grid(row=0, column=0)
    update_inst_lbl.grid(row=0, column=1, padx=40)
    employee_ID.grid(row=1, column=0, sticky=W)
    blank1.grid(row=2, column=0)
    full_name.grid(row=3, column=0, sticky=W)
    blank2.grid(row=4, column=0)
    email.grid(row=5, column=0, sticky=W)
    blank3.grid(row=6, column=0)
    password.grid(row=7, column=0, sticky=W)
    blank4.grid(row=8, column=0)
    date_of_birth.grid(row=9, column=0, sticky=W)
    blank5.grid(row=10, column=0)

    upd_emp_FN.grid(row=3, column=1)
    upd_emp_email.grid(row=5, column=1)
    upd_emp_PW.grid(row=7, column=1)
    upd_emp_DoB.grid(row=9, column=1)

    back_button.grid(row=11, column=0, sticky=W, padx=20)

    PD.mainloop()


def view_staff(ID):
    emp_ID = c.execute("SELECT employee_ID FROM employee WHERE employee_ID=:employee_ID",
                       {'employee_ID': ID}).fetchone()[0]
    emps = c.execute("SELECT * FROM employee WHERE employee_ID=:employee_ID",
                     {'employee_ID': ID}).fetchone()

    staff_list = []
    staff = c.execute("SELECT * FROM employee").fetchall()
    staff.remove(emps)

    for emp in staff:
        staff_list.append(emp)

    VS = Tk()
    VS.title("Employees")
    VS.geometry("425x385")

    emp_ID_txt = "Employee ID\t\t - \t" + str(staff_list[0][0])
    emp_FN_txt = "Employee Fullname\t - \t" + str(staff_list[0][1])
    emp_email_txt = "Employee Email\t\t - \t" + str(staff_list[0][2])
    emp_DoB_txt = "Employee Date of birth\t - \t" + str(staff_list[0][4])
    emp_type_txt = "Employee Type\t\t - \t" + str(staff_list[0][5])
    emp_LTC_txt = "Employee Loan total cost\t - \t" + str(staff_list[0][6])

    emp_type_list = ["admin", "manager", "staff"]

    def back():
        VS.destroy()
        admin_win(emp_ID)

    def previous(index):
        emp_ID_txt = "Employee ID\t\t - \t" + str(staff_list[index][0])
        emp_FN_txt = "Employee Fullname\t - \t" + str(staff_list[index][1])
        emp_email_txt = "Employee Email\t\t - \t" + str(staff_list[index][2])
        emp_DoB_txt = "Employee Date of birth\t - \t" + str(staff_list[index][4])
        emp_type_txt = "Employee Type\t\t - \t" + str(staff_list[index][5])
        emp_LTC_txt = "Employee Loan total cost\t - \t" + str(staff_list[index][6])

        def change_employee_type():
            CET = Toplevel()
            CET.geometry("300x200")

            CET_var = StringVar(CET)
            CET_var.set(str(staff_list[index][5]))
            CET_emp_type_OM = OptionMenu(CET, CET_var, *emp_type_list)

            def confirm_change():
                if CET_var.get() != str(staff_list[index][5]):
                    response = messagebox.askyesno("Change status?", "Are you sure to change this employee's status?")
                    if response == 1:
                        with conn:
                            c.execute("""UPDATE employee SET employee_type=:employee_type
                                        WHERE employee_ID=:employee_ID""",
                                      {"employee_ID": int(staff_list[index][0]), "employee_type": CET_var.get()})
                        messagebox.showinfo("Success!", "Status succesfully changed!")
                        CET.destroy()
                        VS.destroy()
                        view_staff(emp_ID)
                    else:
                        CET.destroy()
                        VS.destroy()
                        view_staff(emp_ID)
                else:
                    pass

            gap_0 = Label(CET)
            emp_ID_lbl = Label(CET, text="Employee ID\t\t - \t")
            ID_lbl = Label(CET, text=str(staff_list[index][0]))
            gap_1 = Label(CET)
            emp_FN_lbl = Label(CET, text="Employee Fullname\t - \t")
            FN_lbl = Label(CET, text=str(staff_list[index][1]))
            gap_2 = Label(CET)
            emp_type_lbl = Label(CET, text="Employee Type\t\t - \t")
            gap_3 = Label(CET)

            close_btn = Button(CET, text="Close", command=CET.destroy)
            confirm_btn = Button(CET, text="Confirm", command=confirm_change)

            gap_0.grid(row=0, column=0)
            emp_ID_lbl.grid(row=1, column=0, sticky=W)
            ID_lbl.grid(row=1, column=1, sticky=W)
            gap_1.grid(row=2, column=0)
            emp_FN_lbl.grid(row=3, column=0, sticky=W)
            FN_lbl.grid(row=3, column=1, sticky=W)
            gap_2.grid(row=4, column=0)
            emp_type_lbl.grid(row=5, column=0)
            CET_emp_type_OM.grid(row=5, column=1)
            gap_3.grid(row=6, column=0)

            close_btn.grid(row=7, column=0, sticky=W, padx=20)
            confirm_btn.grid(row=7, column=1)

        emp_ID_lbl.config(text=emp_ID_txt)
        emp_FN_lbl.config(text=emp_FN_txt)
        emp_email_lbl.config(text=emp_email_txt)
        emp_DoB_lbl.config(text=emp_DoB_txt)
        emp_type_lbl.config(text=emp_type_txt)
        emp_LTC_lbl.config(text=emp_LTC_txt)

        prev_btn = Button(VS, text="<<", command=lambda: previous(index - 1))
        next_btn = Button(VS, text=">>", command=lambda: next(index + 1))
        change_emp_type_btn = Button(VS, text="Change", command=change_employee_type)

        if index == 0:
            prev_btn = Button(VS, text="<<", state=DISABLED)

        prev_btn.grid(row=13, column=0, padx=10, sticky=W)
        next_btn.grid(row=13, column=1)
        change_emp_type_btn.grid(row=9, column=1)

    def next(index):
        emp_ID_txt = "Employee ID\t\t - \t" + str(staff_list[index][0])
        emp_FN_txt = "Employee Fullname\t - \t" + str(staff_list[index][1])
        emp_email_txt = "Employee Email\t\t - \t" + str(staff_list[index][2])
        emp_DoB_txt = "Employee Date of birth\t - \t" + str(staff_list[index][4])
        emp_type_txt = "Employee Type\t\t - \t" + str(staff_list[index][5])
        emp_LTC_txt = "Employee Loan total cost\t - \t" + str(staff_list[index][6])

        def change_employee_type():
            CET = Toplevel()
            CET.geometry("300x200")

            CET_var = StringVar(CET)
            CET_var.set(str(staff_list[index][5]))
            CET_emp_type_OM = OptionMenu(CET, CET_var, *emp_type_list)

            def confirm_change():
                if CET_var.get() != str(staff_list[index][5]):
                    response = messagebox.askyesno("Change status?", "Are you sure to change this employee's status?")
                    if response == 1:
                        with conn:
                            c.execute("""UPDATE employee SET employee_type=:employee_type
                                        WHERE employee_ID=:employee_ID""",
                                      {"employee_ID": int(staff_list[index][0]), "employee_type": CET_var.get()})
                        messagebox.showinfo("Success!", "Status succesfully changed!")
                        CET.destroy()
                        VS.destroy()
                        view_staff(emp_ID)
                    else:
                        CET.destroy()
                        VS.destroy()
                        view_staff(emp_ID)
                else:
                    pass

            gap_0 = Label(CET)
            emp_ID_lbl = Label(CET, text="Employee ID\t\t - \t")
            ID_lbl = Label(CET, text=str(staff_list[index][0]))
            gap_1 = Label(CET)
            emp_FN_lbl = Label(CET, text="Employee Fullname\t - \t")
            FN_lbl = Label(CET, text=str(staff_list[index][1]))
            gap_2 = Label(CET)
            emp_type_lbl = Label(CET, text="Employee Type\t\t - \t")
            gap_3 = Label(CET)

            close_btn = Button(CET, text="Close", command=CET.destroy)
            confirm_btn = Button(CET, text="Confirm", command=confirm_change)

            gap_0.grid(row=0, column=0)
            emp_ID_lbl.grid(row=1, column=0, sticky=W)
            ID_lbl.grid(row=1, column=1, sticky=W)
            gap_1.grid(row=2, column=0)
            emp_FN_lbl.grid(row=3, column=0, sticky=W)
            FN_lbl.grid(row=3, column=1, sticky=W)
            gap_2.grid(row=4, column=0)
            emp_type_lbl.grid(row=5, column=0)
            CET_emp_type_OM.grid(row=5, column=1)
            gap_3.grid(row=6, column=0)

            close_btn.grid(row=7, column=0, sticky=W, padx=20)
            confirm_btn.grid(row=7, column=1)

        emp_ID_lbl.config(text=emp_ID_txt)
        emp_FN_lbl.config(text=emp_FN_txt)
        emp_email_lbl.config(text=emp_email_txt)
        emp_DoB_lbl.config(text=emp_DoB_txt)
        emp_type_lbl.config(text=emp_type_txt)
        emp_LTC_lbl.config(text=emp_LTC_txt)

        prev_btn = Button(VS, text="<<", command=lambda: previous(index - 1))
        next_btn = Button(VS, text=">>", command=lambda: next(index + 1))
        change_emp_type_btn = Button(VS, text="Change", command=change_employee_type)

        if index == len(staff_list) - 1:
            next_btn = Button(VS, text=">>", state=DISABLED)

        prev_btn.grid(row=13, column=0, padx=10, sticky=W)
        next_btn.grid(row=13, column=1)
        change_emp_type_btn.grid(row=9, column=1)

    def add_employee():
        AE = Toplevel()
        AE.title("Add Employee")
        AE.geometry("380x520")

        AE_var = StringVar(AE)
        AE_var.set("staff")
        AE_emp_type_OM = OptionMenu(AE, AE_var, *emp_type_list)

        def get_emp_info():
            Label(AE, text="                                  ").grid(row=2, column=1)
            Label(AE, text="                                  ").grid(row=4, column=1)
            Label(AE, text="                                  ").grid(row=6, column=1)
            Label(AE, text="                                  ").grid(row=8, column=1)

            rand_emp_int = random.randint(111111111, 555555555)

            if FN_ent.get() == "":
                Label(AE, text="Invalid Input", fg="red").grid(row=2, column=1)
            if email_ent.get() == "":
                Label(AE, text="Invalid Input", fg="red").grid(row=4, column=1)
            if PW_ent.get() == "":
                Label(AE, text="Invalid Input", fg="red").grid(row=6, column=1)
            if confirm_PW_ent.get() == "":
                Label(AE, text="Invalid Input", fg="red").grid(row=8, column=1)

            if FN_ent.get() != "" and email_ent.get() != "" and PW_ent.get() != "" \
                    and confirm_PW_ent.get() != "":
                response = messagebox.askyesno("Add Item?", "Are you sure to add this item?")
                if response == 1:
                    add_emp_class = employee(rand_emp_int, FN_ent.get(), email_ent.get(), PW_ent.get(),
                                             cal.get_date(), 0)
                    insert_emp(add_emp_class)
                    messagebox.showinfo("Success!", "The account has been successfully created!")
                    AE.destroy()
                    VS.destroy()
                    view_staff(emp_ID)
                else:
                    AE.destroy()
                    VS.destroy()
                    view_staff(emp_ID)
            else:
                pass

        gap_0 = Label(AE)
        FN_lbl = Label(AE, text="First name: ")
        gap_1 = Label(AE)
        email_lbl = Label(AE, text="Email: ")
        gap_2 = Label(AE)
        PW_lbl = Label(AE, text="Password: ")
        gap_3 = Label(AE)
        confirm_PW_lbl = Label(AE, text="Password confirm: ")
        gap_4 = Label(AE)
        employee_type_lbl = Label(AE, text="Employee type: ")
        gap_5 = Label(AE)
        DoB_lbl = Label(AE, text="Date of Birth: ")
        gap_6 = Label(AE)
        gap_7 = Label(AE)

        FN_ent = Entry(AE, width=40)
        email_ent = Entry(AE, width=40)
        PW_ent = Entry(AE, width=40)
        confirm_PW_ent = Entry(AE, width=40)
        # employee_type_ent = Entry(AE, width=40)

        cal = Calendar(AE, selectmode='day')
        close_btn = Button(AE, text="Close", command=AE.destroy)
        add_employee_btn = Button(AE, text="Confirm", command=get_emp_info)

        gap_0.grid(row=0, column=0)
        FN_lbl.grid(row=1, column=0, sticky=W)
        gap_1.grid(row=2, column=0)
        email_lbl.grid(row=3, column=0, sticky=W)
        gap_2.grid(row=4, column=0)
        PW_lbl.grid(row=5, column=0, sticky=W)
        gap_3.grid(row=6, column=0)
        confirm_PW_lbl.grid(row=7, column=0, sticky=W)
        gap_4.grid(row=8, column=0)
        employee_type_lbl.grid(row=9, column=0, sticky=W)
        gap_5.grid(row=10, column=0)
        DoB_lbl.grid(row=11, column=0, sticky=W)
        gap_6.grid(row=12, column=0)
        gap_7.grid(row=14, column=0)

        FN_ent.grid(row=1, column=1)
        email_ent.grid(row=3, column=1)
        PW_ent.grid(row=5, column=1)
        confirm_PW_ent.grid(row=7, column=1)
        AE_emp_type_OM.grid(row=9, column=1, sticky=W)

        cal.grid(row=13, column=1)
        close_btn.grid(row=15, column=0)
        add_employee_btn.grid(row=15, column=1)

    def change_employee_type():
        CET = Toplevel()
        CET.geometry("300x200")

        CET_var = StringVar(CET)
        CET_var.set(str(staff_list[0][5]))
        CET_emp_type_OM = OptionMenu(CET, CET_var, *emp_type_list)

        def confirm_change():
            if CET_var.get() != str(staff_list[0][5]):
                response = messagebox.askyesno("Change status?", "Are you sure to change this employee's status?")
                if response == 1:
                    with conn:
                        c.execute("""UPDATE employee SET employee_type=:employee_type
                                    WHERE employee_ID=:employee_ID""",
                                  {"employee_ID": int(staff_list[0][0]), "employee_type": CET_var.get()})
                    messagebox.showinfo("Success!", "Status succesfully changed!")
                    CET.destroy()
                    VS.destroy()
                    view_staff(emp_ID)
                else:
                    CET.destroy()
                    VS.destroy()
                    view_staff(emp_ID)
            else:
                pass

        gap_0 = Label(CET)
        emp_ID_lbl = Label(CET, text="Employee ID\t\t - \t")
        ID_lbl = Label(CET, text=str(staff_list[0][0]))
        gap_1 = Label(CET)
        emp_FN_lbl = Label(CET, text="Employee Fullname\t - \t")
        FN_lbl = Label(CET, text=str(staff_list[0][1]))
        gap_2 = Label(CET)
        emp_type_lbl = Label(CET, text="Employee Type\t\t - \t")
        gap_3 = Label(CET)

        close_btn = Button(CET, text="Close", command=CET.destroy)
        confirm_btn = Button(CET, text="Confirm", command=confirm_change)

        gap_0.grid(row=0, column=0)
        emp_ID_lbl.grid(row=1, column=0, sticky=W)
        ID_lbl.grid(row=1, column=1, sticky=W)
        gap_1.grid(row=2, column=0)
        emp_FN_lbl.grid(row=3, column=0, sticky=W)
        FN_lbl.grid(row=3, column=1, sticky=W)
        gap_2.grid(row=4, column=0)
        emp_type_lbl.grid(row=5, column=0)
        CET_emp_type_OM.grid(row=5, column=1)
        gap_3.grid(row=6, column=0)

        close_btn.grid(row=7, column=0, sticky=W, padx=20)
        confirm_btn.grid(row=7, column=1)

    gap0 = Label(VS)
    emp_ID_lbl = Label(VS, text=emp_ID_txt)
    gap1 = Label(VS)
    emp_FN_lbl = Label(VS, text=emp_FN_txt)
    gap2 = Label(VS)
    emp_email_lbl = Label(VS, text=emp_email_txt)
    gap3 = Label(VS)
    emp_DoB_lbl = Label(VS, text=emp_DoB_txt)
    gap4 = Label(VS)
    emp_type_lbl = Label(VS, text=emp_type_txt)
    gap5 = Label(VS)
    emp_LTC_lbl = Label(VS, text=emp_LTC_txt)
    gap6 = Label(VS)
    gap7 = Label(VS)

    prev_btn = Button(VS, text="<<", state=DISABLED)
    next_btn = Button(VS, text=">>", command=lambda: next(1))
    back_btn = Button(VS, text="Back", command=back)
    add_emp_btn = Button(VS, text="Add employee", command=add_employee)
    change_emp_type_btn = Button(VS, text="Change", command=change_employee_type)

    gap0.grid(row=0, column=0)
    emp_ID_lbl.grid(row=1, column=0, sticky=W, columnspan=3)
    gap1.grid(row=2, column=0)
    emp_FN_lbl.grid(row=3, column=0, sticky=W, columnspan=3)
    gap2.grid(row=4, column=0)
    emp_email_lbl.grid(row=5, column=0, sticky=W, columnspan=3)
    gap3.grid(row=6, column=0)
    emp_DoB_lbl.grid(row=7, column=0, sticky=W, columnspan=3)
    gap4.grid(row=8, column=0)
    emp_type_lbl.grid(row=9, column=0, sticky=W, columnspan=3)
    gap5.grid(row=10, column=0)
    emp_LTC_lbl.grid(row=11, column=0, sticky=W, columnspan=3)
    gap6.grid(row=12, column=0, pady=10)
    gap7.grid(row=14, column=0)

    prev_btn.grid(row=13, column=0, padx=10, sticky=W)
    next_btn.grid(row=13, column=1, padx=290)
    back_btn.grid(row=15, column=0, padx=10, sticky=W)
    add_emp_btn.grid(row=15, column=1)
    change_emp_type_btn.grid(row=9, column=1)

    VS.mainloop()


def loaned_items(ID):
    emp_ID = c.execute("SELECT employee_ID FROM employee WHERE employee_ID=:employee_ID",
                       {'employee_ID': ID}).fetchone()[0]

    loaned_item_list_IDs = []
    loaned_item_user_IDs = []

    LI = c.execute("SELECT * FROM loaned_item").fetchall()

    for li in LI:
        loaned_item_list_IDs.append(li[0])
        loaned_item_user_IDs.append(li[1])

    staff_name = c.execute("SELECT full_name FROM employee WHERE employee_ID=:employee_ID",
                           {'employee_ID': loaned_item_user_IDs[0]}).fetchone()[0]
    item_name = c.execute("SELECT item_name FROM item WHERE item_ID=:item_ID",
                          {'item_ID': loaned_item_list_IDs[0]}).fetchone()[0]
    date_of_request = c.execute("SELECT date_of_request FROM loaned_item WHERE item_ID=:item_ID",
                                {'item_ID': loaned_item_list_IDs[0]}).fetchone()[0]
    amount_requested = c.execute("SELECT request_amount FROM loaned_item WHERE item_ID=:item_ID",
                                 {'item_ID': loaned_item_list_IDs[0]}).fetchone()[0]

    LIW = Tk()
    LIW.title("Loaned Items")
    LIW.geometry("400x320")

    item_name_inf = "Item Name: \t\t" + item_name + " - " + str(loaned_item_list_IDs[0])
    staff_name_inf = "Loaned By: \t\t" + staff_name + " - " + str(loaned_item_user_IDs[0])
    DoR = "Date of Request: \t\t" + str(date_of_request)
    AR = "Amount Loaned: \t\t" + str(amount_requested)

    def next(index):
        staff_name = c.execute("SELECT full_name FROM employee WHERE employee_ID=:employee_ID",
                               {'employee_ID': loaned_item_user_IDs[index]}).fetchone()[0]
        item_name = c.execute("SELECT item_name FROM item WHERE item_ID=:item_ID",
                              {'item_ID': loaned_item_list_IDs[index]}).fetchone()[0]
        date_of_request = c.execute("SELECT date_of_request FROM loaned_item WHERE item_ID=:item_ID",
                                    {'item_ID': loaned_item_list_IDs[index]}).fetchone()[0]
        amount_requested = c.execute("SELECT request_amount FROM loaned_item WHERE item_ID=:item_ID",
                                     {'item_ID': loaned_item_list_IDs[index]}).fetchone()[0]

        item_name_inf = "Item Name: \t\t" + item_name + " - " + str(loaned_item_list_IDs[index])
        staff_name_inf = "Loaned By: \t\t" + staff_name + " - " + str(loaned_item_user_IDs[index])
        DoR = "Date of Request: \t\t" + str(date_of_request)
        AR = "Amount Loaned: \t\t" + str(amount_requested)

        item_name_lbl.config(text=item_name_inf)
        staff_name_lbl.config(text=staff_name_inf)
        DoR_lbl.config(text=DoR)
        AR_lbl.config(text=AR)

        next_btn = Button(LIW, text=">>", command=lambda: next(index + 1))
        prev_btn = Button(LIW, text="<<", command=lambda: previous(index - 1))

        if index == len(loaned_item_list_IDs) - 1:
            next_btn = Button(LIW, text=">>", state=DISABLED)
        # if index == 0:
        #     prev_btn = Button(LIW, text="<<", state=DISABLED)
        #     prev_btn.grid(row=9, column=0, padx=20)

        next_btn.grid(row=9, column=2)
        prev_btn.grid(row=9, column=0, padx=20)

    def previous(index):
        staff_name = c.execute("SELECT full_name FROM employee WHERE employee_ID=:employee_ID",
                               {'employee_ID': loaned_item_user_IDs[index]}).fetchone()[0]
        item_name = c.execute("SELECT item_name FROM item WHERE item_ID=:item_ID",
                              {'item_ID': loaned_item_list_IDs[index]}).fetchone()[0]
        date_of_request = c.execute("SELECT date_of_request FROM loaned_item WHERE item_ID=:item_ID",
                                    {'item_ID': loaned_item_list_IDs[index]}).fetchone()[0]
        amount_requested = c.execute("SELECT request_amount FROM loaned_item WHERE item_ID=:item_ID",
                                     {'item_ID': loaned_item_list_IDs[index]}).fetchone()[0]

        item_name_inf = "Item Name: \t\t" + item_name + " - " + str(loaned_item_list_IDs[index])
        staff_name_inf = "Loaned By: \t\t" + staff_name + " - " + str(loaned_item_user_IDs[index])
        DoR = "Date of Request: \t\t" + str(date_of_request)
        AR = "Amount Loaned: \t\t" + str(amount_requested)

        item_name_lbl.config(text=item_name_inf)
        staff_name_lbl.config(text=staff_name_inf)
        DoR_lbl.config(text=DoR)
        AR_lbl.config(text=AR)

        next_btn = Button(LIW, text=">>", command=lambda: next(index + 1))
        prev_btn = Button(LIW, text="<<", command=lambda: previous(index - 1))
        # if index == len(loaned_item_list_IDs)-1:
        #     next_btn.config(state=DISABLED)
        if index == 0:
            prev_btn = Button(LIW, text="<<", state=DISABLED)

        next_btn.grid(row=9, column=2)
        prev_btn.grid(row=9, column=0, padx=20)

    def back():
        LIW.destroy()
        admin_win(emp_ID)

    gap0 = Label(LIW)
    item_name_lbl = Label(LIW, text=item_name_inf)
    gap1 = Label(LIW)
    staff_name_lbl = Label(LIW, text=staff_name_inf)
    gap2 = Label(LIW)
    DoR_lbl = Label(LIW, text=DoR)
    gap3 = Label(LIW)
    AR_lbl = Label(LIW, text=AR)
    gap4 = Label(LIW)
    gap5 = Label(LIW)

    prev_btn = Button(LIW, text="<<", state=DISABLED)
    next_btn = Button(LIW, text=">>", command=lambda: next(1))
    back_btn = Button(LIW, text="Back", command=back)

    gap0.grid(row=0, column=0, pady=10)
    item_name_lbl.grid(row=1, column=0, sticky=W, columnspan=3)
    gap1.grid(row=2, column=0)
    staff_name_lbl.grid(row=3, column=0, sticky=W, columnspan=3)
    gap2.grid(row=4, column=0)
    DoR_lbl.grid(row=5, column=0, sticky=W, columnspan=3)
    gap3.grid(row=6, column=0)
    AR_lbl.grid(row=7, column=0, sticky=W, columnspan=3)
    gap4.grid(row=8, column=0)
    gap5.grid(row=10, column=0, pady=10)

    prev_btn.grid(row=9, column=0, padx=20)
    next_btn.grid(row=9, column=2, padx=230)
    back_btn.grid(row=11, column=0)

    LIW.mainloop()


def inventory(ID):
    emp_ID = c.execute("SELECT employee_ID FROM employee WHERE employee_ID=:employee_ID",
                       {'employee_ID': ID}).fetchone()[0]

    item_list = []

    all_items = c.execute("SELECT * FROM item").fetchall()

    for list_item in all_items:
        item_list.append(list_item)
    #     print(item)
    #
    # print(item_list)

    inv = Tk()
    inv.geometry("400x445")
    inv.title("Inventory")

    item_ID_txt = "Item's ID\t\t - \t" + str(item_list[0][0])
    item_name_txt = "Item's name\t - \t" + str(item_list[0][1])
    item_cost_txt = "Item's cost\t - \t" + str(item_list[0][2])
    num_of_item_txt = "Number of item\t - \t" + str(item_list[0][3])
    threshold_value_txt = "Threshold value\t - \t" + str(item_list[0][5])
    date_of_purchase_txt = "Date of purchase\t - \t" + str(item_list[0][4])
    description_txt = "Item's description\t - \t" + str(item_list[0][6])
    item_type_txt = "Item type\t - \t" + str(item_list[0][7])

    def add_to_inventory():
        A2I = Toplevel()
        A2I.geometry("390x315")
        A2I.title("Inventory")

        def get_item_info():
            Label(A2I, text="                                  ").grid(row=2, column=1)
            Label(A2I, text="                                  ").grid(row=4, column=1)
            Label(A2I, text="                                  ").grid(row=6, column=1)
            Label(A2I, text="                                  ").grid(row=8, column=1)
            Label(A2I, text="                                  ").grid(row=10, column=1)
            Label(A2I, text="                                  ").grid(row=12, column=1)

            rand_item_int = random.randint(555555555, 999999999)
            today = date.today()
            day = today.strftime("%d")
            month = today.strftime("%m")
            year = today.strftime("%Y")[2:4]
            todays_date = day + "/" + month + "/" + year

            if IN_ent.get() == "":
                Label(A2I, text="Invalid Input", fg="red").grid(row=2, column=1)
            if IC_ent.get() == "":
                Label(A2I, text="Invalid Input", fg="red").grid(row=4, column=1)
            if NoI_ent.get() == "":
                Label(A2I, text="Invalid Input", fg="red").grid(row=6, column=1)
            if THV_ent.get() == "":
                Label(A2I, text="Invalid Input", fg="red").grid(row=8, column=1)
            if IT_ent.get() == "":
                Label(A2I, text="Invalid Input", fg="red").grid(row=12, column=1)

            if IN_ent.get() != "" and IC_ent.get() != "" and NoI_ent.get() != "" and THV_ent.get() != "" \
                    and IT_ent.get() != "":
                if D_ent.get() == "":
                    response = messagebox.askyesno("Add Item?", "Are you sure to add this item?")
                    if response == 1:
                        add_item_class = item(rand_item_int, IN_ent.get(), IC_ent.get(), NoI_ent.get(),
                                              str(todays_date), THV_ent.get(), "None", IT_ent.get())
                        insert_item(add_item_class)
                        messagebox.showinfo("Success!", "The item has been added in the inventory!")
                        A2I.destroy()
                        inv.destroy()
                        inventory(emp_ID)
                    else:
                        A2I.destroy()
                        inv.destroy()
                        inventory(emp_ID)
                else:
                    response = messagebox.askyesno("Add Item?", "Are you sure to add this item?")
                    if response == 1:
                        add_item_class = item(rand_item_int, IN_ent.get(), IC_ent.get(), NoI_ent.get(),
                                              str(todays_date), THV_ent.get(), "None", IT_ent.get())
                        insert_item(add_item_class)
                        messagebox.showinfo("Success!", "The item has been added in the inventory!")
                        A2I.destroy()
                        inv.destroy()
                        inventory(emp_ID)
                    else:
                        A2I.destroy()
                        inv.destroy()
                        inventory(emp_ID)
            else:
                pass

        gap_0 = Label(A2I)
        IN_lbl = Label(A2I, text="Item name: ")
        gap_1 = Label(A2I)
        IC_lbl = Label(A2I, text="Item cost: ")
        gap_2 = Label(A2I)
        NoI_lbl = Label(A2I, text="Quantity of purchase: ")
        gap_3 = Label(A2I)
        THV_lbl = Label(A2I, text="Threshold value: ")
        gap_4 = Label(A2I)
        D_lbl = Label(A2I, text="Description: ")
        gap_5 = Label(A2I)
        IT_lbl = Label(A2I, text="Item type: ")
        gap_6 = Label(A2I)

        IN_ent = Entry(A2I, width=40)
        IC_ent = Entry(A2I, width=40)
        NoI_ent = Entry(A2I, width=40)
        THV_ent = Entry(A2I, width=40)
        D_ent = Entry(A2I, width=40)
        IT_ent = Entry(A2I, width=40)

        close_btn = Button(A2I, text="Close", command=A2I.destroy)
        add_item_btn = Button(A2I, text="Purchase", command=get_item_info)

        gap_0.grid(row=0, column=0)
        IN_lbl.grid(row=1, column=0, sticky=W)
        gap_1.grid(row=2, column=0)
        IC_lbl.grid(row=3, column=0, sticky=W)
        gap_2.grid(row=4, column=0)
        NoI_lbl.grid(row=5, column=0, sticky=W)
        gap_3.grid(row=6, column=0)
        THV_lbl.grid(row=7, column=0, sticky=W)
        gap_4.grid(row=8, column=0)
        D_lbl.grid(row=9, column=0, sticky=W)
        gap_5.grid(row=10, column=0)
        IT_lbl.grid(row=11, column=0, sticky=W)
        gap_6.grid(row=12, column=0)

        IN_ent.grid(row=1, column=1, sticky=W)
        IC_ent.grid(row=3, column=1, sticky=W)
        NoI_ent.grid(row=5, column=1, sticky=W)
        THV_ent.grid(row=7, column=1, sticky=W)
        D_ent.grid(row=9, column=1, sticky=W)
        IT_ent.grid(row=11, column=1, sticky=W)

        close_btn.grid(row=13, column=0)
        add_item_btn.grid(row=13, column=1)

    def purchase():
        pur = Toplevel()
        pur.geometry("400x230")

        def increase_item_number():
            Label(pur, text="                               ").grid(row=8, column=1)
            the_increase = num_of_purchase_ent.get()
            if the_increase != "":
                the_sum = int(the_increase) + item_list[0][3]
                response = messagebox.askyesno("Increase Item's Quantity", "Are you sure to make the purchase?")
                if response == 1:
                    with conn:
                        c.execute("""UPDATE item SET number_of_items=:number_of_items
                                    WHERE item_ID=:item_ID""",
                                  {"item_ID": item_list[0][0], "number_of_items": the_sum})
                    messagebox.showinfo("Success!", "The quantity of the item has been increased in the inventory!")
                    pur.destroy()
                    inv.destroy()
                    inventory(emp_ID)
                else:
                    pass
            else:
                Label(pur, text="Key in a number", fg="red").grid(row=8, column=1)

        gap_0 = Label(pur)
        pur_item_name_lbl = Label(pur, text=item_name_txt)
        gap_1 = Label(pur)
        pur_threshold_value_lbl = Label(pur, text=threshold_value_txt)
        gap_2 = Label(pur)
        pur_num_of_items_lbl = Label(pur, text=num_of_item_txt)
        gap_3 = Label(pur)
        num_of_purchase_lbl = Label(pur, text="Number of purchase= ")
        gap_4 = Label(pur)

        num_of_purchase_ent = Entry(pur, width=30)

        close_btn = Button(pur, text="Close", command=pur.destroy)
        confirm_purchase_btn = Button(pur, text="Purchase", command=increase_item_number)

        gap_0.grid(row=0, column=0)
        pur_item_name_lbl.grid(row=1, column=0, sticky=W, columnspan=2)
        gap_1.grid(row=2, column=0)
        pur_threshold_value_lbl.grid(row=3, column=0, sticky=W, columnspan=2)
        gap_2.grid(row=4, column=0)
        pur_num_of_items_lbl.grid(row=5, column=0, sticky=W, columnspan=2)
        gap_3.grid(row=6, column=0)
        num_of_purchase_lbl.grid(row=7, column=0, sticky=W)
        gap_4.grid(row=8, column=0)

        num_of_purchase_ent.grid(row=7, column=1, sticky=W)

        close_btn.grid(row=9, column=0)
        confirm_purchase_btn.grid(row=9, column=1)

    def previous(index):
        item_ID_txt = "Item's ID\t\t - \t" + str(item_list[index][0])
        item_name_txt = "Item's name\t - \t" + str(item_list[index][1])
        item_cost_txt = "Item's cost\t - \t" + str(item_list[index][2])
        num_of_item_txt = "Number of item\t - \t" + str(item_list[index][3])
        threshold_value_txt = "Threshold value\t - \t" + str(item_list[index][5])
        date_of_purchase_txt = "Date of purchase\t - \t" + str(item_list[index][4])
        description_txt = "Item's description\t - \t" + str(item_list[index][6])
        item_type_txt = "Item type\t - \t" + str(item_list[index][7])

        item_ID_lbl.config(text=item_ID_txt)
        item_name_lbl.config(text=item_name_txt)
        item_cost_lbl.config(text=item_cost_txt)
        num_of_items_lbl.config(text=num_of_item_txt)
        threshold_value_lbl.config(text=threshold_value_txt)
        date_of_purchase_lbl.config(text=date_of_purchase_txt)
        description_lbl.config(text=description_txt)
        item_type_lbl.config(text=item_type_txt)

        prev_btn = Button(inv, text="<<", command=lambda: previous(index - 1))
        next_btn = Button(inv, text=">>", command=lambda: next(index + 1))

        if index == 0:
            prev_btn = Button(inv, text="<<", state=DISABLED)

        prev_btn.grid(row=17, column=0, sticky=W, padx=20)
        next_btn.grid(row=17, column=1, padx=80)

    def next(index):
        item_ID_txt = "Item's ID\t\t - \t" + str(item_list[index][0])
        item_name_txt = "Item's name\t - \t" + str(item_list[index][1])
        item_cost_txt = "Item's cost\t - \t" + str(item_list[index][2])
        num_of_item_txt = "Number of item\t - \t" + str(item_list[index][3])
        threshold_value_txt = "Threshold value\t - \t" + str(item_list[index][5])
        date_of_purchase_txt = "Date of purchase\t - \t" + str(item_list[index][4])
        description_txt = "Item's description\t - \t" + str(item_list[index][6])
        item_type_txt = "Item type\t - \t" + str(item_list[index][7])

        item_ID_lbl.config(text=item_ID_txt)
        item_name_lbl.config(text=item_name_txt)
        item_cost_lbl.config(text=item_cost_txt)
        num_of_items_lbl.config(text=num_of_item_txt)
        threshold_value_lbl.config(text=threshold_value_txt)
        date_of_purchase_lbl.config(text=date_of_purchase_txt)
        description_lbl.config(text=description_txt)
        item_type_lbl.config(text=item_type_txt)

        prev_btn = Button(inv, text="<<", command=lambda: previous(index - 1))
        next_btn = Button(inv, text=">>", command=lambda: next(index + 1))

        if index == len(item_list) - 1:
            next_btn = Button(inv, text=">>", state=DISABLED)

        prev_btn.grid(row=17, column=0, sticky=W, padx=20)
        next_btn.grid(row=17, column=1, padx=80)

    def back():
        inv.destroy()
        admin_win(emp_ID)

    gap0 = Label(inv)
    item_ID_lbl = Label(inv, text=item_ID_txt)
    gap1 = Label(inv)
    item_name_lbl = Label(inv, text=item_name_txt)
    gap2 = Label(inv)
    item_cost_lbl = Label(inv, text=item_cost_txt)
    gap3 = Label(inv)
    num_of_items_lbl = Label(inv, text=num_of_item_txt)
    gap4 = Label(inv)
    threshold_value_lbl = Label(inv, text=threshold_value_txt)
    gap5 = Label(inv)
    date_of_purchase_lbl = Label(inv, text=date_of_purchase_txt)
    gap6 = Label(inv)
    description_lbl = Label(inv, text=description_txt)
    gap7 = Label(inv)
    item_type_lbl = Label(inv, text=item_type_txt)
    gap8 = Label(inv)
    gap9 = Label(inv)

    purchase_btn = Button(inv, text="Purchase", command=purchase)
    prev_btn = Button(inv, text="<<", state=DISABLED)
    next_btn = Button(inv, text=">>", command=lambda: next(1))
    back_btn = Button(inv, text="Back", command=back)
    add_item = Button(inv, text="Add Item", command=add_to_inventory)

    gap0.grid(row=0, column=0)
    item_ID_lbl.grid(row=1, column=0, sticky=W, columnspan=3)
    gap1.grid(row=2, column=0)
    item_name_lbl.grid(row=3, column=0, sticky=W, columnspan=3)
    gap2.grid(row=4, column=0)
    item_cost_lbl.grid(row=5, column=0, sticky=W, columnspan=3)
    gap3.grid(row=6, column=0)
    num_of_items_lbl.grid(row=7, column=0, sticky=W, columnspan=3)
    gap4.grid(row=8, column=0)
    threshold_value_lbl.grid(row=9, column=0, sticky=W, columnspan=3)
    gap5.grid(row=10, column=0)
    date_of_purchase_lbl.grid(row=11, column=0, sticky=W, columnspan=3)
    gap6.grid(row=12, column=0)
    description_lbl.grid(row=13, column=0, sticky=W, columnspan=3)
    gap7.grid(row=14, column=0)
    item_type_lbl.grid(row=15, column=0, sticky=W, columnspan=3)
    gap8.grid(row=16, column=0)
    gap9.grid(row=18, column=0)

    purchase_btn.grid(row=7, column=1)
    prev_btn.grid(row=17, column=0, sticky=W, padx=20)
    next_btn.grid(row=17, column=1, padx=260)
    back_btn.grid(row=19, column=0, sticky=W, padx=20)
    add_item.grid(row=19, column=1)

    inv.mainloop()


def admin_win(ID):
    emp_ID = c.execute("SELECT employee_ID FROM employee WHERE employee_ID=:employee_ID",
                       {'employee_ID': ID}).fetchone()
    emp_FN = c.execute("SELECT full_name FROM employee WHERE employee_ID=:employee_ID",
                       {'employee_ID': ID}).fetchone()

    AP = Tk()
    AP.geometry("400x485")
    AP.title("Administrator")

    # functions:
    """
    - remove employee or make employee admin
    - view inventory
    - view loan request from employee
    - grant or deny request
    - update the item list
    """

    def logout_function():
        AP.destroy()
        login_win()

    def view_user_details():
        AP.destroy()
        personal_details(emp_ID[0])

    def view_loaned_items():
        AP.destroy()
        loaned_items(emp_ID[0])

    def view_inventory():
        AP.destroy()
        inventory(emp_ID[0])

    def view_employees():
        AP.destroy()
        view_staff(emp_ID[0])

    emp_ID_text = "Employee's ID: " + str(emp_ID[0])
    emp_FN_text = "Employee's Full name: " + str(emp_FN[0])

    emp_ID_label = Label(AP, text=emp_ID_text)
    emp_FN_label = Label(AP, text=emp_FN_text)

    blank0 = Label(AP)
    view_emp_btn = Button(AP, text="View Employees", command=view_employees, pady=20, width=48)
    blank1 = Label(AP)
    view_loaned_items = Button(AP, text="View Loaned Items", command=view_loaned_items, pady=20, width=48)
    blank2 = Label(AP)
    view_inventory = Button(AP, text="View Inventory", command=view_inventory, pady=20, width=48)
    blank3 = Label(AP)
    view_pers_details = Button(AP, text="View Personal Details", command=view_user_details, pady=20, width=48)
    blank4 = Label(AP)
    logout_button = Button(AP, text="Logout", command=logout_function, pady=20, width=48)

    emp_ID_label.grid(row=0, column=0, sticky=W, columnspan=2)
    emp_FN_label.grid(row=1, column=0, sticky=W, columnspan=2)

    blank0.grid(row=2, column=0)
    view_emp_btn.grid(row=3, column=0, padx=30)
    blank1.grid(row=4, column=0)
    view_loaned_items.grid(row=5, column=0, padx=30)
    blank2.grid(row=6, column=0)
    view_inventory.grid(row=7, column=0, padx=30)
    blank3.grid(row=8, column=0)
    view_pers_details.grid(row=9, column=0, padx=30)
    blank4.grid(row=10, column=0)
    logout_button.grid(row=11, column=0, padx=30)

    AP.mainloop()


def manager_win(ID):
    MW = Tk()
    MW.title("Manager")

    # functions:
    """

    """

    def logout_function():
        MW.destroy()
        login_win()

    def view_user_details():
        pass

    MW.mainloop()


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
        login_win()

    def view_user_details():
        pass

    SW.mainloop()


admin_win("185908204")

# login_win()

conn.close()
