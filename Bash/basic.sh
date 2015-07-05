#!/bin/bash
# pin 17 = close button
# pin 18 = open button
echo "Checking inputs"
while [[ true ]]; do
	val17=`cat /sys/class/gpio/gpio17/value`
	val18=`cat /sys/class/gpio/gpio18/value`
	if [[ $val17 -eq "1" ]]; then
		echo "Close button pressed"
		echo 1 > /sys/class/gpio/gpio22/value
		echo 0 > /sys/class/gpio/gpio23/value
		python ../python/close.py
	fi
	if [[ $val18 -eq "1" ]]; then
		echo "Open button pressed"
		echo 1 > /sys/class/gpio/gpio23/value
		echo 0 > /sys/class/gpio/gpio22/value
		python ../python/open.py
	fi
done