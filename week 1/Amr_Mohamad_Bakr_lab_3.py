class LibraryItem:
    def __init__(self, title, subj):
        self.title = title
        self.subj = subj
        self.is_borrowed = None

    def borrow(self):
        if not self.is_borrowed:
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_item(self):
        if self.is_borrowed:
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Title: {self.title}, Status: {status}"

#=======================================================================================

class Book(LibraryItem):
    def __init__(self, title, author, subj):
        super().__init__(title ,subj)
        self.author = author

    def __str__(self):
        return f"Book - Title: {self.title}, Author: {self.author}, Subject: {self.subj}, Status: {'Borrowed' if self.is_borrowed else 'Available'}"

#========================================================================================

class Magazine(LibraryItem):
    def __init__(self, title, issue_number, subj):
        super().__init__(title ,subj)
        self.issue_number = issue_number

    def __str__(self):
        return f"Magazine - Title: {self.title}, Issue: {self.issue_number}, subject: {self.subj}, Status: {'Borrowed' if self.is_borrowed else 'Available'}"

#=========================================================================================

class Novels(LibraryItem):
    def __init__(self,title, num_page, subj):
        super().__init__(title, subj)
        self.num_page = num_page

    def __str__(self):
        return f"Novels - Title: {self.title}, num of pages: {self.num_page}, subject: {self.subj}, Status: {'Borrowed' if self.is_borrowed else 'Available'}"

#=========================================================================================

class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"'{item.title}' has been added to the library.")

    def borrow_item(self, title):
        for item in self.items:
            if item.title == title:
                item.borrow()
                return
        print(f"Item with title '{title}' not found in the library.")

    def return_item(self, title):
        for item in self.items:
            if item.title == title:
                item.return_item()
                return
        print(f"Item with title '{title}' not found in the library.")

    def list_items(self):
        if not self.items:
            print("The library has no items.")
        else:
            for item in self.items:
                print(item)


# Example Usage:
library = Library()

# Adding books and magazines
book1 = Book("1984", "George Orwell", "science")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "philosophy")
magazine1 = Magazine("National Geographic", "2023-08", "history")
novel1= Novels("The beauty and best", "90", "imagination")

library.add_item(book1)
library.add_item(book2)
library.add_item(magazine1)
library.add_item(novel1)
print("=" *50)
# Listing all items
library.list_items()

print("=" *50)
# Borrowing and returning items
library.borrow_item("1984")
library.borrow_item("National Geographic")
print("=" *50)

# Listing all items again to see updated statuses
library.list_items()
