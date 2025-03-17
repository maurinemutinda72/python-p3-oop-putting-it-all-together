class Shoe:
    def __init__(self, brand, size):
        """Initialize a Shoe with brand and size."""
        self.brand = brand
        if not isinstance(size, int):
            print("size must be an integer")
            self._size = 0  # Default value or handle as needed
        else:
            self._size = size
        self.condition = "New"  # Default condition

    def get_size(self):
        return self._size

    def set_size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    size = property(get_size, set_size)

    def cobble(self):
        """Repair the shoe and set condition to New."""
        self.condition = "New"
        print("Your shoe is as good as new!")