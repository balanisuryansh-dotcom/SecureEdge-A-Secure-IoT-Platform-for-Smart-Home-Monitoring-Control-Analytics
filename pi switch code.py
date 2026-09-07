import RPi.GPIO as GPIO
import time

# GPIO pins for each light
LIGHTS = {
    1: 17,
    2: 27,
    3: 22
}

GPIO.setmode(GPIO.BCM)

# Set all light pins as outputs
for pin in LIGHTS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


def set_light(light_number, state):
    """
    Switch a light ON or OFF.

    light_number: 1, 2, or 3
    state: True = ON, False = OFF
    """

    if light_number not in LIGHTS:
        print("Invalid light number")
        return

    pin = LIGHTS[light_number]

    GPIO.output(pin, GPIO.HIGH if state else GPIO.LOW)

    print(f"Light {light_number} -> {'ON' if state else 'OFF'}")


try:
    # Example commands
    set_light(1, True)    # Light 1 ON
    time.sleep(2)

    set_light(1, False)   # Light 1 OFF
    time.sleep(1)

    set_light(2, True)    # Light 2 ON
    time.sleep(2)

    set_light(2, False)   # Light 2 OFF
    time.sleep(1)

    set_light(3, True)    # Light 3 ON
    time.sleep(2)

    set_light(3, False)   # Light 3 OFF

finally:
    GPIO.cleanup()