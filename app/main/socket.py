import cv2
import base64
from flask_socketio import emit
from .. import socketio
from app.main.controller.camera import Camera

source = 0
camera = None

@socketio.on("connect", namespace="/camera")
def connect():
    """
    Connecting to socket
    """
    emit("status", {"msg": "Connected to camera namespace"})
    global camera
    camera = Camera(source)
    camera.thread_stream()
    print("Connected to camera namespace")
    emit("status", {"msg": "Camera is on"})
    
@socketio.on("disconnect", namespace="/camera")
def disconnect():
    """
    Disconnecting from socket
    """
    global camera
    camera.stop()
    print("Disconnected from camera namespace")
    emit("status", {"msg": "Disconnected from camera namespace"})
    
@socketio.on("stream", namespace = "/camera")
def stream():
    """
    """
    global camera
    frame = camera.frame
    processed_frame = base64.b64encode(cv2.imencode('.jpg', frame)[1]).decode()
    b64_src = "data:image/jpg;base64,"
    processed_frame = b64_src + processed_frame
    print('python stream')
    emit("input_image", processed_frame)