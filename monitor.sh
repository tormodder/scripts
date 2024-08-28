#! /bin/bash

# alias script to monitor
xrandr --auto 
xrandr --output $(xrandr --query | grep " connected" | grep -v "eDP" | awk '{print $1}') --above eDP-1
