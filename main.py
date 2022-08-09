import RPi.GPIO as GPIO
import time
import urllib.request
import requests
import json

GPIO.setmode(GPIO. BCM)
TRIG =26
ECHO = 21

while True:
    print("Distance Measurement In Progress ") 
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    print("waiting For Sensor To Settle")
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO. input(ECHO)==0:
        pulse_start = time.time()
    while GPIO . input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17150
    distance = round(distance,2)
    print ("Distance: ",distance, "cm")
#data sent to cloud
    val= distance
    URl='https://api.thingspeak.com/update?api_key='
    KEY='IH0LKYP1RZEB227V'
    HEADER='&field1={}'.format(val)
    NEW_URL = URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)

    time.sleep(2)