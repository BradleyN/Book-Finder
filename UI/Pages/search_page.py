from __future__ import annotations

from PySide6.QtCore import Qt, Slot

from PySide6.QtWidgets import (
    QFormLayout, QVBoxLayout, QWidget, QLabel, QHBoxLayout
)

from UI.Widgets.input import LineInput, Button
from UI.Widgets.BookInfo import BookInfo
from UI.Widgets.TableModel import DictionaryTableModel
from UI.Widgets.TableView import TableView
from Backend.Signal import event_list
from Backend.async_worker import run_func_async
from Backend.Buisness_Logic import get_cols_data

#This class is responsible for creating the UI for the search tab of the application
class SearchPage(QWidget):
    def __init__(self,parent): 
        super().__init__(parent=parent)

        #Technical debt. Fix later maybe?
        self.book_info = BookInfo(parent=self)
        self.table = TableView(self)

        self.bottom = QHBoxLayout()
        self.bottom.addWidget(self.table)
        self.bottom.addWidget(self.book_info)

        self.createSearchBar()
        self.createFilterForm()
        self.buildLayout()
        self.setLayout(self.page_layout)

        self.search_input.returnPressed.connect(self.search_books)
        self.filter_button.clicked.connect(self.filter_books)

        self.show()
        event_list.create_event("Get_search_data")
        event_list.subscribe("Get_search_data",result_funcs=[self.recieve_data])
        run_func_async("Get_search_data",get_cols_data)

    @Slot(object)
    def recieve_data(self, data):
        self.table_model = DictionaryTableModel(data)
        self.table.setModel(self.table_model)

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

        self.table_model.update_row(0,{"Title": "Hello", "Author": "Guy"})

        print(f"Filtering by Genre: {genre_filter}, year: {year_filter}")


        #TODO:
        #if genre_filter and year_filter = None, grab regular books
        #if genre_filter or year_filter != None, grab books based on those filters