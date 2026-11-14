import csv
from pathlib import Path

class item:
    def __init__(self, name, price, quantity, has_numpad=False):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.has_numpad = has_numpad

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    @classmethod
    def instantiate_from_csv(cls):
        csv_path = Path(__file__).with_name('items.csv')
        with csv_path.open('r', newline='', encoding='utf-8') as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item_data in items:
            cls(
                name=item_data['name'],
                price=float(item_data['price']),
                quantity=int(item_data['quantity']),
                has_numpad=bool(item_data.get('has_numpad'))
            )

