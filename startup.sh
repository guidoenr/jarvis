#!bin/bash

sleep 1

mpg123 ~/Desktop/jarvis/resources/jarvisintro.mp3 & 

sleep 1

chromium github.com/guidoenr &
sleep 2

gnome-terminal -e htop --geometry 87x27+2050+200 &
gnome-terminal --geometry 87x27+3000+200 &

exit


