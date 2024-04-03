import os
import numpy as np
import serial
import busio
import adafruit_gps
import time

from .BaseClient import BaseClient

#pi must be set up with adafruit blinka (see notion guide)
class GpsClient(BaseClient):
    def __init__(self):
        super().__init__()
        uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)
        self.gps = adafruit_gps.GPS(uart, debug=False)  
    
        self.gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
        self.gps.send_command(b"PMTK220,1000")

    def read(self):
        self.gps.update()
        if not self.gps.has_fix:
            return "no fix"

        return (str(self.gps.latitude) + ", " + str(self.gps.longitude))
    
    def persist(self, data):
        time = str(datetime.now())
        data =  str(time) + ", " + data
        with open("gps.csv", "a") as f:
            f.write(data + "\n")
