from PySide6.QtCore import QObject, Signal, Slot
from BooksTable import Books

class DatabaseWorker(QObject):
    """ Worker class to handle database operations in a separate thread. """
    
    # Define signals
    requestData = Signal(str, object)         # Emit when a request for data is made
    dataReady = Signal(str, object)   # Emit when data is ready to send back to UI

    @Slot(str)  # Slot to handle incoming requests
    def handleRequest(self, query_name):
        """ Handle different types of requests based on the query name. """
        if query_name == "fetch_all":
            data = Books.fetch_all()  # Fetch all users
        else:
            data = []  # No matching query found
        
        # Emit the data back to the UI
        self.dataReady.emit(query_name, data)