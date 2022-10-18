class item:
    def __init__(self, item_ID, item_name, item_cost, number_of_items, DoP, threshold_value,
                 description, item_type):
        self.ID = item_ID
        self.name = item_name
        self.cost = item_cost
        self.number = number_of_items
        self.DoP = DoP  # Date of Purchase
        self.TV = threshold_value
        self.DP = description
        self.IT = item_type

class loaned_item:
    def __init__(self, item_ID, employee_ID, date_of_request, request_amount):
        self.IID = item_ID
        self.EID = employee_ID
        self.DoR = date_of_request
        self.RA = request_amount

# this would've been done in inheritance but sqlite lib wouldn't allow it

class employee:
    def __init__(self, ID, name, email, password, date_of_birth, employee_type):
        self.ID = ID
        self.name = name
        self.email = email
        self.password = password
        self.DoB = date_of_birth
        self.ET = employee_type
        self.loan_total_cost = 0
