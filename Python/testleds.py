#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv
# http://RasPi.tv/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3
import RPi.GPIO as GPIO
import time;
GPIO.setmode(GPIO.BCM)

# GPIO 23 & 17 set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
# So we'll be setting up falling edge detection for both
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) #button
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #button
GPIO.setup(22, GPIO.OUT) #led 
GPIO.setup(23, GPIO.OUT) #led

GPIO.output(22,1)
GPIO.output(23,1)

time.sleep(5)
GPIO.output(22,0)
GPIO.output(23,0)
# GPIO 24 set up as an input, pulled down, connected to 3V3 on button press
#GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# now we'll define two threaded callback functions
# these will run in another thread when our events are detected
def openPressed(channel):
    print "falling edge detected on 17"
    GPIO.output(22, 1)
    GPIO.output(23, 0)
    raw_input("Press Enter when ready\n>")


def closePressed(channel):
    print "FALLINing edge detected on 18"
    GPIO.output(23, 1)
    GPIO.output(22, 0)
    raw_input("Press Enter when ready\n>")


# when a falling edge is detected on port 17, regardless of whatever 
# else is happening in the program, the function openPressed will be run
GPIO.add_event_detect(17, GPIO.RISING, callback=closePressed, bouncetime=200)
#GPIO.add_event_callback(17, closePressed)

# when a falling edge is detected on port 23, regardless of whatever 
# else is happening in the program, the function closePressed will be run
# 'bouncetime=300' includes the bounce control written into interrupts2a.py
GPIO.add_event_detect(18, GPIO.RISING, callback=openPressed, bouncetime=200)	
#raw_input("Press Enter when ready\n>")



try:
	while True: 
	pass 
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
	