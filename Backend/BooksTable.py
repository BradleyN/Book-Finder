import sqlite3

class BooksTable:
    def __init__(self):
        # Initialize connection to the database file
        self.db_path = 'Backend/Books_Database/BooksDatabase.db'
        self.conn = sqlite3.connect(self.db_path,check_same_thread=False)
        self.conn.row_factory = sqlite3.Row  # This allows column access by name

    def fetch_all(self):
        #Fetch all rows from the books table and return them as a list of dictionaries.
        with self.conn:
            cursor = self.conn.cursor()

            cursor.execute("SELECT * FROM BOOKS LIMIT 100")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    #Pass col_names as a tuple
    def fetch_first_cols(self):
        with self.conn:
            cursor = self.conn.cursor()
            try:
                cursor.execute("SELECT Title, Authors FROM BOOKS LIMIT 100")
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
            except Exception as e:
                print(f"Failed to read column name, {e}")
                return None
        