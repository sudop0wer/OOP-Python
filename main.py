class Book:

    all = []

    def __init__(self, title: str, author: str, isbn: int):

        assert title, f"Please insert title"
        assert isbn > 0, f"ISBN {isbn} is not valid"

        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        Book.all.append(self)

    def __repr__(self):
        return f"Book '{self.title}' by {self.author} with ISBN {self.isbn}, available to borrow: {self.available}"

    def is_available(self):
        return self.available

class Member:

    all = []

    def __init__(self, name: str, member_id: int, borrowed_books: list, bb_count=0):

        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books
        self.bb_count = bb_count
        Member.all.append(self)

    def borrow_book(self, book):
        if book.is_available():
            self.borrowed_books.append(f"{book.title} by {book.author}")
            self.bb_count = self.bb_count + 1
            book.available = False
        else:
            print(f"Book {book.title} is not available to borrow")

    def __repr__(self):
        return f"Member {self.name} with ID {self.member_id} borrowed {self.bb_count} books"


book1 = Book("Haidi", "John Smith", 300987)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 987654321)
member1 = Member("David", 1, [])
member2 = Member("Alex", 2,[])

member1.borrow_book(book1)
print(member1.borrowed_books)
member2.borrow_book(book1)
