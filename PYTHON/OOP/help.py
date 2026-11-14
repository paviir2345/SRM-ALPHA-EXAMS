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

"""the static method is used to check if a number is an integer or not. 
It takes a number as input and returns True if the number is an integer, 
and False otherwise. The method first checks if the input is a float, and if so, 
it uses the is_integer() method to check if it is an integer. If the input is an int,
 it returns True. If the input is neither a float nor an int, it returns False.
The class method is used to instantiate objects of the item class from a CSV file.
 It reads the CSV file using the csv module and creates a list of dictionaries 
 representing each row in the file. It then iterates over the list of dictionaries
   and creates an instance of the item class for each row, passing in the values 
   from the dictionary as arguments to the constructor. The method uses the Path module to get the path to the CSV file relative to the current file."""