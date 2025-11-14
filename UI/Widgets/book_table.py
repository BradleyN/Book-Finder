from PySide6.QtCore import Qt, QAbstractTableModel, QPoint
from PySide6.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QWidget, QLabel, QSizePolicy
from PySide6.QtCharts import QPieSeries
from PySide6.QtGui import QCursor
from UI.Widgets.input import Button
from UI.Widgets.BookInfo import BookInfo
#import stylesheets

#Table is a class that creates the table with values of several columns of data.
#To create a table, you need to pass in a list of labels to the table.

#TODO: Look at reimplementing with a QAbstractTableView
#TODO: look into extracting book table into a seperate class and then implement specifics for each book table in 
class Book_Table(QTableWidget):
    def __init__(self, col_labels,book_info=None):
        super().__init__()
        #Create columns
        self.setColumnCount(len(col_labels))
        self.setHorizontalHeaderLabels(col_labels)

        #Make it so the table can't be edited manually.
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #Made the table's scrollpars smooth instead of correcting to the nearest table element
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        #Adjust the horizontal header to stretch the last column to the edge of the canvas
        horizontal_header = self.horizontalHeader()
        horizontal_header.setStretchLastSection(True)
        horizontal_header.setDefaultSectionSize(160) #Sets default column width to 160
        horizontal_header.resizeSection(1, 250) #Set width of Description column to double the default

        #Hide the vertical header, and set the vertical header to resize to the size of the item.
        vertical_header = self.verticalHeader()
        vertical_header.hide()
        vertical_header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.book_info = book_info
        self.num_rows = 0
        

    #takes a dictionary of items and uses it to fill in the list
    #Dictionary should be in the form {"Label1": value1, "Label2": value2, ...}

    def fill_table(self, data):
        #Make sure that data has values in it
        if not data:
            raise ValueError("Attempted to fill table with no data.")
        
        for row in data:
            #Add a new row. Start at column 0 and move until you run out of items
            column_index = 0
            self.insertRow(self.num_rows)

            #Add items from each row one at a time
            for _, item in row.items():
                self.addTableValue(item,column_index)
                column_index += 1

            #Add a button at the end that says "See book info"
            self.addTableButton("See Book info", column_index)
            self.num_rows += 1

    def addTableValue(self,value,column):
        entry = QTableWidgetItem(str(value))
        entry.setTextAlignment(Qt.AlignLeft)
        self.setItem(self.num_rows, column, entry)

    def addTableButton(self,value,column):
        entry = Button(str(value))
        self.setCellWidget(self.num_rows, column, entry)
        entry.clicked.connect(self.onButtonClick)
    
    #TODO: MAKE THIS READ FROM THE DATABASE
    #TODO: MAKE THIS UNPACK DATA IN A BETTER WAY
    def onButtonClick(self):
        #returns a reference to button pressed
        button_pressed = self.sender()
        row = int(self.indexAt(button_pressed.pos()).row())

        title = self.item(row,0).text()
        author = self.item(row,1).text()
        self.book_info.set_book_info(title,author)
        
    #Clear the data in the table
    def clear_table(self):
        self.setRowCount(0)
        self.num_rows = 0
