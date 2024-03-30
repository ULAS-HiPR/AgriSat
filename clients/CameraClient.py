import os
import numpy as np
from picamera2 import Picamera2

from .BaseClient import BaseClient


class CameraClient(BaseClient):
    def __init__(self):
        super().__init__()
        
        self.frame_count = 0
        os.makedirs("captures", exist_ok=True)
        
        self.picam2 = Picamera2()
        self.picam2.configure(self.picam2.create_still_configuration())
        self.picam2.start()

    def read(self):
        image = self.picam2.capture_array() # (3040, 4056, 3) - full res
        self.frame_count += 1
        return np.resize(image, (256, 256, 3))
    
    def persist(self, data):
        file_path = os.path.join("captures", f"frame-{self.frame_count}.npy")
        np.save(file_path, data)
        


