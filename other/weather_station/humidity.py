import Adafruit_DHT 
import time
import csv
from datetime import datetime

DHT_SENSOR = Adafruit_DHT.DHT22

DHT_PIN = 2




while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    with open('data_file.csv', mode='w') as datafile:
        writer= csv.writer(datafile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if humidity and temperature:
            date = datetime.now()
            writer.writerow([temperature, humidity,date])
            print("Temp={0:0.1f}*C Humidity= {1:0.1f}%".format(temperature, humidity))
            time.sleep(15)
        else:
            print("Failed to retrieve data")

