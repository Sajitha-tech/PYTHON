class Publisher:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        return f"Publisher: {self.name}"

# Derived class
class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)  # Call the constructor of Publisher
        self.title = title
        self.author = author

    def display_info(self):
        # Override the display_info method to include book details
        publisher_info = super().display_info()
        return f"{publisher_info}\nTitle: {self.title}\nAuthor: {self.author}"

# Further derived class
class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)  # Call the constructor of Book
        self.price = price
        self.no_of_pages = no_of_pages

    def display_info(self):
        # Override the display_info method to include Python book details
        book_info = super().display_info()
        return f"{book_info}\nPrice: {self.price}\nNumber of Pages: {self.no_of_pages}"

# Create an instance of the Python class
python_book = Python("O'Reilly Media", "Learning Python", "Mark Lutz", 39.99, 1648)

# Display information about the Python book
print(python_book.display_info())