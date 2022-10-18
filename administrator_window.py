from tkinter import Tk, Label, Button, W

def admin_win(ID):
    import sqlite3
    conn = sqlite3.connect("PIMS")
    c = conn.cursor()

    emp_ID = c.execute("SELECT employee_ID FROM employee WHERE employee_ID=:employee_ID",
                       {'employee_ID': ID}).fetchone()
    emp_FN = c.execute("SELECT full_name FROM employee WHERE employee_ID=:employee_ID",
                       {'employee_ID': ID}).fetchone()

    #   Administrator window with the user's information displayed
    #   on top left corner.
    #   This window calls in admins' functions through buttons.

    AP = Tk()
    AP.geometry("400x485")
    AP.title("Administrator")

    #   Each button opens windows of different functions, each closes
    #   this window.
    def logout_function():
        AP.destroy()
        conn.close()
        from login_window import login_win
        login_win()

    def view_user_details():
        AP.destroy()
        conn.close()
        from personal_details_window import personal_details
        personal_details(emp_ID[0])

    def view_loaned_items():
        AP.destroy()
        conn.close()
        from loaned_items_window import loaned_items
        loaned_items(emp_ID[0])

    def view_inventory():
        AP.destroy()
        conn.close()
        from inventory_window import inventory
        inventory(emp_ID[0])

    def view_employees():
        AP.destroy()
        conn.close()
        from view_staff_window import view_staff
        view_staff(emp_ID[0])

    emp_ID_text = "Employee's ID: " + str(emp_ID[0])
    emp_FN_text = "Employee's Full name: " + str(emp_FN[0])

    emp_ID_label = Label(AP, text=emp_ID_text)
    emp_FN_label = Label(AP, text=emp_FN_text)

    #   Labels
    blank0 = Label(AP)
    view_emp_btn = Button(AP, text="View Employees", command=view_employees, pady=20, width=48)
    blank1 = Label(AP)
    view_loaned_items = Button(AP, text="View Loaned Items", command=view_loaned_items, pady=20, width=48)
    blank2 = Label(AP)
    view_inventory = Button(AP, text="View Inventory", command=view_inventory, pady=20, width=48)
    blank3 = Label(AP)
    view_pers_details = Button(AP, text="View Personal Details", command=view_user_details, pady=20, width=48)
    blank4 = Label(AP)

    #   Button
    logout_button = Button(AP, text="Logout", command=logout_function, pady=20, width=48)

    #   Grid
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