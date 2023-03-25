#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

systemctl stop rpi-pwm-fan-control
rm /etc/systemd/system/rpi-pwm-fan-control.service
rm /usr/local/bin/rpi-pwm-fan-control.py

echo DONE
