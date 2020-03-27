import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

segments = (2,3,4,17,27,22,10)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)

GPIO.setup(14, GPIO.OUT)
GPIO.output(14, GPIO.HIGH)

for segments in segments:
    print("Led on")
    GPIO.output(segment, GPIO.LOW)
time.sleep(5)


GPIO.cleanup()
print("Led off")


