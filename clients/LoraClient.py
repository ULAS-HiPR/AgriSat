import os
import numpy as np
import serial
import busio
import time

from .BaseClient import BaseClient

#pi must be set up with adafruit blinka (see notion guide)
class LoraClient(BaseClient):
    def __init__(self, gps, altimiter):
        super().__init__()
        lora = 0

    def read(self):
        #read gps & alitimeter data
        pass
    
    def persist(self, data):
        #send gps & alitimeter data 
        pass
        
