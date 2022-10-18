from tkinter import Tk, Toplevel, StringVar, OptionMenu, messagebox, Label, Button, W, DISABLED, Entry
from tkcalendar import Calendar

def view_staff(ID):
    import sqlite3
    conn = sqlite3.connect("PIMS")
    c = conn.cursor()
    emp_ID = c.execute("SELECT employee_ID FROM employee WHERE employee_ID=:employee_ID",
                       {'employee_ID': ID}).fetchone()[0]
    emps = c.execute("SELECT * FROM employee WHERE employee_ID=:employee_ID",
                     {'employee_ID': ID}).fetchone()

    """
    
        This list variable is used to store other
        user's ID for later use.
        
    """

    staff_list = []
    staff = c.execute("SELECT * FROM employee").fetchall()
    staff.remove(emps)

    """
    
        For each user, insert their IDs
        in the staff_list
    
    """

    for emp in staff:
        staff_list.append(emp)

    VS = Tk()
    VS.title("Employees")
    VS.geometry("425x385")

    """
    
        This window displays every information about other users.
        Clicking on the button "<<" or ">>" will display information
        about different users.
    
    """

    emp_ID_txt = "Employee ID\t\t - \t" + str(staff_list[0][0])
    emp_FN_txt = "Employee Fullname\t - \t" + str(staff_list[0][1])
    emp_email_txt = "Employee Email\t\t - \t" + str(staff_list[0][2])
    emp_DoB_txt = "Employee Date of birth\t - \t" + str(staff_list[0][4])
    emp_type_txt = "Employee Type\t\t - \t" + str(staff_list[0][5])
    emp_LTC_txt = "Employee Loan total cost\t - \t" + str(staff_list[0][6])

    emp_type_list = ["admin", "manager", "staff"]

    def back():
        VS.destroy()
        conn.close()
        from administrator_window import admin_win
        admin_win(emp_ID)

        """
        
            next(index) and previous(index) functions are
            copies of each other while the difference
            is that next(index) will disable next_btn
            at the length of a list -1 while
            previous(index) will disable back_btn if
            index is equals to 0.        
        
        """

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

    """
    
        next(index) and previous(index) functions are
        copies of each other while the difference
        is that next(index) will disable next_btn
        at the length of a list -1 while
        previous(index) will disable back_btn if
        index is equals to 0.    
    
    """

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

    """
    
        This function opens a window bound to the
        view staff window, allowing certain users to
        create accounts to add users.
    
    """

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

            import random
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

                    from Classes import employee

                    def insert_emp(emp):
                        with conn:
                            c.execute("INSERT INTO employee VALUES"
                                      "(:employee_ID, :full_name, :email, :password, :date_of_birth, :employee_type, :loan_total_cost)",
                                      {'employee_ID': emp.ID, "full_name": emp.name, "email": emp.email,
                                       "password": emp.password, "date_of_birth": emp.DoB,
                                       "employee_type": emp.ET, "loan_total_cost": 0})

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

        #   Label
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

        #   Entries
        FN_ent = Entry(AE, width=40)
        email_ent = Entry(AE, width=40)
        PW_ent = Entry(AE, width=40)
        confirm_PW_ent = Entry(AE, width=40)
        # employee_type_ent = Entry(AE, width=40)

        #   Miscellaneous
        cal = Calendar(AE, selectmode='day')
        close_btn = Button(AE, text="Close", command=AE.destroy)
        add_employee_btn = Button(AE, text="Confirm", command=get_emp_info)

        #   Grids
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

    """
    
        This function opens a window bound to the
        view staff window, allowing certain users to
        change an other employee's type.
    
    """

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

        #   Labels
        gap_0 = Label(CET)
        emp_ID_lbl = Label(CET, text="Employee ID\t\t - \t")
        ID_lbl = Label(CET, text=str(staff_list[0][0]))
        gap_1 = Label(CET)
        emp_FN_lbl = Label(CET, text="Employee Fullname\t - \t")
        FN_lbl = Label(CET, text=str(staff_list[0][1]))
        gap_2 = Label(CET)
        emp_type_lbl = Label(CET, text="Employee Type\t\t - \t")
        gap_3 = Label(CET)

        #   Buttons
        close_btn = Button(CET, text="Close", command=CET.destroy)
        confirm_btn = Button(CET, text="Confirm", command=confirm_change)

        #   Grids
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

    #   Labels
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

    #   Buttons
    prev_btn = Button(VS, text="<<", state=DISABLED)
    next_btn = Button(VS, text=">>", command=lambda: next(1))
    back_btn = Button(VS, text="Back", command=back)
    add_emp_btn = Button(VS, text="Add employee", command=add_employee)
    change_emp_type_btn = Button(VS, text="Change", command=change_employee_type)

    #   Grids
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

# view_staff("185908204")