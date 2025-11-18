from PySide6.QtCore import QRunnable, Slot, QThreadPool
from Backend.Signal import WorkerSignals

import traceback
import sys

class Worker(QRunnable):
    """Worker thread that processes tasks asynchronously in the background.
    
    Inherits from QRunnable to handle worker thread setup, signals, and cleanup.

    :param process_result: Callback function to process the result of the worker.
    :param final_function: Callback function to run when the worker finishes (always called).
    :param fn: The function to execute in the worker thread.
    :param args: Arguments for the function `fn`.
    :param kwargs: Keyword arguments for the function `fn`.
    """



    def __init__(self,fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()  # Signals for result, error, and finished

    
    @Slot()
    def run(self):
        """Execute the task in the worker thread."""
        try:
            # Run the function and get the result
            result = self.fn(*self.args, **self.kwargs)
        except Exception:
            # If an error occurs, emit the error signal
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            # Optionally, emit the result signal (if you want to use it elsewhere)
            self.signals.result.emit(result)
        finally:
            # Always call the final callback function (clean-up or any final steps)
            self.signals.finished.emit()
        
    def setup(self, error_func=None, result_func=None, finished_func=None):
        if error_func is not None:
            self.signals.error.connect(error_func)
        if result_func is not None:
            self.signals.result.connect(result_func)
        if finished_func is not None:
            self.signals.finished.connect(finished_func)

