from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QFrame, QVBoxLayout, QHBoxLayout, QApplication, QFormLayout, QLabel
from UI.Widgets.input import TextBox, Button, LineInput

class ReviewPopup(QDialog):
    def __init__(self, main_window, book_id):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Review Editor")

        #Make sure book_id is the right format, then assign it
        try:
            int(book_id)
            self.book_id = book_id
        except ValueError:
            print("Error: book_id is not an int")
            self.close()

        # Create Widgets
        self.score_label = QLabel("Score: ")
        self.score_suffix_label = QLabel("/ 10")
        self.score_input = LineInput() #Input for the score.
        self.review_text_input = TextBox() #Text box to input the review text
        self.create_review_button = Button("Create Review",click_on_enter=False) #Create review button. 
        self.cancel_button = Button("Cancel",click_on_enter=False) #Cancel button

        #Make the score input field big enough for just two characters to visually suggest how long the input should be
        self.score_input.setMaximumWidth(50)
    
        self.score_input_form = QHBoxLayout()
        self.score_input_form.addStretch()
        self.score_input_form.addWidget(self.score_label)
        self.score_input_form.addWidget(self.score_input)
        self.score_input_form.addWidget(self.score_suffix_label)
        self.score_input_form.addStretch()

        self.score_input_form.setAlignment(Qt.AlignCenter)

        # Bottom buttons layout
        self.bottom_buttons = QHBoxLayout()
        self.bottom_buttons.addWidget(self.create_review_button)
        self.bottom_buttons.addWidget(self.cancel_button)

        # Main vertical layout
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addLayout(self.score_input_form)
        self.vertical_layout.addWidget(self.review_text_input)
        self.vertical_layout.addLayout(self.bottom_buttons)

        # Set border and shadow for text input
        self.review_text_input.setFrameShape(QFrame.Box)
        self.review_text_input.setFrameShadow(QFrame.Sunken)
        self.review_text_input.setLineWidth(1)
    
        # Get current stylesheet from application
        self.setStyleSheet(QApplication.instance().styleSheet())

        # Set the layout for the dialog
        self.setLayout(self.vertical_layout)

        # Connect signals to slots
        self.cancel_button.clicked.connect(self.close)
        self.score_input.textChanged.connect(self.clamp_values)

    def closeEvent(self, event):
        self.main_window.popup = None
        event.accept()

    def clamp_values(self):
        #Remove whitespace from the end of the input
        self.score_input.setText(self.score_input.text().strip())
        try:
            value = int(self.score_input.text())
            #Clamp values in range 0-10
            if value > 10:
                self.score_input.setText("10")
            elif value < 0:
                self.score_input.setText("0")
        except ValueError:
            #Remove any non text characters
            self.score_input.setText(self.score_input.text()[:-1])