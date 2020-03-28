import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

segments = (2,3,4,17,27,22,10)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)


GPIO.cleanup()
print("Led off")

digits_dict = {
    '0': (0, 0, 0, 0, 0, 0, 1),
    '1': (1, 0, 0, 1, 1, 1, 1),
    '2': (0, 0, 1, 0, 0, 1, 0),
    '3': (0, 0, 0, 1, 1, 0, 1),
    '4': (1, 0, 0, 1, 1, 0, 0),
    '5': (0, 1, 0, 0, 1, 0, 0),
    '6': (0, 1, 0, 0, 0, 0, 1),
    '7': (0, 0, 0, 1, 1, 1, 1),
    '8': (0, 0, 0, 0, 0, 0, 0),
    '9': (0, 0, 0, 0, 1, 0, 0)
}


def displaydigit(digit, place):
    for segment in segments:
        GPIO.output(segment, GPIO.LOW)
    

def displaynumber(number):
    nextif = True
    while nextif:
        digits = list(number)
        for digit in digits:
            displaydigit(digit,  digits.index(digit))
        time.sleep(5)
        nextif=False


try:
    numbers = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
    for number in numbers:
        print("Displaying {}".format(number))
        displaynumber(number)


finally:
    GPIO.cleanup()