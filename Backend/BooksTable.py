import sqlite3
from Backend.Logger import main_logger

#A list of valid tables to read from
TABLE_NAMES = {"BOOKS", "BOOK_INFO", "READING_GOALS", "WISHLIST", "YEARS", "BOOK_CATEGORIES"}

class BooksTable:
    def __init__(self):
        # Initialize connection to the database file
        self.db_path = 'Backend/Books_Database/BooksDatabase.db'
        self.conn = sqlite3.connect(self.db_path,check_same_thread=False)
        self.conn.row_factory = sqlite3.Row  # This allows column access by name

    def fetch_books(self,id_filter=None,name_filter=None,limit=None):
        #Fetch all rows from the a table and return them as a list of dictionaries.
        parameters = []

        with self.conn:
            cursor = self.conn.cursor()
            
            #use WHERE 1=1 to use up the first WHERE statement. This allows dynamically building queries
            query = "SELECT * FROM BOOKS WHERE 1=1 "

            if id_filter is not None:
                query += "AND book_id = ? "
                parameters.append(id_filter)
            
            if name_filter is not None:
                query += "AND \"Title\" LIKE ? "    
                parameters.append("%" + name_filter + "%")            

            if limit is not None:
                query += "LIMIT " + str(limit)

            main_logger.Log(f"{query},{parameters}")
            cursor.execute(query,parameters)
            rows = cursor.fetchall()

            return [dict(row) for row in rows]
    
    #Fetch rows from BOOK_INFO table based on the given filters.
    def fetch_book_info(self,id_filter=None,year_filter=None,genre_filter=None,limit=None):
        parameters = []

        with self.conn:
            cursor = self.conn.cursor()
            
            query = "SELECT * FROM BOOK_INFO WHERE 1=1 "

            if id_filter is not None:
                query += "AND book_id = ? "
                parameters.append(id_filter)

            if genre_filter is not None:
                query += "AND \"Category\" = ? "
                parameters.append(genre_filter)

            if year_filter is not None:
                query += "AND \"Publish Date (Year)\" = ? "
                parameters.append(year_filter)

            if limit is not None:
                query += "LIMIT " + str(limit)

            main_logger.Log(f"{query},{parameters}")

            cursor.execute(query,parameters)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def fetch_book_category(self, category=None, limit=None):
        parameters = []
        
        with self.conn:
            cursor = self.conn.cursor()

            query = "SELECT book_id FROM BOOK_CATEGORIES "

            if category is not None:
                query += "WHERE category = ? "
                parameters.append(category)
                
            if limit is not None:
                query += "LIMIT " + str(limit)

            main_logger.Log(f"{query},{parameters}")
            cursor.execute(query,parameters)
            rows = cursor.fetchall()
            print(rows)
            return [dict(row)["book_id"] for row in rows]

    def fetch_books_with_year(self,year_filter=None,limit = None):
         parameters = []

         with self.conn:
            cursor = self.conn.cursor()
            
            query = "SELECT book_id FROM YEARS "

            if year_filter is not None:
                query +=  "WHERE \"year\" = ? "
                parameters.append(year_filter)

            if limit is not None:
                query += "LIMIT " + str(limit)

            main_logger.Log(f"{query},{parameters}")

            cursor.execute(query,parameters)
            rows = cursor.fetchall()
            return [dict(row)["book_id"] for row in rows]

    def add_review(self, book_id, review_score, review_text):
        with self.conn:
            cursor = self.conn.cursor()
            query = "INSERT INTO REVIEWS(book_id, score, text) VALUES (?, ?, ?);"
            parameters = [book_id, review_score, review_text]
            main_logger.Log(f"{query},{parameters}")
            cursor.execute(query, parameters)

    def edit_review(self, book_id, review_score, review_text):
        with self.conn:
            cursor = self.conn.cursor()
            query = "UPDATE REVIEWS SET score = ?, text = ? WHERE book_id = ?;"
            parameters = [review_score, review_text, book_id]
            main_logger.Log(f"{query},{parameters}")
            cursor.execute(query, parameters)

    def fetch_review_info(self, id_filter=None, limit=None):
        parameters = []

        with self.conn:
            cursor = self.conn.cursor()
            
            query = "SELECT * FROM REVIEWS WHERE 1=1 "

            if id_filter is not None:
                query += "AND book_id = ? "
                parameters.append(id_filter)
                
            if limit is not None:
                query += "LIMIT " + str(limit)

            main_logger.Log(f"{query},{parameters}")
            cursor.execute(query,parameters)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
