#!/bin/bash
/home/helg/.local/bin/dronekit-sitl copter 
sleep 2

~/QGroundControl.AppImage 2>/dev/null&
sleep 2

screen -dm mavproxy.py --master=tcp:127.0.0.1:5760 --out:127.0.0.1:14550 --out:127.0.0.1:5762

python "$1" --connect 127.0.0.1:5762

function finish {
    kill -9 $(ps -ef | grep QG | awk -F' ' '{print $2}')
    kill -9 $(ps -ef | grep ardu | awk -F' ' '{print $2}')
    kill -9 $(ps -ef | grep mav | awk -F' ' '{print $2}')
}
trap finish EXIT