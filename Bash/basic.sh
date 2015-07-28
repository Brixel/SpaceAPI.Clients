#!/bin/bash
# pin 17 = close button
# pin 18 = open button

pollForInternet(){
        echo "Polling the web"
        internetStatus=`./connectedtointernet.sh`
        echo $internetStatus
        while [[ $internetStatus -eq "0" ]]; do
                echo "POLLING"
                internetStatus=`./connectedtointernet.sh`
                echo $internetStatus
        done
        echo "We have interwebz"
}



echo "Checking inputs"
while [[ true ]]; do
        internetStatus=`./connectedtointernet.sh`
        val17=`cat /sys/class/gpio/gpio17/value`
        val18=`cat /sys/class/gpio/gpio18/value`
        echo $internetStatus
        if [[ $val17 -eq "1" ]]; then
                echo "Close button pressed"
                python ../python/close.py
                echo 1 > /sys/class/gpio/gpio22/value
                echo 0 > /sys/class/gpio/gpio23/value

        fi
        if [[ $val18 -eq "1" ]]; then
                echo "Open button pressed"
                pollForInternet
                echo "Posting"
                python ../python/open.py
                echo 1 > /sys/class/gpio/gpio23/value
                echo 0 > /sys/class/gpio/gpio22/value

        fi
        if [[ $internetStatus -eq "0" ]]; then
              echo 0 > /sys/class/gpio/gpio22/value
              echo 0 > /sys/class/gpio/gpio23/value
        fi
done
