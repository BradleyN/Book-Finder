import sqlite3

#A list of valid tables to read from
TABLE_NAMES = {"BOOKS", "BOOK_INFO", "READING_GOALS", "WISHLIST", "YEARS"}

class BooksTable:
    def __init__(self):
        # Initialize connection to the database file
        self.db_path = 'Backend/Books_Database/BooksDatabase.db'
        self.conn = sqlite3.connect(self.db_path,check_same_thread=False)
        self.conn.row_factory = sqlite3.Row  # This allows column access by name

    def fetch_books(self,id_filter=None,name_filter=None,limit=None):
        #Fetch all rows from the a table and return them as a list of dictionaries.
        parameters = []

        print(id_filter)

        with self.conn:
            cursor = self.conn.cursor()
            
            #use WHERE 1=1 to use up the first WHERE statement. This allows dynamically building queries
            query = "SELECT * FROM BOOKS WHERE 1=1 "

            if id_filter is not None:
                query += "AND book_id = ? "
                parameters.append(id_filter)
            
            if name_filter is not None:
                query += "AND \"Title\" = ? "    
                parameters.append(name_filter)            

            if limit is not None:
                query += "LIMIT " + str(limit)

            print(query)
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

            print(query,parameters)
            cursor.execute(query,parameters)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
    
    
    def modify_review(self,book_id,review_score,review_text):
        #STEP 1: IMPLEMENT BOOK REVIEW
        pass

    def fetch_books_with_year(self,year_filter=None,limit = None):
         parameters = []

         with self.conn:
            cursor = self.conn.cursor()
            
            query = "SELECT id FROM YEARS "

            if year_filter is not None:
                query +=  "WHERE \"year\" = ? "
                parameters.append(year_filter)

            if limit is not None:
                query += "LIMIT " + str(limit)

            print(query)

            cursor.execute(query,parameters)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]


    #Pass col_names as a tuple
    #TODO: REFACTOR!!!
    def fetch_cols(self,cols_list,table,limit=None):
        with self.conn:
            cursor = self.conn.cursor()
            query = "SELECT "

            #add cols to table query
            for i in range(len(cols_list)):
                if i != len(cols_list)-1:
                    query += cols_list[i] + ", "
                else:
                    query += cols_list[i] + " "

            #specify table to get data from
            query += "FROM " + table + " "

            #apply limit if provided
            if limit is not None:
                query += "LIMIT " + str(limit)

            print(query)
            try:
            
                cursor.execute("SELECT Title, Authors FROM BOOKS LIMIT 100")
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
            except Exception as e:
                print(f"Failed to read column name, {e}")
                return None

    def add_review(self, book_id, review_score, review_text):
        with self.conn:
            cursor = self.conn.cursor()
            query = "INSERT INTO REVIEWS(book_id, score, text) VALUES (?, ?, ?);"
            parameters = [book_id, review_score, review_text]
            cursor.execute(query, parameters)

    def edit_review(self, book_id, review_score, review_text):
        with self.conn:
            cursor = self.conn.cursor()
            query = "UPDATE REVIEWS SET score = ?, text = ? WHERE book_id = ?;"
            parameters = [review_score, review_text, book_id]
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

            print(query,parameters)
            cursor.execute(query,parameters)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]