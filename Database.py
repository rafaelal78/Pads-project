import sqlite3

conn = sqlite3.connect("PIMS")
c = conn.cursor()

c.execute('''CREATE TABLE item (
                Item_name text,
                Item_cost integer,
                Number_of_items integer,
                Date_of_purchase text,
                Threshold_value integer,
                Description text,
                Item_type text
                )''')

c.execute('''CREATE TABLE employee(
            Employee_ID integer,
            Full_name text,
            Username text,
            Password text,
            Email text,
            Items_loaned integer,
            employee_type text
            )''')

conn.close()