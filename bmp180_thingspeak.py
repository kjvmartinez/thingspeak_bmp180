import sys
import urllib2 
import RPi.GPIO as GPIO 
from time import sleep 
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085

myAPI = "WRITE API IN THINGSPEAK CHANNEL"

def main(): 
   print 'starting...'
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 
   while True: 
       try: 
           sensor = BMP085.BMP085()
           print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
           print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
           print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
           print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))
           f = urllib2.urlopen(baseURL + 
                    "&field1=%s&field2=%s&field3=%s&field4=%s" % (sensor.read_temperature(), sensor.read_pressure(), sensor.read_altitude(),sensor.read_sealevel_pressure() )) 
           print f.read() 
           f.close() 
           sleep(2) #uploads DHT22 sensor values every 5 minutes 
       except: 
           print 'exiting.' 
           break 
# call main 
if __name__ == '__main__': 
   main()  

