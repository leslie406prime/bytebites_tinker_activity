# ByteBites Spec

## Client Feature Request

We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the name, price, category, and popularity rating for every item we sell.

We also need a way to manage the full collection of items — a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost.

## Candidate Classes

- **Customer** — a registered user of the app; tracked by name and past purchase history so the system can tell real, returning users apart from anonymous ones.
- **MenuItem** — a single sellable food/drink item; tracked by name, price, category, and popularity rating.
- **Menu** — the full collection of `MenuItem`s the app offers; supports filtering the collection by category (e.g. "Drinks", "Desserts").
- **Transaction** — one order a customer places; holds the `MenuItem`s they selected and computes the total cost.
