class Category:
    categories = []
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        Category.categories.append(self.name)
    
    def __str__(self):
        my_string = ""
        my_string = self.name.center(30, "*")
        if self.ledger != []:
            for x in self.ledger:
                big_desc = x['description'][:23]
                big_amount = str("{:.2f}".format(x['amount']))[:7]
                x = "{0:<23}{1:>7}".format(big_desc, big_amount)
                my_string = f"{my_string}\n{x}"
        balance = sum(entries['amount'] for entries in self.ledger)
        return f"{my_string}\nTotal: {round(balance, 2)}"


    def deposit(self, amount, description = ""):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount": self.amount, "description": self.description})
    
    def withdraw(self, amount, description = ""):
        self.amount = amount
        if self.check_funds(self.amount):
            self.amount = -amount
            self.description = description
            self.ledger.append({"amount": self.amount, "description": self.description})
            return True
        return False

    def get_balance(self):
        balance = sum(entries['amount'] for entries in self.ledger)
        return round(balance, 2)
    
    def transfer(self, amount, budget_category):
        self.amount = amount
        if self.check_funds(self.amount):
            self.budget_category = budget_category
            self.description = f"Transfer to {self.budget_category.name}"
            
            self.withdraw(self.amount, self.description)
            self.budget_category.deposit(abs(self.amount), f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        self.amount = amount
        balance = sum(entries['amount'] for entries in self.ledger)
        if self.amount <= balance:
            return True
        return False

def create_spend_chart(list_categories):
    my_dictionary = {}
    for category in list_categories:
        my_sum = 0
        for x in category.ledger:
            if x["amount"] < 0:
                my_sum += x["amount"]
        my_dictionary[category.name] = my_sum

    total_spent = sum(my_dictionary.values())
    for key, value in my_dictionary.items():
        how_many_o = (value / total_spent * 100) // 10
        my_dictionary[key] = how_many_o
    
    lst = list(my_dictionary.values())
    lst2 = list(my_dictionary.keys())
    length = len(lst)
    my_string = "Percentage spent by category"
    for i in range(10, -1, -1):
        zero = []
        for x in lst:
            if x >= i:
                zero.append(" o ")
            else:
                zero.append("   ")
        line = "".join(zero)
        if i * 10 == 100:
            my_string = f"{my_string}\n{i * 10}|{line} "
        elif i * 10 == 0:
            my_string = f"{my_string}\n  {i * 10}|{line} "
        else:
            my_string = f"{my_string}\n {i * 10}|{line} "
    dashes = "-"*(1 + length * 3)
    my_string = f"{my_string}\n    {dashes}"
    for i, x in enumerate(lst2):
        lst2[i] = x.capitalize()

    for i in range(20):
        temp_string = "    "
        for x in lst2:
            length = len(x)
            if i < length:
                temp_string = f"{temp_string} {x[i]} "
            else:
                temp_string = f"{temp_string}   "
        if temp_string.strip() == "":
            break
        my_string = f"{my_string}\n{temp_string} "
        

    return my_string

# TEST CASES
# Food = Category("Food")
# Stationary = Category("Stationary")

# print(Food.get_balance())
# print(Food.deposit(4.83, "First deposit"))
# print(Food.get_balance())
# print(Food.withdraw(2.01, "First withdrawal"))
# print(Food.get_balance())
# print(Food.ledger)
# print(Food.transfer(2.00, Stationary))
# print(Food.get_balance())
# print(Food.ledger)
# print(Stationary.get_balance())
# print(Stationary.ledger)
# print(Stationary.deposit(4923.94, "Large deposit"))
# print(Stationary.withdraw(10.00, "withdraw"))
# print(Category.categories)
# print(Food)
# print(Stationary)
# print(Food.check_funds(0.83))
# print(Food.check_funds(0.30))

# print(create_spend_chart([Food, Stationary]))

