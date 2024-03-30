import multiprocessing
from abc import ABC, abstractmethod

from handlers.StoreHandler import StoreHandler


class BaseClient(multiprocessing.Process, ABC):
    def __init__(self):
        multiprocessing.Process.__init__(self)

    @abstractmethod
    def read(
        self,
    ):
        # Must return payload from sensor i.e image, temperature, etc.
        pass

    def run(self):
        data = self.read_client()
        StoreHandler().update_dataframe(data)
