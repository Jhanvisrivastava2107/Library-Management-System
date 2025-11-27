##Library-Management-System
Library Management System is a beginner-friendly Python project that helps manage books, members, and borrowing operations using simple CSV-based datasets. It runs entirely in the terminal and requires no external database, making it easy to set up and understand.It provides a simple, menu-driven system for managing book inventory, member registration, and the process of borrowing and returning books. The system ensures data persistence by storing all records in structured CSV files.

##Features 
The LMS includes the following core functionalities:
-Book Management:
  View the complete list of books and available copies.
  Add new book records (ID, Title, Author, Copies).
  Search books by title or author.

-Member Management:
  View the list of all registered members.
  Add new member records (ID, Name).

-Loan Management:
  Borrow Book: Records a transaction, calculates a 14-day due date, and decrements the book's copy count.
  Return Book: Updates the loan record and increments the book's copy count back into inventory.

##Technologies/Tools Used 
Primary Language: Python 3.x
Data Storage: CSV (Comma Separated Values) files (books.csv, members.csv, loans.csv)
Standard Python Modules: csv, os, datetime, timedelta

##Steps to Install and Run the program
1. Clone the repository or download the file
2. Ensure python is installed.
3. Run the program
4. Initial Setup: Upon the first run, the script will automatically check for the presence of books.csv, members.csv, and loans.csv. If these files do not exist, it will create them with initial sample data.

##Insturctions for testing
1.Start the Program: Run python library_management.py.
2.Test Book Addition:
  Select 2. Add Book.
  Enter details for a new book.
  Select 1. View Books to confirm the entry.
3.Test Borrowing Logic (Inventory Check):
  Note the book_id and available copies for a book (e.g., Book ID 1 has 3 copies).
  Select 6. Borrow Book. Enter valid book_id and member_id.
  Select 1. View Books to verify the copies count has been decremented by 1.
4.Test Return Logic (Loan Update):
  Select 7. Return Book. Enter the loan_id recorded during the borrow step.
  Select 1. View Books to verify the copies count has been incremented back to the original number.
5.Test Error Handling:
  Attempt to borrow a book when its copies count is 0. The system should output "No copies available."
  Attempt to return a book using a non-existent loan_id. The system should output "Invalid loan ID."

##Screenshots
<img width="777" height="731" alt="Addition of books" src="https://github.com/user-attachments/assets/48e6d2b5-1453-4ea0-a6b9-b8964ca1904b" />
<img width="543" height="907" alt="More functionalities" src="https://github.com/user-attachments/assets/d2ae440e-db72-4d5e-b1f5-5bce7a1428b5" />
