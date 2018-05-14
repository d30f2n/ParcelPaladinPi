try:
    import RPi.GPIO
except RuntimeError:
    print("Error importing RPi.GPIO")

RPi.GPIO.setmode(RPi.GPIO.BCM)
