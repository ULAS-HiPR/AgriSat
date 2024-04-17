import board
import adafruit_bmp3xx
from datetime import datetime

from .BaseClient import BaseClient
from handlers.CSVHandler import CSVHandler


class AltimeterClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.csv = CSVHandler(
            "altimeter", ["time", "altitude", "pressure", "temperature"]
        )

        i2c = board.I2C()
        self.bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)

        self.bmp.pressure_oversampling = 8
        self.bmp.temperature_oversampling = 2

        # Adjust at location for accurate altitude readings
        self.bmp.sea_level_pressure = 997

    def read(self):
        return (self.bmp.altitude, self.bmp.pressure, self.bmp.temperature)

    def persist(self, data):
        self.csv.write([str(datetime.now()), *data])
