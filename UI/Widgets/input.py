from PySide6.QtWidgets import QLineEdit, QPushButton, QSizePolicy

#Two Simple Wrapper classes for QLineEdit and QPushButton. 

class LineInput(QLineEdit):
    def __init__(self, include_clear_button=False):
        super().__init__(clearButtonEnabled=include_clear_button)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,  # horizontal stretch
            QSizePolicy.Policy.Preferred   # vertical size stays preferred
        )

class Button(QPushButton):
    def __init__(self, text, enabled=True):
        super().__init__(text)
        self.setEnabled(enabled)

