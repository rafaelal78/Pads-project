from tkinter import Tk, messagebox, Label, N, Entry, Button, W

def retrieve_PW_win():
    RPW = Tk()
    RPW.geometry("360x210")
    RPW.title("Retrieve Password")

    def back_to_login():
        RPW.destroy()
        from login_window import login_win
        login_win()

    #   This function verifies if the keyed in email exists, if not,
    #   passes on a message beneath the entry "Invalid Email",
    #   if the email exists, it opens a message box displaying some user
    #   information.
    #   If the user clicks on the button without keying anything in
    #   entry, passes on a message "Invalid Email"
    def ver_email():
        import sqlite3
        conn = sqlite3.connect("PIMS")
        c = conn.cursor()

        Label(RPW, text="                                ").grid(row=2, column=1, sticky=N)
        if email_entry.get() != "":
            if c.execute("SELECT email FROM employee WHERE email=:email",
                         {'email': email_entry.get()}).fetchone()[0] is not None:
                details_wind(email_entry.get())
            else:
                Label(RPW, text="Invalid Email", fg="red").grid(row=2, column=1, sticky=N)
        else:
            Label(RPW, text="Invalid Email", fg="red").grid(row=2, column=1, sticky=N)

    #   the message box displays user information, also asks user
    #   if he wants to stay in the window or not, if not,
    #   closes the window and opens the login_win
    def details_wind(email):
        email_entry.delete(0, "end")

        import sqlite3
        conn = sqlite3.connect("PIMS")
        c = conn.cursor()

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
            conn.close()
            from login_window import login_win
            login_win()
        else:
            pass

    #   Labels
    blank0 = Label(RPW)
    email_text = Label(RPW, text="Email")
    blank1 = Label(RPW)
    back_button = Button(RPW, text="Back", command=back_to_login)
    confirm_button = Button(RPW, text="Confirm", command=ver_email)

    #   Entries
    email_entry = Entry(RPW, width=45)

    #   Grids
    blank0.grid(row=0, column=0, pady=30)
    email_text.grid(row=1, column=0, padx=10, sticky=W)
    email_entry.grid(row=1, column=1)
    blank1.grid(row=2, column=0, pady=20)
    back_button.grid(row=3, column=0, sticky=W)
    confirm_button.grid(row=3, column=1)

    RPW.mainloop()