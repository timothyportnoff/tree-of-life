import time
#from time import sleep
import RPi.GPIO as GPIO
from config import *
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import gpiozero
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
gpiozero.Device.pin_factory=PiGPIOFactory('127.0.0.1')
servo = Servo(17)
 
def servin_time():
    servo.mid()
    sleep(0.5)
    servo.max()
    sleep(0.5)
 
# Function for step sequence
def setStep(w1, w2, w3, w4):
    GPIO.output(MOTOR_A_1, w1)
    GPIO.output(MOTOR_A_2, w2)
    GPIO.output(MOTOR_B_1, w3)
    GPIO.output(MOTOR_B_2, w4)

# Loop through step sequence based on number of steps
def clockwise(steps, delay):
    for i in range(0, steps):
        setStep(1,0,1,0)
        time.sleep(delay)
        setStep(0,1,1,0)
        time.sleep(delay)
        setStep(0,1,0,1)
        time.sleep(delay)
        setStep(1,0,0,1)
        time.sleep(delay)
    return

# Loop through step sequence based on number of steps
def cclockwise(steps,delay):
    for i in range(0, steps):
        setStep(1,0,0,1)
        time.sleep(delay)
        setStep(0,1,0,1)
        time.sleep(delay)
        setStep(0,1,1,0)
        time.sleep(delay)
        setStep(1,0,1,0)
        time.sleep(delay)
    return

def STARFINGER():   #MORA FUNCTION: 
    #VARIABLES TO ADJUST FOR-LOOP AND DELAYS RESPECTIVELY                 
    zzzzz = 0.09                    #Delay for in between clockwise function calls
    delay = 0.09                    #Delay for in between setStep function calls within clockwise function
    fov = 20                        #Step Ticks in this section if increased/decreased can cause weird jolting in the motor
    print('Running Motor')
    GPIO.output(RELAY_IN_1, False)  #RELAY SWITCH ON
    clockwise(fov, delay)
    cclockwise(fov, delay)
    clockwise(fov, delay)
    cclockwise(fov, delay)

    GPIO.output(RELAY_IN_1, True)   #RELAY SWITCH OFF
    print('Motor finished')
    #Mora's wonderful message
    #PORTNOFFFFFFF!!!!!!!
    #BL to STARFINGER TO RUN THE MOTOR
    #When Motor is done running it means it worked
    #BL to STARTFINGER whenever you need to use the motor
    #YOU CAN DELETE ANY PRINT STATEMENTS AFTER IMPLEMENTATION THEY ARE THERE FOR YOUR SAKE

if __name__ == '__main__':     # Program start from here
	setup()
	try:
            print("Testing STEPPER MOTOR")
            delay = 0.0028
            fov = 20
 
            clockwise(fov/2, delay)
            sleep(1)
            cclockwise(fov, delay)
            sleep(1)
            clockwise(fov, delay)
            sleep(1)
            cclockwise(fov, delay)
            sleep(1)
            clockwise(fov/2, delay)

	#except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		#destroy()
        except RuntimeError:
                # this gets thrown when control C gets pressed
                # because wait_for_edge doesn't properly pass this on
		destroy()
                #pass
