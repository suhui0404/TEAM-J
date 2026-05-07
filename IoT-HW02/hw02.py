from gpiozero import LED, Button

led = LED(27)
button = Button(4)

while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()