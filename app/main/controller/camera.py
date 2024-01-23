import cv2
from threading import Thread
from datetime import datetime

class Camera():
    def __init__(self, device=None):
        if not device:
            self._device = self.get_device()
        self._loop_timer = self.get_device()
        self.stopped = False
        
    def get_device(self):
        index = 0
        arr = []
        i = 10
        while i > 0:
            cap = cv2.VideoCapture(index)
            if cap.read()[0]:
                arr.append(index)
                cap.release()
            index += 1
            i -= 1
            
        if len(arr) < 1:
            return None
        elif len(arr) > 1:
            return arr[1]
        else:
            return arr[0]
        
    @property
    def device(self):
        return self._device
        
    @device.setter
    def device(self, device):
        self._device = device
        
    def start(self):
        """
        Start streaming from device
        """
        cap = cv2.VideoCapture(self._device)
        self.grabbed, self.frame = cap.read()
        self.stopped= False
        if not self.grabbed:
            err_message = f"No camera device found for: {self._device}"
            raise Exception(err_message)
        else:
            self.cap = cap
            
    def stream(self):
        """
        Check for conditions to stop stream
        """
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                self.grabbed, self.frame = self.cap.read()
                
    def thread_stream(self):
        """
        Start a thread to stream camera
        """
        self.start()
        Thread(target=self.stream, args=()).start()
        
    def stop(self):
        self.stopped=True
        self.cap.release()
        
    def save_image(self, fileName):
        try:
            cv2.imwrite(fileName, self.frame)
            print(f"Saved image as {fileName}")
            return True
        except:
            print("Failed to save image")
            return False