import RPi.GPIO as GPIO
import time
from datetime import datetime

digits_dict = {
    '0': (0, 0, 0, 0, 0, 0, 1),
    '1': (1, 0, 0, 1, 1, 1, 1),
    '2': (0, 0, 1, 0, 0, 1, 0),
    '3': (0, 0, 0, 0, 1, 1, 0),
    '4': (1, 0, 0, 1, 1, 0, 0),
    '5': (0, 1, 0, 0, 1, 0, 0),
    '6': (0, 1, 0, 0, 0, 0, 0),
    '7': (0, 0, 0, 1, 1, 1, 1),
    '8': (0, 0, 0, 0, 0, 0, 0),
    '9': (0, 0, 0, 0, 1, 0, 0)
}
segments = (3,4,17,27,22,10,9)


def setuppins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for segment in segments:
        GPIO.setup(segment, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)


def displaydigit(digit, place):
    for segment in segments:
        if place == 0:
            GPIO.output(11,GPIO.LOW)
            GPIO.output(5, GPIO.HIGH)
        elif place == 1:
            GPIO.output(11, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
        GPIO.output(segment, digits_dict[digit][segments.index(segment)])
    

def displaynumber(number):
    t1 = datetime.now()
    while (datetime.now()-t1).seconds <= 1:
        displaydigit(number[0], 0)
        time.sleep(0.005)
        displaydigit(number[1], 1)
        time.sleep(0.005)
        displaydigit(number[0], 0)
