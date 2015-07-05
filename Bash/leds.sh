#!/bin/bash
echo 17 > /sys/class/gpio/export
echo 18 > /sys/class/gpio/export
echo 23 > /sys/class/gpio/export
echo 22 > /sys/class/gpio/export
while true; do
	val17=`cat /sys/class/gpio/gpio17/value`
	val18=`cat /sys/class/gpio/gpio18/value`
	if [[ val17 -eq 1 ]]; then
		echo 1 > /sys/class/gpio/gpio22/value
	fi

	if [[ val18 -eq 1 ]]; then
		echo 1 > /sys/class/gpio/gpio23/value
	fi
done
