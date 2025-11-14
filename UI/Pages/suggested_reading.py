from PySide6.QtWidgets import QWidget, QHBoxLayout
from Backend.BooksTable import Books
from UI.Widgets.book_table import Book_Table

class Popular_Items(QWidget):
    def __init__(self):
        super().__init__()

        self.books = Books
        self.popular_book_list = [{"book_id": 1, "Title": "Lord of the rings"}]
        self.popular_author_list = [{"Author:", "J.R.R Tolkien"}]

        #get labels from data
        labels = []
        for label, _ in self.popular_book_list[0].items():
            labels.append(label)
        labels.append("Options")
        self.popular_book_table = Book_Table(labels)
        self.popular_book_table.fill_table(self.popular_book_list)

        labels = []
        for label, _ in self.popular_book_list[0].items():
            labels.append(label)
        labels.append("Options")
        self.popular_author_table = Book_Table(labels)
        self.popular_author_table.fill_table(self.popular_author_list)

        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.popular_book_table)
        self.horizontal_layout.addWidget(self.popular_author_table)
        
#Needs to be implemented on the db API
def fetch_popular_books(self):
    pass

#Needs to be implemented on the db API
def fetch_popular_authors(self):
    pass
    