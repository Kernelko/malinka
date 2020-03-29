import Adafruit_DHT 

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 2

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return humidity, temperature
