import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
control_pins = [7, 11, 13, 15]
for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)


def setStep(steps, control_pins=control_pins):
    for pin in control_pins:
        GPIO.output(pin, steps[control_pins.index(pin)])


def forward(delay, step):
    for i in range(0, step):
        setStep([1, 0, 1, 0])
        time.sleep(delay)
        setStep([0, 1, 1, 0])
        time.sleep(delay)
        setStep([0, 1, 0, 1])
        time.sleep(delay)
        setStep([1, 0, 0, 1])
        time.sleep(delay)


forward(0.001, 1)


GPIO.cleanup()
