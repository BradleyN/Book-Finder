from Backend.BooksTable import BooksTable
def get_cols_data():
    return BooksTable().fetch_first_cols()