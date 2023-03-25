import RPi.GPIO as GPIO
import time
import subprocess
import re
import traceback
import sys

min_speed_temp = 40.0
max_speed_temp = 60.0

pwm_pin = 18
pwm_freq = 100

sleep_time = 5

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
        time.sleep(sleep_time)
except KeyboardInterrupt:
    pass
except:
    traceback.print_exc(limit=2, file=sys.stdout)
finally:
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    GPIO.cleanup()
