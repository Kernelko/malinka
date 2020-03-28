import RPi.GPIO as GPIO
import time

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
segments = (2,3,4,17,27,22,10)

def setuppins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for segment in segments:
        GPIO.setup(segment, GPIO.OUT)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)




def displaydigit(digit, place):
    digits = (9,11)
    for segment in segments:
        GPIO.output(segment, GPIO.LOW)
        print(digits_dict[digit][segments.index(segment)])
        GPIO.output(digits[place], digits_dict[digit][segments.index(segment)])


    

def displaynumber(number):
    nextif = True
    while nextif:
        digits = list(number)
        for digit in digits:
            displaydigit(digit,  digits.index(digit))
        time.sleep(5)
        nextif=False


try:
    setuppins()
    numbers = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
    for number in numbers:
        print("Displaying {}".format(number))
        displaynumber(number)


finally:
    GPIO.cleanup()