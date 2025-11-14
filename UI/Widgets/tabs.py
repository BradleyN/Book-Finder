from PySide6.QtWidgets import QTabWidget

from UI.Pages.search_page import SearchPage
#from UI.Pages.suggested_reading import Popular_Items

class Tab_Widget(QTabWidget):
    def __init__(self):
        super().__init__()
        #A dictionary containing the name of each tab, and the corresponding constructor for each tab.
        self.widgets_list = {
            "Search": SearchPage(), 
            #"Popular": Popular_Items()
        }

        for name,widget in self.widgets_list.items():
            self.addTab(widget,name)