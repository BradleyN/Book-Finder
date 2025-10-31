from PySide6.QtWidgets import QLineEdit, QPushButton

#Two Simple Wrapper classes for QLineEdit and QPushButton. 

class LineInput(QLineEdit):
    def __init__(self, include_clear_button=True):
        super().__init__(clearButtonEnabled=include_clear_button)

class Button(QPushButton):
    def __init__(self, text, enabled=True):
        super().__init__(text)
        self.setEnabled(enabled)

