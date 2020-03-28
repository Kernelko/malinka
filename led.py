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
segments = (2,3,4,17,27,22,10)


def setuppins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for segment in segments:
        GPIO.setup(segment, GPIO.OUT)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)




def displaydigit(digit, place):
    for segment in segments:
        if place == 0:
            GPIO.output(9,GPIO.LOW)
            GPIO.output(11, GPIO.HIGH)
        elif place == 1:
            GPIO.output(9, GPIO.HIGH)
            GPIO.output(11, GPIO.LOW)
        GPIO.output(segment, digits_dict[digit][segments.index(segment)])
    

def displaynumber(number):
    displaydigit(number[0], 0)
    print("next")
    time.sleep(0.005)
    displaydigit(number[1], 1)



try:
    setuppins()
    numbers = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
    for number in numbers:
        print("Displaying {}".format(number))
        displaynumber(number)
        time.sleep(1)


finally:
    GPIO.cleanup()
