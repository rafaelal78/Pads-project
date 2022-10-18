import sqlite3
from tkinter import *
import tkinter.messagebox

employee_id_list = []
full_name_list = []
email_list = []
employee_type_list = []
loan_total_cost_list = []
item_ID_list = []
item_name_list = []
item_cost_list = []
number_of_items_list = []
item_type_list = []
date_of_request_list = []
request_amount_list = []

conn = sqlite3.connect("PIMS")
c = conn.cursor()
print("Opened database successfully")

c.execute("INSERT INTO employee (employee_ID, full_name, email, password, date_of_birth, employee_type, loan_total_cost) \
      VALUES (10086,'marksheng','markshengcn@gmai.com','123456','1990325','Boss',1499)")


cursor = c.execute("SELECT employee_ID, full_name, email, password, date_of_birth, employee_type, loan_total_cost  from employee")

for row in cursor:
    employee_id_list.append(row[0])
    print("employee_ID = ", row[0])
    full_name_list.append(row[1])
    print("full_name = ", row[1])
    email_list.append(row[2])
    print("email = ", row[2])
    print("password = ", row[3])
    print("date_of_birth = ", row[4])
    employee_type_list.append(row[5])
    print("employee_type = ", row[5])
    loan_total_cost_list.append(row[6])
    print("loan_total_cost = ", row[6])

cursor2 = c.execute("SELECT item_ID,item_name,item_cost,number_of_items,date_of_purchase,threshold_value,description,item_type from item")

for row in cursor2:
    item_ID_list.append(row[0])
    print("item_ID = ", row[0])
    item_name_list.append(row[1])
    print("item_name = ", row[1])
    item_cost_list.append(row[2])
    print("item_cost = ", row[2])
    number_of_items_list.append(row[3])
    print("number_of_items = ", row[3])
    print("date_of_purchase = ", row[4])
    print("threshold_value = ", row[5])
    print("description = ", row[6])
    item_type_list.append(row[7])
    print("item_type = ", row[7])


cursor3 = c.execute("SELECT item_ID, employee_ID,date_of_request,request_amount from loaned_item")
for row in cursor3:
    print("item_ID = ", row[0])
    print("employee_ID = ", row[1])
    date_of_request_list.append(row[2])
    print("date_of_request = ", row[2])
    request_amount_list.append(row[3])
    print("request_amount = ", row[3])

print("Operation done successfully")
conn.close()

print(employee_id_list)
print(full_name_list)
print(email_list)
print(employee_type_list)
print(loan_total_cost_list)
print(item_ID_list)
print(item_name_list)
print(item_cost_list)
print(number_of_items_list)
print(item_type_list)
print(date_of_request_list)
print(request_amount_list)


#c.execute('''INSERT INTO employee VALUES (10086,"marksheng","markshengcn@gmai.com","123456","1990325","Boss",1499)''')
#c.execute('''SELECT * FROM item''')
#c.execute('''SELECT * FROM loaned_item''')

