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
import itertools
# Logic that you write
#setup LEDs
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
#setup buttons
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#differentiate between increment and decrement buttons
incButton = 24
decButton = 23

#Logic for Part 3
#set LED pins to start off (LOW)
GPIO.output(17,GPIO.LOW)
GPIO.output(22,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
#Create counter
global counter
counter = 0
lst=list(itertools.product([0,1],repeat=3))
#Button assignment
def firstCallback(incButton):
    #Increment section of code
    global counter
    counter +=1
    if counter<0:
	counter+=8
    if counter==8:
	counter=0
    GPIO.output((17,27,22),lst[counter])
    time.sleep(.2)
    print ('Increase')
def secondCallback(decButton):
    #Decrement section of code
    global counter
    counter-=1
    if counter<0:
	counter+=8
    if counter==8:
	counter=0
    GPIO.output((17,27,22),lst[counter])
    time.sleep(.2)
    print ('Decrease')
#Interrupt and debounce section
GPIO.add_event_detect(23,GPIO.FALLING,callback=firstCallback,bouncetime=200)
GPIO.add_event_detect(24,GPIO.FALLING,callback=secondCallback,bouncetime=200)

def main():
   # print("write your logic here")
    #Part 1 - turn LED on then off
    # Turn LED on
#    GPIO.output(17,GPIO.HIGH)
#    time.sleep(3) #LED on for three seconds
    #Turn off LED
#    GPIO.output(17,GPIO.LOW)
#    time.sleep(2) #LED off for two seconds


    #Part 2 - toggle LED using a button
#    GPIO.output(17,False) #start off with LED off
#    try:
#	while True:
#		GPIO.output(17, not GPIO.input(23))
#		time.sleep(.1)
#    finally:
#	GPIO.output(17,False)



    #Part 3
    pass

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
