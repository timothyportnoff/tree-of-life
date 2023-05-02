#Python libs
import RPi.GPIO as GPIO
import threading
import os
from time import sleep
from config import *
from led import * 
from sonar import *
from motor import * 
from lara import * 

i = 0
try:
    if __name__ == "__main__":
        mode = LED0 # Change Mode, modes from LED0 to LED3
        sleeptime = 1        # Change speed, lower value, faster speed
        blink_sleeptime = 3
        RED = 0
        GREEN = 0
        BLUE = 0
        #Welcome, and setup
        setup()

        #Main Loop:
        while True:
            #Check distances
            distance1 = sonar_1()#measure_average(GPIO_TRIGGER_1, GPIO_ECHO_1) #check distance
            distance2 = sonar_2()#measure_average(GPIO_TRIGGER_2, GPIO_ECHO_2) #check distance
            distance3 = sonar_3()#measure_average(GPIO_TRIGGER_3, GPIO_ECHO_3) #check distance
            if distance1 < 20: RED = 1
            else: RED = 0
            if distance1 < 20: BLUE = 1
            else: BLUE = 0
            if distance1 < 20: GREEN = 1
            else: GREEN = 0

            # Change LED status from mode
            if RED:
                print ("TURNING ON ALL REDS")
                hc595_shift(REDS[0])
                RED = 0
                GREEN = 1
                time.sleep(sleeptime)
            if GREEN:
                print ("TURNING ON ALL GREENS")
                hc595_shift(GREENS[0])
                GREEN = 0
                BLUE = 1
                time.sleep(sleeptime)
            if BLUE:
                print ("TURNING ON ALL BLUES")
                hc595_shift(BLUES[0])
                BLUE = 1
                GREEN = 1
                time.sleep(sleeptime)
            if RED and BLUE and GREEN:
                print ("TURNING ON ALL COLORS")
                hc595_shift(0xff)
                time.sleep(sleeptime)
                RED = 0
                BLUE = 0
                GREEN = 0
                STARFINGER()
            sleep(0.1) #Sleep at the end of the loop. This is a magic number, please adjust.
            #End loop

#Exit cleanly after a keyboard interrupt
except KeyboardInterrupt:
    #Return to center
    destroy()
