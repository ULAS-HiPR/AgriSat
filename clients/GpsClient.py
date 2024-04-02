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
        tx = 1
        rx = 0
        uart = busio.UART(tx, rx, baudrate=9600, timeout=10)
        self.gps = adafruit_gps.GPS(uart, debug=False)  
    
        self.gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
        self.gps.send_command(b"PMTK220,1000")

    def read(self):
        self.gps.update()
        if not self.gps.has_fix:
            return "no fix"
        
        return ("Latitude: {0:.6f} degrees".format(self.gps.latitude)+ ",Longitude: {0:.6f} degrees".format(self.gps.longitude))
    
    def persist(self, data):
        time = time.time.now()
        data =  str(time) + " " + data
        file_path = os.path.join("gpsDate", f"gpsData-{self.gps.timestamp_utc.tm_mon}-{self.gps.timestamp_utc.tm_mday}-{self.gps.timestamp_utc.tm_year}.npy")
        np.save(file_path, data)
        
