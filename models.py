# ByteBites core models
#
# Customer    - a registered user; tracks name and past purchase history.
# MenuItem    - a single sellable item; tracks name, price, category, popularity rating.
# Menu        - the full collection of MenuItems; supports filtering/sorting.
# Transaction - one order; holds selected MenuItems and computes the total cost.


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []


class MenuItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items = []


class Transaction:
    def __init__(self):
        self.selected_items = []
