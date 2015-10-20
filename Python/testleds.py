import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# GPIO 23 & 17 set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
# So we'll be setting up falling edge detection for both
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.setup(22, GPIO.OUT) #led red
GPIO.setup(23, GPIO.OUT) #led green

p_red = GPIO.PWM(22, 0.5)
p_green = GPIO.PWM(23, 0.5)
p_red.start(100)
p_green.start(80)

p_red.ChangeFrequency(100)
p_green.ChangeFrequency(100)


# now we'll define two threaded callback functions
# these will run in another thread when our events are detected
def close_callback(channel):
    print "falling edge detected on 17"
    p_red.start(40)
    #p_green.ChangeDutyCycle(0)
    p_green.stop()
    execfile("close.py")
    print "Closed"
    p_red.ChangeDutyCycle(100)
    p_green.stop()

def open_callback(channel):
    print "falling edge detected on 23"
    p_green.start(30)
    p_red.stop()
    execfile("open.py")
    print "Opened"
    p_green.ChangeDutyCycle(100)


#raw_input("Press Enter when ready\n>")

# when a falling edge is detected on port 17, regardless of whatever
# else is happening in the program, the function my_callback will be run
GPIO.add_event_detect(17, GPIO.RISING, callback=close_callback, bouncetime=300)

# when a falling edge is detected on port 23, regardless of whatever
# else is happening in the program, the function my_callback2 will be run
# 'bouncetime=300' includes the bounce control written into interrupts2a.py
GPIO.add_event_detect(18, GPIO.RISING, callback=open_callback, bouncetime=300)

try:
        while True:
                 pass


except KeyboardInterrupt:
        GPIO.cleanup()           # clean up GPIO on normal exit