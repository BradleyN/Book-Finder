from PySide6.QtCore import Slot
from time import sleep
from PySide6.QtWidgets import QTabWidget

from UI.Pages.search_page import SearchPage

class Tab_Widget(QTabWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        #A dictionary containing the name of each tab, and the corresponding constructor for each tab.
        self.widgets_list = {
            "Search": SearchPage(parent=self), 
        }

        for name,widget in self.widgets_list.items():
            self.addTab(widget,name)

    @Slot(object)
    def hello(self,data):
        print("hello")
        print(data[0])