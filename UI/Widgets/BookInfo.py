from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem, QAbstractItemView, QVBoxLayout, QWidget, QLabel, QSizePolicy,QSpacerItem, QDialog, QFrame

class BookInfo(QWidget):
    def __init__(self):
        super().__init__()   
        self.name = ""
        self.author = ""
        self.name_label = QLabel(f"Name: {self.name}")
        self.author_label = QLabel(f"Author: {self.author}")
        #TODO: FIND A BETTER WAY TO NOT HAVE THE ITEMS MOVE DOWN WHEN STRETCHING THE WINDOW
        self.spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        #TODO: WRITE A CUSTOM LABEL CLASS THAT AUTOMATICALLY DOES THIS
        self.name_label.setWordWrap(True)
        self.author_label.setWordWrap(True)
        
        #TODO: WRITE A CUSTOM Frame CLASS THAT AUTOMATICALLY DOES THIS
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)  # Horizontal line
        separator.setFrameShadow(QFrame.Sunken) # Gives a 3D effect (optional)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.name_label)
        self.vertical_layout.addWidget(separator)
        self.vertical_layout.addWidget(self.author_label)
        self.vertical_layout.addItem(self.spacer)

        self.vertical_layout.setContentsMargins(20, 10, 20, 10)
        self.setFixedWidth(300)
        self.setLayout(self.vertical_layout)

    def set_book_info(self,name, author):
        self.name_label.setText(f"Name: {name}")
        self.author_label.setText(f"Author: {author}")