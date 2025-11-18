from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QPushButton

class DictionaryTableModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self._data = data  # List of dictionaries
        self._headers = list(self._get_all_keys())  # Extract column headers from all dictionaries

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            row_data = self._data[index.row()]
            column_key = self._headers[index.column()]
            return row_data.get(column_key, None)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        return None

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            row_data = self._data[index.row()]
            column_key = self._headers[index.column()]
            row_data[column_key] = value  # Update the value in the dictionary
            self.dataChanged.emit(index, index)  # Notify the view to update the cell
            return True
        return False

    def _get_all_keys(self):
        keys = set()
        for item in self._data:
            keys.update(item.keys())
        return keys

    def update_data(self, row, column, new_value):
        """This method updates the model's data and notifies the view."""
        row_data = self._data[row]
        column_key = self._headers[column]
        row_data[column_key] = new_value  # Update the value
        index = self.createIndex(row, column)  # Create the index for the changed cell
        self.dataChanged.emit(index, index)  # Notify the view to update that cell

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Editable Dictionary TableModel Example")
        self.setGeometry(100, 100, 400, 300)

        # Sample data: a list of dictionaries
        data = [
            {"key1": "value1", "key2": "value2"},
            {"key1": "value3"},
            {"key2": "value4"}
        ]

        # Create model and set data
        self.model = DictionaryTableModel(data)

        # Create a QTableView and set the model
        self.table_view = QTableView(self)
        self.table_view.setModel(self.model)

        # Create a button to update a specific cell
        self.update_button = QPushButton("Update Cell", self)
        self.update_button.clicked.connect(self.update_cell)
        self.update_button.setGeometry(150, 250, 100, 30)

        self.setCentralWidget(self.table_view)

    def update_cell(self):
        """Simulate updating the value of a specific cell."""
        row, column = 1, 0  # We will update the second row, first column (key1 in the second row)
        new_value = "updated_value"
        self.model.update_data(row, column, new_value)  # Update the model's data and notify the view

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
