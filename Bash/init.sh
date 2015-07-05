#!/bin/bash
echo "Initializing the GPIO pins"
echo 17 > /sys/class/gpio/export
echo 18 > /sys/class/gpio/export
echo 22 > /sys/class/gpio/export
echo 23 > /sys/class/gpio/export

echo "Pins exported"

echo in > /sys/class/gpio/gpio17/direction
echo in > /sys/class/gpio/gpio18/direction
echo out > /sys/class/gpio/gpio22/direction
echo out > /sys/class/gpio/gpio23/direction

echo "Configured pin connections"