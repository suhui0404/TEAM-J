# IoT Team-J HW03 - Motion Detection Camera System

## 1. Objective

Use Raspberry Pi to detect motion with a PIR sensor and automatically capture photos using the Raspberry Pi Camera Module.

## 2. Environment

- Raspberry Pi 5
- Raspberry Pi OS (64-bit)
- Python 3
- gpiozero library
- picamera2 library

## 3. Circuit

### Components
- Raspberry Pi
- Raspberry Pi Camera Module v2
- HC-SR501 PIR Motion Sensor
- Push Button
- Breadboard
- Jumper Wires

## 4. Files

- Python source code is included in the repository.
- Result images and GIF/video files are included in the images folder.

## 5. Issues / Troubleshooting

### picamera Module Error
- `ModuleNotFoundError: No module named 'picamera'` occurred.
- Replaced the old `picamera` library with `picamera2`.

### Camera Detection Failure
- Camera was not detected by the system.
- Reconnected the camera cable and checked CSI port connection.

### libcamera Command Error
- `libcamera-hello: command not found` occurred.
- Installed the required `libcamera-apps` package.

### Camera Interface Issue
- Camera interface was disabled.
- Enabled the camera option using:
```bash
sudo raspi-config
```

### Circuit Short Problem
- Incorrect wiring caused circuit short issues.
- Rechecked GPIO, GND, and power connections carefully.

## 6. Conclusion

Through this project, I learned how to combine motion sensors and camera modules using Raspberry Pi GPIO and Python.  
I also gained experience troubleshooting camera configuration issues, hardware connection problems, and event-based sensor control systems.
