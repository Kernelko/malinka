from libs.led import displaynumber, setuppins
from libs.humidity import read_sensor
import RPi.GPIO as GPIO


try:
    setuppins()
    while True:
        humidity, temperature = read_sensor()
        if humidity and temperature:
            displaynumber(temperature)
            print("Temp={0:0.1f}*C Humidity= {1:0.1f}%".format(temperature, humidity))
        else:
            print("Failed to retrieve data")


finally:
    GPIO.cleanup()
