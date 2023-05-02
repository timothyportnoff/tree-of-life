#############################################################################

#DEBUG
MOTOR_DEBUG         = 0
SONAR_DEBUG         = 0
AUDIO_DEBUG         = 0
LED_DEBUG           = 0
FANCY               = 0

#INPUTS
POTENTIOMMETER      = 0
START_BUTTON        = 0 
STOP_BUTTON         = 0
KNOB                = 0
IR                  = 0

#OUTPUTS
GPIO_TRIGGER_1      = 23
GPIO_ECHO_1         = 24
GPIO_TRIGGER_2      = 19
GPIO_ECHO_2         = 26
MOTOR_A_1           = 12
MOTOR_A_2           = 20
MOTOR_B_1           = 16
MOTOR_B_2           = 21
RELAY_IN_1          = 18

#LED'S
RED                 = 0
YELLOW              = 0
GREEN               = 0
BLUE                = 0

#############################################################################

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#SONAR
GPIO.setup(GPIO_TRIGGER_1,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO_1,GPIO.IN)      # Echo
GPIO.setup(GPIO_TRIGGER_2,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO_2,GPIO.IN)      # Echo

def setup():
    # Set pin states
    GPIO.setup(RELAY_IN_1, GPIO.OUT)
    GPIO.setup(MOTOR_A_1, GPIO.OUT)
    GPIO.setup(MOTOR_A_2, GPIO.OUT)
    GPIO.setup(MOTOR_B_1, GPIO.OUT)
    GPIO.setup(MOTOR_B_2, GPIO.OUT)

def destroy():
    GPIO.cleanup()
