import csv
from pathlib import Path


class Item:
    pay_rate = 0.8
    all = []

    def __init__(
        self,
        name: str,
        price: float,
        quantity: int = 0,
        has_numpad: bool = True,
    ):
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        assert isinstance(has_numpad, bool), (
            f"has_numpad {has_numpad} is not a boolean"
        )
        self.name = name
        self.price = price
        self.quantity = quantity
        self.has_numpad = has_numpad
        Item.all.append(self)

    def total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        csv_path = Path(__file__).with_name("items.csv")
        with csv_path.open("r", newline="", encoding="utf-8") as file:
            for item in csv.DictReader(file):
                cls(
                    name=item["name"],
                    price=float(item["price"]),
                    quantity=int(item["quantity"]),
                    has_numpad=item.get("has_numpad", "").strip().lower() == "true",
                )

    @staticmethod
    def is_integer(number):
        return isinstance(number, int) or (
            isinstance(number, float) and number.is_integer()
        )
