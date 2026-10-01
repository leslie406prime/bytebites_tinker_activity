from models import Customer, MenuItem, Menu, Transaction


def test_calculate_total_with_multiple_items():
    transaction = Transaction()
    transaction.add_item(MenuItem("Spicy Burger", 10.0, "Food", 4.0))
    transaction.add_item(MenuItem("Large Soda", 5.0, "Drinks", 3.5))

    assert transaction.calculate_total() == 15.0


def test_order_total_is_zero_when_empty():
    transaction = Transaction()

    assert transaction.calculate_total() == 0


def test_filter_menu_items_by_category():
    menu = Menu()
    menu.add_item(MenuItem("Large Soda", 2.5, "Drinks", 3.8))
    menu.add_item(MenuItem("Iced Tea", 2.0, "Drinks", 4.9))
    menu.add_item(MenuItem("Spicy Burger", 8.5, "Food", 4.2))

    drinks = menu.filter_by_category("Drinks")

    assert len(drinks) == 2
    assert all(item.category == "Drinks" for item in drinks)


def test_sort_by_popularity():
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 8.5, "Food", 4.2))
    menu.add_item(MenuItem("Large Soda", 2.5, "Drinks", 3.8))
    menu.add_item(MenuItem("Iced Tea", 2.0, "Drinks", 4.9))

    ranked = menu.sort_by_popularity()

    assert [item.name for item in ranked] == ["Iced Tea", "Spicy Burger", "Large Soda"]


def test_customer_purchase_history_updates():
    customer = Customer("Alice")
    transaction = Transaction()
    transaction.add_item(MenuItem("Spicy Burger", 8.5, "Food", 4.2))

    customer.add_purchase(transaction)

    assert len(customer.purchase_history) == 1
    assert customer.purchase_history[0] is transaction
