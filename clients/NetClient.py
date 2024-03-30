from .BaseClient import BaseClient


class NetClient(BaseClient):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def read(self):
        return self.queue.get()["timestamp"]

    def persist(self, data):
        print(data)
