import threading
from abc import ABC, abstractmethod


class BaseClient(threading.Thread, ABC):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True

    @abstractmethod
    def read(
        self,
    ):
        """
        Must return payload from sensor i.e image, temperature, etc.
        """
        pass
    
    @abstractmethod
    def persist(self, data):
        """
        Must implement function to save read data
        """
        pass 

    def run(self):
        while self.running:
            data = self.read()
            self.persist(data)