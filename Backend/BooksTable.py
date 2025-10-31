import sqlite3

class BooksTable:
    def __init__(self):
        # Initialize connection to the database file
        self.db_path = 'test.db'

    def fetch_all(self):
        #Fetch all rows from the books table and return them as a list of dictionaries.
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # This allows column access by name
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()

        # Convert rows to list of dictionaries
        books = [dict(row) for row in rows]

        conn.close()
        return books

    def to_dict(self):
        #Return the entire table as a single dictionary keyed by title.
        books_list = self.fetch_all()
        books_dict = {book["Title"]: book for book in books_list}
        return books_dict

Books = BooksTable()
Books.fetch_all()
