#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Kea Nchodu
Student Number: NCHKEA001
Prac: Prac 1
Date: 28 July 2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
# Logic that you write
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

def main():
    print("write your logic here")
    #Part 1 - turn LED on then off
    # Turn LED on
    GPIO.output(17,GPIO.HIGH)
    time.sleep(3) #LED on for three seconds
    #Turn off LED
    GPIO.output(17,GPIO.LOW)
    time.sleep(2) #LED off for two seconds

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
