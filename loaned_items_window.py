from tkinter import Tk, Button, DISABLED, Label, W

def loaned_items(ID):
    import sqlite3
    conn = sqlite3.connect("PIMS")
    c = conn.cursor()
    emp_ID = c.execute("SELECT employee_ID FROM employee WHERE employee_ID=:employee_ID",
                       {'employee_ID': ID}).fetchone()[0]

    #   Each to store loaned items' ID for later use
    loaned_item_list_IDs = []
    loaned_item_user_IDs = []

    LI = c.execute("SELECT * FROM loaned_item").fetchall()

    #   For each loaned items, insert only the items'
    #   as well as users' IDs in their respective
    #   lists for later use.
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

    #   This window displays each loaned item's information
    #   as well as the item's and user's ID. Clicking
    #   on "<<" or ">>" will either change the information
    #   to the previous or next loaned items respectively.
    #   the parameter index on both next and previous
    #   functions are used to refer to the position
    #   of each loaned items.

    #   next(index) and previous(index) functions are
    #   copies of each other while the difference
    #   is that next(index) will disable next_btn
    #   at the length of a list -1 while
    #   previous(index) will disable back_btn if
    #   index is equals to 0.
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

        #   config is used to alter text
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

    #   next(index) and previous(index) functions are
    #   copies of each other while the difference
    #   is that next(index) will disable next_btn
    #   at the length of a list -1 while
    #   previous(index) will disable back_btn if
    #   index is equals to 0.
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

        #   config is used to alter text
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
        conn.close()
        from administrator_window import admin_win
        admin_win(emp_ID)

    #   Labels
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

    #   Buttons
    prev_btn = Button(LIW, text="<<", state=DISABLED)
    next_btn = Button(LIW, text=">>", command=lambda: next(1))
    back_btn = Button(LIW, text="Back", command=back)

    #   Grids
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
