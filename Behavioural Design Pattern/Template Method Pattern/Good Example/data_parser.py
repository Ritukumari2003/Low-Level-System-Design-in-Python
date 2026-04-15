from abc import ABC, abstractmethod

class DataParser(ABC):

    def _open(self):
        print("Opening the file..")
    
    def _parse(self):
        self._open()

        # Parser
        self._dataParser()

        self._close()

    def _close(self):
        print("Closing the file...")

    @abstractmethod
    def _dataParser(self):
        pass