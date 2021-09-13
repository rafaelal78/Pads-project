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

c.execute('''CREATE TABLE employee (
            employee_ID integer,
            full_name text,
            email text,
            password text,
            date_of_birth text,
            employee_type text,
            loan_total_cost integer
            )''')

conn.close()
