# Import required Python libraries
# -----------------------
from __future__ import print_function
import time
import RPi.GPIO as GPIO

# -----------------------
# Define some functions
# -----------------------
def measure_sonar1():
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER, True)
  # Wait 10us
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  
  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()
    
  elapsed = stop-start
  distance = (elapsed * speedSound)/2

  return distance


def measure_sonar2():
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER2, True)
  # Wait 10us
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER2, False)
  start = time.time()
  
  while GPIO.input(GPIO_ECHO2)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO2)==1:
    stop = time.time()

  elapsed = stop-start
  distance_sonar2 = (elapsed * speedSound)/2

  return distance_sonar2

def measure_average_sonar_1(): 
  # This function takes 3 measurements and
  # returns the average.

  distance1=measure_sonar1()
  time.sleep(0.01)
  distance2=measure_sonar1()
  time.sleep(0.01)
  distance3=measure_sonar1()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance

def measure_average_sonar_2(): 
  # This function takes 3 measurements and
  # returns the average.

  distance1=measure_sonar2()
  time.sleep(0.01)
  distance2=measure_sonar2()
  time.sleep(0.01)
  distance3=measure_sonar2()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance

def measure_average_sonar_3(): 
  # This function takes 3 measurements and
  # returns the average.

  distance1=measure_sonar2()
  time.sleep(0.01)
  distance2=measure_sonar2()
  time.sleep(0.01)
  distance3=measure_sonar2()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance
 
# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
#sonar1 (person detection)
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

#sonar2 (hand detection)
GPIO_TRIGGER2 = 17
GPIO_ECHO2 = 27

GPIO_TRIGGER3 = 2
GPIO_ECHO3 = 3

# Speed of sound in cm/s at temperature
temperature = 20
speedSound = 33100 + (0.6*temperature)

print("Ultrasonic Measurement")
print("Speed of sound is",speedSound/100,"m/s at ",temperature,"deg")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

GPIO.setup(GPIO_TRIGGER2,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO2,GPIO.IN)      # Echo

GPIO.setup(GPIO_TRIGGER3,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO3,GPIO.IN)      # Echo


# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

GPIO.output(GPIO_TRIGGER2, False)

GPIO.output(GPIO_TRIGGER3, False)
 
def sonar_1():
    min = 1000
    distance1 = measure_average_sonar_1()
    centimeters1 = distance1
    print("Distance : {0:5.1f}".format(distance1), "cm")
    if centimeters1 < min:
         min = centimeters1
    time.sleep(0.05)
    return distance1
    
def sonar_2():
    min = 1000
    distance2 = measure_average_sonar_2()
    centimeters2 = distance2
    print("Distance 2 : {0:5.1f}".format(distance2), "cm")
    if centimeters2 < min:
         min = centimeters2
    time.sleep(0.05)
    return distance2
    
def sonar_3():
    min = 1000
    distance3 = measure_average_sonar_3()
    centimeters3 = distance3
    print("Distance 3 : {0:5.1f}".format(distance3), "cm")
    if centimeters3 < min:
         min = centimeters3
    time.sleep(0.05)
    return distance3

def pain():
    while True:
        color1 = sonar_1()
        color2 = sonar_2()
        color3 = sonar_3()
