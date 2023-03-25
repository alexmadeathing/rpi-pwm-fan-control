# Raspberry Pi PWM Fam Controller
A simple python script to control the speed of a PWM fan based on core cpu temperature. Suitable for Raspberry Pi only.

# Pre-requisites
```bash
sudo apt install python3-rpi.gpio
```

# Installation from source
It is recommended that you install from source so that the correct GPIO pin and temperature ranges can be selected. These properties are currently hard coded in `rpi-pwm-fan-control.py`.

### Download from latest git
```bash
sudo apt install git
git clone https://github.com/alexmadeathing/rpi-pwm-fan-control.git
cd rpi-pwm-fan-control
```

### Download with curl
```bash
mkdir -p rpi-pwm-fan-control && cd $_
curl -LJ `curl -s https://api.github.com/repos/alexmadeathing/rpi-pwm-fan-control/releases/latest | python3  -c 'import sys, json; print(json.load(sys.stdin)["tarball_url"])'` | tar zxf - --strip=1
```

### (Optionally) Edit the source file and change the pin and min/max speed temperature value (in degrees C):
```bash
nano rpi-pwm-fan-control.py
```
```py
min_speed_temp = 40.0
max_speed_temp = 60.0

pwm_pin = 18
pwm_freq = 100

sleep_time = 5
```
