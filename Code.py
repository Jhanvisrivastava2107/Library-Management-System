import csv
import os
from datetime import datetime, timedelta
BOOKS_FILE = "books.csv"
MEMBERS_FILE = "members.csv"
LOANS_FILE = "loans.csv"
def ensure_files():
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["book_id", "title", "author", "copies"])
            w.writerow(["1", "Python 101", "John Doe", "3"])
            w.writerow(["2", "Data Structures", "CLRS", "2"])

    if not os.path.exists(MEMBERS_FILE):
        with open(MEMBERS_FILE, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["member_id", "name"])
            w.writerow(["1", "Alice"])
            w.writerow(["2", "Bob"])

    if not os.path.exists(LOANS_FILE):
        with open(LOANS_FILE, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["loan_id", "book_id", "member_id", "due_date", "returned"])
def view_books():
    with open(BOOKS_FILE) as f:
        for row in csv.reader(f):
            print(row)

def add_bookS():
    book_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    copies = input("Copies: ")

    with open(BOOKS_FILE, "a", newline="") as f:
        csv.writer(f).writerow([book_id, title, author, copies])

    print("Book added!")

def search_books():
    term = input("Search term: ").lower()
    with open(BOOKS_FILE) as f:
        for row in csv.reader(f):
            if term in row[1].lower() or term in row[2].lower():
                print(row)


def view_members():
    with open(MEMBERS_FILE) as f:
        for row in csv.reader(f):
            print(row)

def add_member():
    member_id = input("Member ID: ")
    name = input("Name: ")

    with open(MEMBERS_FILE, "a", newline="") as f:
        csv.writer(f).writerow([member_id, name])

    print("Member added!")

def borrow_book():
    book_id = input("Book ID: ")
    member_id = input("Member ID: ")

    due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")

    rows = []
    updated = False

    with open(BOOKS_FILE) as f:
        r = csv.reader(f)
        for row in r:
            if row[0] == book_id and row[0] != "book_id":
                if int(row[3]) > 0:
                    row[3] = str(int(row[3]) - 1)
                    updated = True
            rows.append(row)

    if not updated:
        print("No copies available.")
        return

    with open(BOOKS_FILE, "w", newline="") as f:
        csv.writer(f).writerows(rows)

    # record loan
    loan_id = str(int(datetime.now().timestamp()))

    with open(LOANS_FILE, "a", newline="") as f:
        csv.writer(f).writerow([loan_id, book_id, member_id, due_date, "no"])

    print("Book borrowed! Due date:", due_date)

def return_book():
    loan_id = input("Loan ID: ")
    rows = []
    returned = False
    book_id = None
    
    with open(LOANS_FILE) as f:
        for row in csv.reader(f):
            if row[0] == loan_id and row[0] != "loan_id":
                row[4] = "yes"
                book_id = row[1]
                returned = True
            rows.append(row)

    if not returned:
        print("Invalid loan ID.")
        return

    with open(LOANS_FILE, "w", newline="") as f:
        csv.writer(f).writerows(rows)

    b_rows = []
    with open(BOOKS_FILE) as f:
        for row in csv.reader(f):
            if row[0] == book_id and row[0] != "book_id":
                row[3] = str(int(row[3]) + 1)
            b_rows.append(row)

    with open(BOOKS_FILE, "w", newline="") as f:
        csv.writer(f).writerows(b_rows)

    print("Book returned!")

from datetime import datetime, timedelta

issued_books = {}

book_issue_count = {}
def issue_book(book_id, user):
    issue_date = datetime.now()
    due_date = issue_date + timedelta(days=7)

    issued_books[book_id] = {
        "user": user,
        "issue_date": issue_date,
        "due_date": due_date
    }

    
    if book_id in book_issue_count:
        book_issue_count[book_id] += 1
    else:
        book_issue_count[book_id] = 1

    print(f"Book issued. Due date: {due_date.date()}")
    
def most_issued_books():
    if not book_issue_count:
        print("No books issued yet.")
        return

    sorted_books = sorted(book_issue_count.items(), key=lambda x: x[1], reverse=True)

    print("\nMost Issued Books:")
    for book_id, count in sorted_books:
        print(f"Book ID: {book_id} | Issued: {count} times")

def main():
    ensure_files()

    while True:
        print("\n--- LIBRARY MENU ---")
        print("1. View Books")
        print("2. Add Book")
        print("3. Search Books")
        print("4. View Members")
        print("5. Add Member")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Issued Books")
        print("9. View Most Issued Books")
        print("10. Exit")

        choice = input("Choice: ")

        if choice == "1": view_books()
        elif choice == "2": add_bookS()
        elif choice == "3": search_books()
        elif choice == "4": view_members()
        elif choice == "5": add_member()
        elif choice == "6": borrow_book()
        elif choice == "7": return_book()
        elif choice == "8": issue_book()
        elif choice == "9": most_issued_books()
        elif choice == "10":
            print("Bye.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
