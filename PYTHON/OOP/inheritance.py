try:
    from Item import Item
    from phone import Phone
except ModuleNotFoundError:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from Item import Item
    from phone import Phone


if __name__ == "__main__":
    phone1 = Phone("iPhone 17", 999.99, 10, 1)
    phone2 = Phone("Samsung Galaxy S30", 899.99, 5, 1)
    print(phone1.calculate_total_price())
    print(phone2.calculate_total_price())
    print(Phone.all)
