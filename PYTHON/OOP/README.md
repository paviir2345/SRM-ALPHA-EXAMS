# Object-Oriented Programming

Examples of Python classes and common object-oriented patterns.

## Concepts

- `Item` stores product state and validates constructor inputs.
- Class attributes (`pay_rate`, `all`) are shared by instances.
- `total_price` and `apply_discount` are instance methods.
- `instantiate_from_csv` is a `classmethod` that loads [`items.csv`](./items.csv).
- `is_integer` is a `staticmethod` because it does not need instance or class state.
- `Phone` inherits from `Item` and adds phone-specific data and behavior.
- `__repr__` provides a useful representation when objects are printed.

## Files

- [`Item.py`](./Item.py): base `Item` class and CSV loading.
- [`phone.py`](./phone.py): `Phone(Item)` inheritance example.
- [`main.py`](./main.py): creates and prints phone objects.
- [`help.py`](./help.py): additional class/introspection notes.

## Run

```powershell
python .\oop\main.py
python .\oop\Item.py
```

`Item.py` reads the CSV path relative to its own file, so it can be run from
any working directory.
