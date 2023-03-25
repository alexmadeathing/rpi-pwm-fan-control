#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

apt install python3-rpi.gpio

cd "$(dirname "$0")"
cp rpi-pwm-fan-control.py /usr/local/bin/
cp rpi-pwm-fan-control.service /etc/systemd/system/
systemctl start rpi-pwm-fan-control
