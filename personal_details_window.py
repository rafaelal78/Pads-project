from tkinter import Tk, Toplevel, Label, messagebox, Entry, Button, N, W

def personal_details(ID):
    import sqlite3
    conn = sqlite3.connect("PIMS")
    c = conn.cursor()
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

    #   Each function opens a window bound to the personal_details
    #   window, each function opens a window that users can use
    #   to alter their own personal details.
    #   If the alteration is made, a message box will appear telling
    #   the user a change has been successful, taking the user
    #   back to the administrator window using the admin's ID
    def change_FN():
        CFN = Toplevel()
        CFN.geometry("400x150")
        CFN.title("Update Employee detail")

        #   This window is used to change user's first name.

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
                    conn.close()
                    from administrator_window import admin_win
                    admin_win(emp_ID[0])
                else:
                    pass
            else:
                Label(CFN, text="Fill In The Entry", fg="red").grid(row=2, column=1, sticky=N)

        #   Labels
        blank_0 = Label(CFN)
        FN_lbl = Label(CFN, text="First Name:")
        FN_ent = Entry(CFN, width=50)
        blank_1 = Label(CFN)

        #   Buttons
        close_window = Button(CFN, text="Close", command=CFN.destroy)
        confirm_button = Button(CFN, text="Confirm", command=confirm_change)

        #   Grids
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

        #   This window is used to change user's email.

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
                    conn.close()
                    from administrator_window import admin_win
                    admin_win(emp_ID[0])
                else:
                    pass
            else:
                Label(CE, text="Fill In The Entry", fg="red").grid(row=2, column=1, sticky=N)

        #   Labels
        blank_0 = Label(CE)
        email_lbl = Label(CE, text="Email:")
        email_ent = Entry(CE, width=50)
        blank_1 = Label(CE)

        #   Buttons
        close_window = Button(CE, text="Close", command=CE.destroy)
        confirm_button = Button(CE, text="Confirm", command=confirm_change)

        #   Grids
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

        #   This window is used to change user's password.
        #   The user is asked to key in the initial password,
        #   if successful, a window will be opened requiring
        #   the user to key in the new password twice, if both
        #   don't match the function will pass on a message
        #   "Passwords don't match!", else, will pop up a
        #   message box asking the user whether to confirm
        #   changes. If yes, will close the opened windows
        #   and open admin_win, if not, will close the pop up.

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
                            conn.close()
                            from administrator_window import admin_win
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

        #   Label
        blank_0 = Label(CPW)
        PW_lbl = Label(CPW, text="Password:")
        PW_ent = Entry(CPW, width=50, show="*")
        blank_1 = Label(CPW)

        #   Buttons
        close_window = Button(CPW, text="Close", command=CPW.destroy)
        confirm_button = Button(CPW, text="Confirm", command=ver_PW)

        #   Grids
        blank_0.grid(row=0, column=1, pady=15)
        PW_lbl.grid(row=1, column=0)
        PW_ent.grid(row=1, column=1)
        blank_1.grid(row=2, column=0, pady=10)

        close_window.grid(row=3, column=0)
        confirm_button.grid(row=3, column=1)

    def change_DoB():
        from tkcalendar import Calendar

        CDoB = Toplevel()
        CDoB.geometry("330x260")
        CDoB.title("Update Employee detail")

        #   This window is used to change user's date of birth using a calendar.

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
                conn.close()
                from administrator_window import admin_win
                admin_win(emp_ID[0])
            else:
                pass

        #   Labels
        blank_0 = Label(CDoB)
        blank_1 = Label(CDoB)

        #   Tkinter calendar
        cal = Calendar(CDoB, selectmode='day')

        #   Buttons
        prev_win = Button(CDoB, text="Close", command=CDoB.destroy)
        confirm_button = Button(CDoB, text="Confirm", command=change_DoB)

        #   Grids
        blank_0.grid(row=0, column=0)
        cal.grid(row=1, column=1)
        blank_1.grid(row=2, column=0)
        prev_win.grid(row=3, column=0)
        confirm_button.grid(row=3, column=1)

    def back():
        PD.destroy()
        from administrator_window import admin_win
        admin_win(emp_ID[0])

    emp_ID_txt = "Employee's ID: " + str(emp_ID[0])
    emp_FN_txt = "Employee's First Name: " + str(emp_FN[0])
    emp_email_txt = "Employee's Email: " + str(emp_email[0])
    emp_PW_txt = "Employee's Password: " + str(len(emp_PW[0]) * "*")
    emp_DoB_txt = "Employee's Date of Birth: " + str(emp_DoB[0])

    #   Labels
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

    #   Buttons
    upd_emp_FN = Button(PD, text="○", command=change_FN)
    upd_emp_email = Button(PD, text="○", command=change_email)
    upd_emp_PW = Button(PD, text="○", command=change_PW)
    upd_emp_DoB = Button(PD, text="○", command=change_DoB)
    back_button = Button(PD, text="Back", command=back)

    #   Grids
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

personal_details(185908204)