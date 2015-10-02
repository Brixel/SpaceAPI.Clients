#!/bin/bash
wget -q --tries=2 --timeout=2 --spider http://google.com
if [[ $? -eq 0 ]]; then
        echo "0"
else
        echo "1"
fi