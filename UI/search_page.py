from __future__ import annotations

from PySide6.QtWidgets import (
    QFormLayout, QVBoxLayout, QWidget
)

from UI.Widgets.table import Table
from UI.Widgets.input import LineInput

#This class is responsible for creating the UI for the search tab of the application
class SearchPage(QWidget):
    def __init__(self):
        super().__init__()

        #Temporary. Eventually this will be replaced once the backend is done and we can get the books to read directly from the database
        self.books = {"Goat Brothers": ("11111111 Colton, Larry", "", "History" , "General Doubleday", 8.79, "January", 1993)}

        self.table = Table(["Title", "Author", "Description", "Category", "Publisher", "Price in USD", "Publish Month", "Publish Year"])
        self.table.fill_table(self.books)

        #Create search bar        
        search_input = LineInput()
        search_form = QFormLayout()
        search_form.addRow("Search:", search_input)

        self.page_layout = QVBoxLayout()
        self.page_layout.addLayout(search_form)
        self.page_layout.addWidget(self.table)
        self.setLayout(self.page_layout)
