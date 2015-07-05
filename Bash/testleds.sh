#!/bin/bash
echo "Checking leds"
echo 1 > /sys/class/gpio/gpio22/value
echo 1 > /sys/class/gpio/gpio23/value
sleep 4
echo 0 > /sys/class/gpio/gpio22/value
echo 0 > /sys/class/gpio/gpio23/value
sleep 4
echo 1 > /sys/class/gpio/gpio22/value
sleep 1
echo 0 > /sys/class/gpio/gpio22/value
echo 1 > /sys/class/gpio/gpio23/value
sleep 1
echo 1 > /sys/class/gpio/gpio22/value
echo 0 > /sys/class/gpio/gpio23/value
sleep 1
echo 0 > /sys/class/gpio/gpio22/value
echo 1 > /sys/class/gpio/gpio23/value
sleep 1
echo 1 > /sys/class/gpio/gpio22/value
echo 0 > /sys/class/gpio/gpio23/value
sleep 1
echo 0 > /sys/class/gpio/gpio22/value
echo 1 > /sys/class/gpio/gpio23/value
sleep 1
echo 1 > /sys/class/gpio/gpio22/value
echo 0 > /sys/class/gpio/gpio23/value
sleep 1
echo 0 > /sys/class/gpio/gpio22/value
echo 0 > /sys/class/gpio/gpio23/value
sleep 1
echo 1 > /sys/class/gpio/gpio22/value
echo 1 > /sys/class/gpio/gpio23/value
sleep 2
echo 0 > /sys/class/gpio/gpio22/value
echo 0 > /sys/class/gpio/gpio23/value