from picamera2 import Picamera2

from .BaseClient import BaseClient


class CameraClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.picam2 = Picamera2()
        self.capture_config = self.picam2.create_still_configuration()
        self.picam2.start()

    def read(self):
        return self.picam2.switch_mode_and_capture_image(self.capture_config)

    def __del__(self):
        self.picam2.stop()
        self.picam2.close()
