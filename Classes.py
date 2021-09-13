class item:
    def __init__(self, item_name, item_cost, number_of_items, DoP,threshold_value, description):
        self.name = item_name
        self.cost = item_cost
        self.number = number_of_items
        self.DoP = DoP  # Date of Purchase
        self.TV = threshold_value
        self.DP = description

class stationary(item):
    def __init__(self, item_name, item_cost, number_of_items, DoP, threshold_value, description):
        super().__init__(item_name, item_cost, number_of_items, DoP, threshold_value, description)
        self.IT = "stationary"

class electronic(item):
    def __init__(self, item_name, item_cost, number_of_items, DoP, threshold_value, description):
        super().__init__(item_name, item_cost, number_of_items, DoP, threshold_value, description)
        self.IT = "electronic"

class employee:
    def __init__(self, ID, name, email, password, date_of_birth, employee_type):
        self.ID = ID
        self.name = name
        self.email = email
        self.password = password
        self.DoB = date_of_birth
        self.ET = employee_type
        self.loan_total_cost = 0        
        
class PIMS:
    def __init__(self):
        self.items_list = []

    def add_stationary(self, IN, IC, NoI, DoP, THV, D):
        stationary_item = stationary(IN, IC, NoI, DoP, THV, D)
        self.item_list += stationary_item

    def add_electronic(self):
        electronic_item = electronic(IN, IC, NoI, DoP, THV, D)
        self.item_list += electronic_item

    def delete(self):
        pass

#     def modify(self):
#         pass

