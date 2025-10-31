from __future__ import annotations

from PySide6.QtWidgets import (
    QFormLayout, QVBoxLayout, QWidget
)

from UI.Widgets.table import Table
from UI.Widgets.input import LineInput
from Backend.BooksTable import Books

#This class is responsible for creating the UI for the search tab of the application
class SearchPage(QWidget):
    def __init__(self):
        super().__init__()

        #Temporary. Eventually this will be replaced once the backend is done and we can get the books to read directly from the database
        self.books = Books
        self.book_list = self.books.fetch_all()
        self.table = Table(["Title", "Author", "Description", "Category", "Publisher", "Price in USD", "Publish Month", "Publish Year"])
        self.table.fill_table(self.book_list)

        #Create search bar        
        search_input = LineInput()
        search_form = QFormLayout()
        search_form.addRow("Search:", search_input)

        self.page_layout = QVBoxLayout()
        self.page_layout.addLayout(search_form)
        self.page_layout.addWidget(self.table)
        self.setLayout(self.page_layout)
