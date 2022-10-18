import sqlite3

conn = sqlite3.connect("PIMS")
c = conn.cursor()

c.execute('''CREATE TABLE employee (
            employee_ID integer,
            full_name text,
            email text,
            password text,
            date_of_birth text,
            employee_type text,
            loan_total_cost integer
            )''')

c.execute('''CREATE TABLE item (
                item_ID integer,
                item_name text,
                item_cost integer,
                number_of_items integer,
                date_of_purchase text,
                threshold_value integer,
                description text,
                item_type text
                )''')

c.execute('''CREATE TABLE loaned_item (
            item_ID integer,
            employee_ID integer,
            date_of_request text,
            request_amount integer
            )''')

conn.close()
