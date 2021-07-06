#!/bin/bash
    
    sudo cp gps_rtk.rules  /etc/udev/rules.d
    echo " "
    echo "Restarting udev"
    echo ""
    sudo service udev reload
    sudo service udev restart
    echo "finish "
