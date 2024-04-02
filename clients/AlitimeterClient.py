import os
import numpy as np

from .BaseClient import BaseClient


class CameraClient(BaseClient):
    def __init__(self):
        super().__init__()
        
        self.alimeter = 0

    def read(self):
        #read alitimeter
        pass
    
    def persist(self, data):
        #save data
        pass
        


