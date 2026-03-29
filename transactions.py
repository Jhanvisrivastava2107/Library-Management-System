from datetime import datetime, timedelta

issued_books = {}

def issue_book(book_id, user):
    issue_date = datetime.now()
    due_date = issue_date + timedelta(days=7)

    issued_books[book_id] = {
        "user": user,
        "issue_date": issue_date,
        "due_date": due_date
    }

    print(f"Book issued successfully. Due date: {due_date.date()}")
def return_book(book_id):
    if book_id not in issued_books:
        print("Book not issued.")
        return

    record = issued_books[book_id]
    due_date = record["due_date"]
    return_date = datetime.now()

    delay = (return_date - due_date).days

    if delay > 0:
        fine = delay * 5
        print(f"Book returned late. Fine: ₹{fine}")
    else:
        print("Book returned on time. No fine.")

    del issued_books[book_id]
issue_date.strftime("%Y-%m-%d")
datetime.strptime(date_string, "%Y-%m-%d")
