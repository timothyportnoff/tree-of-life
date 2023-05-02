import RPi.GPIO as GPIO
from config import *
import time
import random

SDI   = 16
RCLK  = 20
SRCLK = 21
BuzzerPin = 4

def setupLED():
    GPIO.setmode(GPIO.BCM)    # Number GPIOs by its BCM location
    GPIO.setup(SDI, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(RCLK, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(SRCLK, GPIO.OUT, initial=GPIO.LOW)
    
# Shift the data to 74HC595
def hc595_shift(dat):
    for bit in range(0, 8): 
        GPIO.output(SDI, 0x80 & (dat << bit))
        GPIO.output(SRCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.LOW)
    
def bright_burn(RED, GREEN, BLUE):
    sleeptime = 1        # Change speed, lower value, faster speed
    #while True:
    # Change LED status from mode
    if RED == "a" and BLUE == "a" and GREEN == "a":
        print ("TURNING ON ALL COLORS")
        hc595_shift(0xff)
        tune()
    elif RED == "a" and BLUE == "a" and GREEN != "a":
        print ("TURNING ON REDS AND BLUES")
        hc595_shift(REDS[0] + BLUES[0])
    elif RED == "a" and BLUE != "a" and GREEN == "a":
        print ("TURNING ON REDS AND GREENS")
        hc595_shift(REDS[0] + GREENS[0])
    elif RED != "a" and BLUE == "a" and GREEN == "a":
        print ("TURNING ON BLUES AND GREENS")
        hc595_shift(BLUES[0] + GREENS[0])
    elif RED == "a":
        print ("TURNING ON ALL REDS")
        hc595_shift(REDS[0])
    elif GREEN == "a":
        print ("TURNING ON ALL GREENS")
        hc595_shift(GREENS[0])
    elif BLUE == "a":
        print ("TURNING ON ALL BLUES")
        hc595_shift(BLUES[0])
    else:
        print ("TURNING OFF ALL COLORS")
        hc595_shift(0x00)
    time.sleep(sleeptime)
        
REDS = [0x09]
GREENS = [0x12]
BLUES = [0x24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BuzzerPin, GPIO.OUT) 
GPIO.setwarnings(False)

global Buzz 
Buzz = GPIO.PWM(BuzzerPin, 440) 
Buzz.start(50) 

P=1
C3=131
CS3=139
D3=147
DS3=156
E3=165
F3=175
FS3=185
G3=196
GS3=208
A3=220
AS3=233
B3=247
C4=262
CS4=277
D4=294
DS4=311
E4=330
F4=349
FS4=370
G4=392
GS4=415
A4=440
AS4=466
B4=494
C5=523
CS5=554
D5=587
DS5=622
E5=659
F5=698
FS5=740
G5=784
GS5=831
A5=880
AS5=932
B5=988

song = [
    P,
    
    D3, F3, A3,
    D3, F3, A3,
    D4, P, D4,
    A4, P, A4,
    E4, F4, E4,
    
    D4, F3, A3,
    D3, A4, C5,
    D5, C5,
    A4, B4, G4,
    A4, F3, A3,
    D3, F3, D5,
    
    D5, D5,
    C5, A4,
    A4, G4, F4,
    E4, E3, G3,
    C3, E3, G3,
    D4, A4,
    
    G4, F4,
    E4, D4, C4,
    D4,
    D4
    ]

song2 = [
    P,
    
    E4,
    G4, A4,
    B4, C5, B4,
    A4, FS4,
    D4, E4, FS4,
    G4, E4,
    E4, DS4, E4,
    FS4, DS4,
    
    B3, E4,
    G4, A4,
    B4, C5, B4,
    A4, FS4,
    D4, E4, FS4,
    G4, FS4, E4,
    DS4, CS4, DS4,
    E4, E4
    ]

beat = [
    1,
    1, 1, 1,
    1, 1, 1,
    2, 0.01, 1,
    2, 0.01, 1,
    1.5, 0.5, 1,
    
    1, 1, 1,
    1, 1, 1,
    2, 1,
    1, 1, 1,
    1, 1, 1,
    1, 1, 1,
    
    2, 1,
    2, 1,
    1, 1, 1,
    1, 1, 1,
    1, 1, 1,
    2, 1,
    
    2, 1,
    1, 1, 1,
    3,
    3
    ]

beat2 = [
    1,
    1,
    2, 1,
    1.5, 0.5, 1,
    2, 1,
    1.5, 0.5, 1,
    2, 1,
    1.5, 0.5, 1,
    2, 1,
    
    2, 1,
    2, 1,
    1.5, 0.5, 1,
    2, 1,
    1.5, 0.5, 1,
    1.5, 0.5, 1,
    1.5, 0.5, 1,
    2, 1,
    ]

def tune():
    theme = random.randint(1, 10)
    #print (theme) #debug
    if theme <= 5:
        for i in range(1, len(song)):
            Buzz.ChangeFrequency(song[i])
            time.sleep(beat[i]*0.38)
            Buzz.stop()
            time.sleep(0.01)
            Buzz.start(50)
        Buzz.stop()
    if theme >= 6:
        for i in range(1, len(song2)):
            Buzz.ChangeFrequency(song2[i])
            time.sleep(beat2[i]*0.38)
            Buzz.stop()
            time.sleep(0.01)
            Buzz.start(50)
        Buzz.stop()

#def main():
    #Buzz.stop()
    #while True:
        #print("These colors represent each sonar sensor. Please configure colors:\n")
        #RED = input("RED: ")
        #GREEN = input("\nGREEN: ")
        #BLUE = input("\nBLUE: ")
        
        #bright_burn(RED, GREEN, BLUE)
    
def destroy():
    Buzz.stop()
    GPIO.output(BuzzerPin, 0)
    GPIO.cleanup()

try:
    setup()
    #main()
except KeyboardInterrupt:     # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
