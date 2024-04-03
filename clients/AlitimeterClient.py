import os
import numpy as np
import board
import adafruit_bmp3xx
from datetime import datetime

from .BaseClient import BaseClient

class AlitimeterClient(BaseClient):
    def __init__(self):
        super().__init__()
        i2c = board.I2C()  
        self.bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)

        self.bmp.pressure_oversampling = 8
        self.bmp.temperature_oversampling = 2

        #sea level pressure needs to be checked and adjuested on day for accuracte height
        self.bmp.sea_level_pressure = 997

    def read(self):
        pressure = self.bmp.pressure
        temperature = self.bmp.temperature
        altitude = self.bmp.altitude
        return(pressure, temperature, altitude)
    
    def persist(self, data):
        time = str(datetime.now())
        data =  str(time) + ", " + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2])
        with open("alitimeter.csv", "a") as f:
            f.write(data + "\n")
        