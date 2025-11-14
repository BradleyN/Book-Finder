from __future__ import annotations

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QFormLayout, QVBoxLayout, QWidget, QLabel, QHBoxLayout
)

from UI.Widgets.book_table import Book_Table
from UI.Widgets.input import LineInput, Button
from UI.Widgets.BookInfo import BookInfo
from Backend.BooksTable import Books

#This class is responsible for creating the UI for the search tab of the application
class SearchPage(QWidget):
    def __init__(self):
        super().__init__()

        self.books = Books
        self.book_list = self.books

        #get labels from data
        """labels = []
        for label, _ in self.book_list[0].items():
            labels.append(label)
        labels.append("Options")
        self.table = Book_Table(labels)"""

        #Technical debt. Fix later maybe?
        self.book_info = BookInfo()
        labels = ["Title", "Authors","Options"]
        self.table = Book_Table(labels,self.book_info)
        self.bottom = QHBoxLayout()
        self.bottom.addWidget(self.table)
        self.bottom.addWidget(self.book_info)
        
        self.book_list = self.books.fetch_first_cols()
        self.table.fill_table(self.book_list)

        self.createSearchBar()
        self.createFilterForm()
        self.buildLayout()
        self.setLayout(self.page_layout)

        self.search_input.returnPressed.connect(self.search_books)
        self.filter_button.clicked.connect(self.filter_books)
        

    def createSearchBar(self):
        self.search_input = LineInput()
        self.search_form = QFormLayout()
        self.search_form.addRow("Search:", self.search_input)

    def createFilterForm(self):
        self.options_label = QLabel("Filters")
        self.options_label.setAlignment(Qt.AlignCenter)
        self.genre_input = LineInput()
        self.year_input = LineInput()
        self.filter_form = QFormLayout()
        self.filter_form.addRow("Genre: ", self.genre_input)
        self.filter_form.addRow("Year: ", self.year_input)
        self.filter_button = Button("Filter")

    def buildLayout(self):
        self.page_layout = QVBoxLayout()
        self.page_layout.addWidget(self.options_label)
        self.page_layout.addLayout(self.filter_form)
        self.page_layout.addWidget(self.filter_button)
        self.page_layout.addLayout(self.search_form)
        self.page_layout.addLayout(self.bottom)

    def search_books(self):
        text = self.search_input.text()
        print(f"Searching for: {text}")
        #TODO: When db stuff is done, fill in the code here.
        #db_api.search_books(text)
        pass

    def filter_books(self):
        #get genre from text box
        genre_filter = self.genre_input.text()
        if genre_filter == "":
            genre_filter = None

        #get year from text box
        try:
            year_filter = int(self.year_input.text())
        except ValueError:
            year_filter = None

        print(f"Filtering by Genre: {genre_filter}, year: {year_filter}")

        #TODO:
        #if genre_filter and year_filter = None, grab regular books
        #if genre_filter or year_filter != None, grab books based on those filters