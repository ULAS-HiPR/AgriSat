import serial
import adafruit_gps
from datetime import datetime

from .BaseClient import BaseClient
from handlers.CSVHandler import CSVHandler


class GpsClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.csv = CSVHandler("gps", ["time", "latitude", "longitude"])

        self.gps = adafruit_gps.GPS(
            serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000), debug=False
        )

        self.gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
        self.gps.send_command(b"PMTK220,1000")

    def read(self):
        self.gps.update()
        if not self.gps.has_fix:
            return (-1, -1)  # Non breaking error

        return (self.gps.latitude, self.gps.longitude)

    def persist(self, data):
        self.csv.write([str(datetime.now()), *data])
