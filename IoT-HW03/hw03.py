from gpiozero import Button, MotionSensor
from picamera2 import Picamera2
from time import sleep
from signal import pause
import os

button = Button(2)
pir = MotionSensor(4)

camera = Picamera2()

save_path = "/home/pi/Desktop"
os.makedirs(save_path, exist_ok=True)

camera.start()
sleep(2)

i = 0

def stop_camera():
    camera.stop()
    exit()

def take_photo():
    global i
    i += 1
    filename = f"{save_path}/image_{i}.jpg"
    camera.capture_file(filename)
    print("A photo has been taken:", filename)
    sleep(10)

button.when_pressed = stop_camera
pir.when_motion = take_photo

pause()