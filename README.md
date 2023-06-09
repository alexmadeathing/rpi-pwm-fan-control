# Raspberry Pi PWM Fam Controller
A simple python script to control the speed of a PWM fan based on core cpu temperature (temperature zone 0). Suitable for Raspberry Pi only.

An installer is provided which ensures the script runs on system startup.

# Installation from source
It is recommended that you install from source so that the correct GPIO pin and temperature ranges can be selected. These properties are currently hard coded.

### Download
```bash
sudo apt -qq install curl
mkdir -p rpi-pwm-fan-control && cd $_
curl -fsSL https://github.com/alexmadeathing/rpi-pwm-fan-control/archive/refs/heads/main.tar.gz | tar zxf - --strip=1 && echo DONE
```

### (Optional) Validate fan pin
You may use the `rpi-pin-test.py` utility to test that your fan will turn on and off correctly.

E.g. Turn fan (on pin 18) on:
```bash
python rpi-pin-test.py --pin 18 on
```

### (Optional) Edit the source file to change configuration:
```bash
nano rpi-pwm-fan-control.py
```
Look for the following variable assignments:
```py
min_speed_temp = 40.0 # Temperature at which fan speed should be 0%
max_speed_temp = 60.0 # Temperature at which fan speed should be 100%

pwm_pin = 18          # PWM Pin
                      # Refer to your Pi pinout diagram and use `rpi-pin-test.py` to test pins
                      #
                      # E.g. python rpi-pin-test.py --pin 18 on
                      #
                      # On RPi 4, you may choose pin 12, 14, or 18

refresh_interval = 5  # How often to check and update (recommended to be > 1.0 to reduce stress on CPU and fan)
```
Press `Ctrl-O; Enter` to save.

Press `Ctrl-X` to exit.

### Install
```bash
sudo bash install.sh
```
If you don't plan on uninstalling or editing any time soon, you may safely delete the source folder:
```bash
cd .. && rm -r rpi-pwm-fan-control
```

### Check service status
```bash
systemctl status rpi-pwm-fan-control
```

### Uninstall
```bash
sudo bash uninstall.sh
```
