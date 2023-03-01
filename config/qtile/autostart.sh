#!/bin/sh
feh --bg-scale --randomize ~/.config/wallpapers/*
xfce4-power-manager &
nm-applet &
#picom --vsync -f &
#picom --experimental-backends &

