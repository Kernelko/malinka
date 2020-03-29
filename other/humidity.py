import Adafruit_DHT 
import time

DHT_SENSOR = Adafruit_DHT.DHT22

DHT_PIN = 2




while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity and temperature:
        print("Temp={0:0.1f}*C Humidity= {1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data")

