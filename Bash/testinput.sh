#!/bin/bash
echo "Checking inputs"
while [[ true ]]; do
	val17=`cat /sys/class/gpio/gpio17/value`
	val18=`cat /sys/class/gpio/gpio18/value`
	if [[ $val17 -eq "1" ]]; then
		echo 1 > /sys/class/gpio/gpio22/value
		echo 0 > /sys/class/gpio/gpio23/value
	fi
	if [[ $val18 -eq "1" ]]; then
		echo 1 > /sys/class/gpio/gpio23/value
		echo 0 > /sys/class/gpio/gpio22/value
	fi
done