from PySide6.QtWidgets import QTabWidget

from UI.search_page import SearchPage

class Tab_Widget(QTabWidget):
    def __init__(self):
        super().__init__()
        #A dictionary containing the name of each tab, and the corresponding constructor for each tab.
        self.widgets_list = {
            "Search": SearchPage(), 
        }

        for name,widget in self.widgets_list.items():
            self.addTab(widget,name)