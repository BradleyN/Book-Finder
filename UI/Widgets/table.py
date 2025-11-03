from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem, QAbstractItemView
from PySide6.QtCharts import QPieSeries
#import stylesheets

#Table is a class that creates the table with values of several columns of data.
#To create a table, you need to pass in a list of labels to the table.
class Table(QTableWidget):
    def __init__(self, col_labels):
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
        horizontal_header.setDefaultSectionSize(125) #Sets default column width to 125
        horizontal_header.resizeSection(2, 250) #Set width of Description column to double the default

        #Hide the vertical header, and set the vertical header to resize to the size of the item.
        vertical_header = self.verticalHeader()
        vertical_header.hide()
        vertical_header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.num_rows = 0

    #takes a dictionary of items and uses it to fill in the list
    #Dictionary should be in the form {"first column": [value 1, value 2, value 3, ...]}
    def fill_table(self, data):
        #Make sure that data has values in it
        if not data:
            raise ValueError("Attempted to fill table with no data.")
        for key, values in data.items():
            self.insertRow(self.num_rows)
            self.addTableValue(key,0)
            column_index = 1
            for data_point in values:
                self.addTableValue(data_point,column_index)
                column_index += 1
            self.num_rows += 1

    def addTableValue(self,value,column):
        entry = QTableWidgetItem(str(value))
        entry.setTextAlignment(Qt.AlignLeft)
        self.setItem(self.num_rows, column, entry)


    #This function takes the data in the chart and converts it to a QPieSeries
    def get_table_as_series(self):
        series = QPieSeries()
        for i in range(self.rowCount()):
            text = self.item(i, 0).text()
            number = float(self.item(i, 1).text())
            series.append(text, number)
        return series
    
    #Clear the data in the table
    def clear_table(self):
        self.setRowCount(0)
        self.items = 0