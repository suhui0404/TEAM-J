# IoT Team-J HW01 - Raspberry Pi LED Control

## 1. Objective

Learn how to control Raspberry Pi GPIO digital outputs using Python and the gpiozero library.  
This project demonstrates LED control through GPIO pin output signals.

## 2. Environment

- Raspberry Pi 5
- Raspberry Pi OS (64-bit)
- Python 3
- gpiozero library

## 3. Circuit

### Components
- Raspberry Pi
- LED
- 220Ω Resistor
- Breadboard

## 4. Files

- Python source code is included in the repository.
- Result images and GIF files are included in the images folder.

## 5. Issues / Troubleshooting

### Wi-Fi Connection Issue
- Raspberry Pi was not detected on the network.
- Reconfigured Wi-Fi settings and reconnected successfully.

### SSH Connection Failure
- PuTTY connection timed out.
- Checked network connection and retried SSH access.

### GPIO Busy Error
- Existing Python process occupied GPIO pins.
- Solved using:
```bash
sudo pkill python3
```

### LED Connection Error
- LED polarity and GPIO pin configuration were incorrect.
- Reconnected LED and verified GPIO pin numbers.

## 6. Conclusion

Through this project, I learned how to control Raspberry Pi GPIO outputs using Python and the gpiozero library.  
I also experienced troubleshooting various hardware and network issues while working with Raspberry Pi.
