class Book:
    def __init__(self, title, page_count):
        """Initialize a Book with title and page_count."""
        self.title = title
        if not isinstance(page_count, int):
            print("page_count must be an integer")
            self._page_count = 0  # Default value or handle as needed
        else:
            self._page_count = page_count

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        """Simulate turning a page."""
        print("Flipping the page...wow, you read fast!")