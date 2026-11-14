from oop.Item import Item


class Phone(Item):
    def __init__(
        self,
        name: str,
        price: float,
        quantity: int = 0,
        broken_phones: int = 0,
    ):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, (
            f"Broken phones {broken_phones} is not greater than or equal to zero"
        )
        self.broken_phones = broken_phones

    def calculate_total_price(self):
        return self.total_price()


if __name__ == "__main__":
    phone1 = Phone("iPhone 17", 999.99, 10, 1)
    phone2 = Phone("Samsung Galaxy S30", 899.99, 5, 1)
    print(phone1.calculate_total_price())
    print(phone2.calculate_total_price())
    print(Phone.all)
