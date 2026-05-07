# IoT Team-J HW02 - Button Controlled LED

## 1. Objective

Use Raspberry Pi GPIO pins to read button input data and control an LED output using Python and the gpiozero library.

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
- Push Button
- Breadboard

## 4. Files

- Python source code is included in the repository.
- Result images and GIF files are included in the images folder.

## 5. Issues / Troubleshooting

### GPIO Busy Error
- `lgpio.error: 'GPIO busy'` occurred during execution.
- Solved by terminating existing Python processes:
```bash
sudo pkill python3
```

### Button Input Failure
- LED did not respond when the button was pressed.
- Rechecked button orientation, GPIO pin connections, and GND wiring.

## 6. Conclusion

Through this project, I learned how to use Raspberry Pi GPIO pins for both digital input and output.  
I also gained experience troubleshooting hardware connection issues and GPIO process conflicts while implementing button-controlled LED interaction.
