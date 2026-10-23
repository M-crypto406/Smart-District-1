from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def details(self):
        pass

    def __str__(self):
        return self.details()


class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def details(self):
        return f"{self.title} by {self.author}"


class ReferenceBook(Book):
    def __init__(self, title, author, section):
        super().__init__(title, author)
        self.section = section

    def details(self):
        return f"{super().details()}, Section: {self.section}"


class BorrowingRules:
    def days_allowed(self):
        return 14


class StudentMember(BorrowingRules):
    def days_allowed(self):
        return 7


book = Book("Python Basics", "John")
reference = ReferenceBook("Science", "Sara", "A")

for item in [book, reference]:
    print(item)

student = StudentMember()
print("Student borrowing days:", student.days_allowed())