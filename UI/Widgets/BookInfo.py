from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QSizePolicy,QSpacerItem, QFrame, QScrollArea
from UI.Widgets.input import Button

class BookInfo(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)  
        self.info = {
            "Title" : Label("Title: "),
            "Authors" : Label("Authors: "),
            "Description" : Label("Description: "),
            "Category" : Label("Category: "),
            "Publisher" : Label("Publisher: "),
            "Price Starting With ($)" : Label("Price: $"),
            "Publish Date (Month)" : Label("Publish Month: "),
            "Publish Date (Year)" : Label("Publish Year: ",include_seperator=False)
        }

        self.current_book_id = None

        #TODO: FIND A BETTER WAY TO NOT HAVE THE ITEMS MOVE DOWN WHEN STRETCHING THE WINDOW
        self.spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)


        self.add_review_button = Button("Add Review")
        self.edit_review_button = Button("Edit Review")

        self.horizontal_buttons = QHBoxLayout()
        self.horizontal_buttons.addWidget(self.add_review_button)
        self.horizontal_buttons.addWidget(self.edit_review_button)

        self.vertical_layout = QVBoxLayout()

        for _,label in self.info.items():
            self.vertical_layout.addLayout(label.vertical_layout) 

        self.vertical_layout.addLayout(self.horizontal_buttons)
        self.vertical_layout.addItem(self.spacer)

        self.vertical_layout.setContentsMargins(10, 10, 10, 10)
        
        # Set the layout to be scrollable
        self.scroll_area = QScrollArea(self)
        self.scroll_widget = QWidget(self)
        self.scroll_widget.setLayout(self.vertical_layout)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)

        # Set the scroll area as the main layout of the widget
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.scroll_area)

        # Set the fixed width of the widget
        self.setFixedWidth(350)
        self.setLayout(main_layout)

    def set_book_info(self,book_data):
        for key, value in book_data.items():
            if key != "book_id":
                self.info[key].changeData(value)
            else:
                self.book_id = value

class Label(QWidget):
    def __init__(self, text, data=None, include_seperator=True):
        super().__init__()
        self.text = text
        
        #Optional starting info.
        if data is not None:
            self.text += data
    
        self.label = QLabel(text)
        self.label.setWordWrap(True)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.label)

        if include_seperator:
            seperator = QFrame()
            seperator.setFrameShape(QFrame.HLine)  # Horizontal line
            seperator.setFrameShadow(QFrame.Sunken) # Gives a 3D effect (optional)
            self.vertical_layout.addWidget(seperator)

    def changeData(self,new_data):
        self.label.setText(self.text + new_data)
