# Python OOP library manager

A Python program that uses OOP to manage a database of books and members.

## Project Description

The main purpose of this project was practicing an implementing OOP concepts in a real-life scenario usecase. The project is not complete and does not aim to give an absolute solution for the scenario, only configurations relevant to OOP being implemented.
The scenario of this project is the following:

### Challenge: Library Management System
You are tasked with designing a Library Management System using Object-Oriented Programming (OOP) concepts. The system should be able to manage books, members, and lending operations. Your task is to implement the following classes and methods:

Requirements:

Class: Book

Attributes:
- title (string)
- author (string)
- isbn (string)
- available (boolean, default is True)

Methods:
- __init__(self, title, author, isbn) : Initialize a book object with the given details.
- __repr__(self): Return the book details in a string format.
- is_available(self): Return whether the book is available or not.

Class: Member

Attributes:
- name (string)
- member_id (string)
- borrowed_books (list, to store borrowed books)

Methods:
- __init__(self, name, member_id): Initialize a member object.
- borrow_book(self, book): Add a book to the member's borrowed_books list and mark it as unavailable.
- __repr__(self): Return the member details and borrowed books.

The code acompplishes all this requirments, and I have lef 3 print statements at the end with which you can test the borrowing system: how the list of borrowed books increases for the member, and the book becomes unavailable to borrow.
