import RPi.GPIO as GPIO
import sys

pin = 18
pin_state = 1

def show_help():
    print("Usage:")
    print("    python rpi-pin-test.py [options] [on|off]")
    print("")
    print("Options:")
    print("    -p, --pin <pin number>   Set pin number")
    print("    -h, --help               Show this help page")

arg_c = 1
while arg_c < len(sys.argv):
    if sys.argv[arg_c] == "-h" or sys.argv[arg_c] == "--help":
        show_help()
        exit()
    elif sys.argv[arg_c] == "-p" or sys.argv[arg_c] == "--pin":
        arg_c += 1
        if arg_c < len(sys.argv):
            pin = int(sys.argv[arg_c])
    elif sys.argv[arg_c] == "on":
        pin_state = 1
    elif sys.argv[arg_c] == "off":
        pin_state = 0
    else:
        print("Unexpected argument: %s" % sys.argv[arg_c])
        print("")
        show_help()
        exit()
    arg_c += 1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, pin_state)