def manager_win(ID, Item_ID):
    MW = Tk()
    MW.title("Manager")
    MW.geometry("500x600")
    mainframe = Frame(MW)
    mainframe.grid(column=10, row=10)

    for i in range(len(employee_id_list)):

        employee_ID = employee_id_list[i]
        full_name = full_name_list[i]
        email = email_list[i]
        employee_type = employee_type_list[i]
        loan_total_cost = loan_total_cost_list[i]

        item_ID = item_ID_list[i]
        item_name = item_name_list[i]
        item_cost = item_cost_list[i]
        number_of_items = number_of_items_list[i]
        item_type = item_type_list[i]


        date_of_request = date_of_request_list[i]
        request_amount = request_amount_list[i]


    # Display the data
    counter = tkinter.IntVar()
    def onClick(event=None):
        counter.set(counter.get() + 1)
        print(employee_id_list[int(counter.get())])

        employee_ID_result = employee_id_list[int(counter.get())]
        full_name_result = full_name_list[int(counter.get())]
        email_result = email_list[int(counter.get())]
        employee_type_result = employee_type_list[int(counter.get())]
        loan_total_cost_result = loan_total_cost_list[int(counter.get())]
        item_ID_result = item_ID_list[int(counter.get())]
        item_name_result = item_name_list[int(counter.get())]
        item_cost_result = item_cost_list[int(counter.get())]
        number_of_items_result = number_of_items_list[int(counter.get())]
        item_type_result = item_type_list[int(counter.get())]
        date_of_request_result = date_of_request_list[int(counter.get())]
        request_amount_result = request_amount_list[int(counter.get())]

        label_employee_ID_value = Label(MW, text=employee_ID_result)
        label_employee_ID_value.grid(column=1, row=0, sticky=N)

        label_full_name_value = Label(MW, text=full_name_result)
        label_full_name_value.grid(column=1, row=1, sticky=N)

        label_email_value = Label(MW, text=email_result)
        label_email_value.grid(column=1, row=2, sticky=N)

        label_employee_type_value = Label(MW, text=employee_type_result)
        label_employee_type_value.grid(column=1, row=3, sticky=N)

        label_loan_total_cost_value = Label(MW, text=loan_total_cost_result)
        label_loan_total_cost_value.grid(column=1, row=4, sticky=N)

        label_item_ID_value = Label(MW, text=item_ID_result)
        label_item_ID_value.grid(column=1, row=5, sticky=N)

        label_item_name_value = Label(MW, text=item_name_result)
        label_item_name_value.grid(column=1, row=6, sticky=N)

        label_item_cost_value = Label(MW, text=item_cost_result)
        label_item_cost_value.grid(column=1, row=7, sticky=N)

        label_number_of_items_value = Label(MW, text=number_of_items_result)
        label_number_of_items_value.grid(column=1, row=8, sticky=N)

        label_item_type_value = Label(MW, text=item_type_result)
        label_item_type_value.grid(column=1, row=9, sticky=N)

        label_date_of_request_value = Label(MW, text=date_of_request_result)
        label_date_of_request_value.grid(column=1, row=10, sticky=N)

        label_request_amount_value = Label(MW, text=request_amount_result)
        label_request_amount_value.grid(column=1, row=11, sticky=N)

    label_employee_ID = Label(MW, text="Employee_ID:")
    label_full_name = Label(MW, text="Full_name:")
    label_email = Label(MW, text="Email:")
    label_employee_type = Label(MW, text="Employee_type:")
    label_loan_total_cost = Label(MW, text="Loan_total_cost:")
    label_item_ID = Label(MW, text="Item_ID:")
    label_item_name = Label(MW, text="Item_name:")
    label_item_cost = Label(MW, text="Item_cost:")
    label_number_of_items = Label(MW, text="Number_of_items:")
    label_item_type = Label(MW, text="item_type:")
    label_date_of_request = Label(MW, text="date_of_request")
    label_request_amount = Label(MW, text="label_request_amount")

    tkinter.Button(MW, text="Next", command=onClick, fg="dark green", bg="white").grid(column=1, row=12, sticky=N)

    label_employee_ID.grid(column=0, row=0, sticky=N)
    label_full_name.grid(column=0, row=1, sticky=N)
    label_email.grid(column=0, row=2, sticky=N)
    label_employee_type.grid(column=0, row=3, sticky=N)
    label_loan_total_cost.grid(column=0, row=4, sticky=N)
    label_item_ID.grid(column=0, row=5, sticky=N)
    label_item_name.grid(column=0, row=6, sticky=N)
    label_item_cost.grid(column=0, row=7, sticky=N)
    label_number_of_items.grid(column=0, row=8, sticky=N)
    label_item_type.grid(column=0, row=9, sticky=N)
    label_date_of_request.grid(column=0, row=10, sticky=N)
    label_request_amount.grid(column=0, row=11, sticky=N)

    def hit_me():
        tkinter.messagebox.showinfo(title="INFO", message="Approve")
        print("Approve")
        return 1

    b = Button(MW, text='Approve', command=hit_me, fg="dark green", bg="white")
    b.grid(column=2, row=12, sticky=N)

    def logout_function():
        MW.destroy()
        from login_window import login_win
        login_win()

    def view_user_details():
        pass

    MW.mainloop()

manager_win(185908204, 618601763)