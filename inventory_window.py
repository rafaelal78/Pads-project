from tkinter import Toplevel, Label, messagebox, Entry, Button, W, DISABLED, Tk

def inventory(ID):
    import sqlite3
    conn = sqlite3.connect("PIMS")
    c = conn.cursor()
    emp_ID = c.execute("SELECT employee_ID FROM employee WHERE employee_ID=:employee_ID",
                       {'employee_ID': ID}).fetchone()[0]

    #   This list variable is used to store items' ID
    #   for later use.
    item_list = []

    all_items = c.execute("SELECT * FROM item").fetchall()

    #   For each item, insert their IDs
    #   in the item_list
    for list_item in all_items:
        item_list.append(list_item)

    inv = Tk()
    inv.geometry("400x445")
    inv.title("Inventory")

    #   This window displays every information about an item.
    #   Clicking on the button "<<" or ">>" users can navigate
    #   through the items, changing information on the window
    #   respective of the items' ID.

    item_ID_txt = "Item's ID\t\t - \t" + str(item_list[0][0])
    item_name_txt = "Item's name\t - \t" + str(item_list[0][1])
    item_cost_txt = "Item's cost\t - \t" + str(item_list[0][2])
    num_of_item_txt = "Number of item\t - \t" + str(item_list[0][3])
    threshold_value_txt = "Threshold value\t - \t" + str(item_list[0][5])
    date_of_purchase_txt = "Date of purchase\t - \t" + str(item_list[0][4])
    description_txt = "Item's description\t - \t" + str(item_list[0][6])
    item_type_txt = "Item type\t - \t" + str(item_list[0][7])

    #   This function will open a window bound to the inventory
    #   window. This window will allow certain users to add
    #   an item.
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

            from datetime import date

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

                        from Classes import item
                        import random
                        rand_item_int = random.randint(555555555, 999999999)  # 9 digits

                        def insert_item(item):
                            with conn:
                                c.execute("INSERT INTO item VALUES"
                                          "(:item_ID, :item_name, :item_cost, :number_of_items, :date_of_purchase, :threshold_value,"
                                          ":description, :item_type)",
                                          {'item_ID': item.ID, "item_name": item.name, "item_cost": item.cost,
                                           "number_of_items": item.number, "date_of_purchase": item.DoP,
                                           "threshold_value": item.TV, "description": item.DP, "item_type": item.IT})

                        add_item_class = item(rand_item_int, IN_ent.get(), IC_ent.get(), NoI_ent.get(),
                                              str(todays_date), THV_ent.get(), "None", IT_ent.get())
                        insert_item(add_item_class)
                        messagebox.showinfo("Success!", "The item has been added in the inventory!")
                        A2I.destroy()
                        inv.destroy()
                        conn.close()
                        inventory(emp_ID)
                    else:
                        A2I.destroy()
                        inv.destroy()
                        inventory(emp_ID)
                else:
                    response = messagebox.askyesno("Add Item?", "Are you sure to add this item?")
                    if response == 1:

                        from Classes import item
                        import random
                        rand_item_int = random.randint(555555555, 999999999)  # 9 digits

                        def insert_item(item):
                            with conn:
                                c.execute("INSERT INTO item VALUES"
                                          "(:item_ID, :item_name, :item_cost, :number_of_items, :date_of_purchase, :threshold_value,"
                                          ":description, :item_type)",
                                          {'item_ID': item.ID, "item_name": item.name, "item_cost": item.cost,
                                           "number_of_items": item.number, "date_of_purchase": item.DoP,
                                           "threshold_value": item.TV, "description": item.DP, "item_type": item.IT})

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

        #   Labels
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

        #   Entries
        IN_ent = Entry(A2I, width=40)
        IC_ent = Entry(A2I, width=40)
        NoI_ent = Entry(A2I, width=40)
        THV_ent = Entry(A2I, width=40)
        D_ent = Entry(A2I, width=40)
        IT_ent = Entry(A2I, width=40)

        #   Buttons
        close_btn = Button(A2I, text="Close", command=A2I.destroy)
        add_item_btn = Button(A2I, text="Purchase", command=get_item_info)

        #   Grids
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

    #   This function will open a window bound to
    #   the inventory window, allowing users to
    #   purchase certain amount of item, depending
    #   on what's displayed on the window.
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
                    conn.close()
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

    #   next(index) and previous(index) functions are
    #   copies of each other while the difference
    #   is that next(index) will disable next_btn
    #   at the length of a list -1 while
    #   previous(index) will disable back_btn if
    #   index is equals to 0.
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

    #   next(index) and previous(index) functions are
    #   copies of each other while the difference
    #   is that next(index) will disable next_btn
    #   at the length of a list -1 while
    #   previous(index) will disable back_btn if
    #   index is equals to 0.
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
        conn.close()
        from administrator_window import admin_win
        admin_win(emp_ID)

    #   Labels
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

    #   Buttons
    purchase_btn = Button(inv, text="Purchase", command=purchase)
    prev_btn = Button(inv, text="<<", state=DISABLED)
    next_btn = Button(inv, text=">>", command=lambda: next(1))
    back_btn = Button(inv, text="Back", command=back)
    add_item = Button(inv, text="Add Item", command=add_to_inventory)

    #   Grids
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
