import RPi.GPIO as GPIO
import time
import subprocess
import re
import traceback
import sys

min_speed_temp = 40.0 # Temperature at which fan speed should be 0%
max_speed_temp = 60.0 # Temperature at which fan speed should be 100%

pwm_pin = 18          # PWM Pin
                      # Refer to your Pi pinout diagram and use `rpi-pin-test.py` to test pins
                      #
                      # E.g. python rpi-pin-test.py --pin 18 on
                      #
                      # On RPi 4, you may choose pin 12, 14, or 18

refresh_interval = 5  # How often to check and update (recommended to be > 1.0 to reduce stress on CPU and fan)

pwm_freq = 100

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, pwm_freq)
pwm.start(0)

def get_temp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    temp = float(file.read()) / 1000
    file.close()
    return(temp)

def get_speed_percent(temp):
    speed = 100 * (temp - min_speed_temp) / (max_speed_temp - min_speed_temp)
    return(min(max(0.0, speed), 100.0))

try:
    while 1:
        temp = get_temp()
        speed = get_speed_percent(temp)
        pwm.ChangeDutyCycle(speed)
#        print('\nTemp: %2.2f, Speed: %2.2f' % (temp, speed))
        time.sleep(refresh_interval)
except KeyboardInterrupt:
    pass
except:
    traceback.print_exc(limit=2, file=sys.stdout)
finally:
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    GPIO.cleanup()
