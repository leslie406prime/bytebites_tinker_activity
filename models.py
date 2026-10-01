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

    def add_purchase(self, transaction):
        self.purchase_history.append(transaction)


class MenuItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def filter_by_category(self, category):
        return [item for item in self.items if item.category == category]

    def sort_by_popularity(self, descending=True):
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=descending)


class Transaction:
    def __init__(self):
        self.selected_items = []

    def add_item(self, item):
        self.selected_items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.selected_items)
