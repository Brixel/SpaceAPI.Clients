#!/bin/bash
echo "Disabling leds"
echo 0 > /sys/class/gpio/gpio22/value
echo 0 > /sys/class/gpio/gpio23/value