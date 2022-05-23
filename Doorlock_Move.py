import RPi.GPIO as GPIO

import time


def Doorlock():
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(18,GPIO.OUT)
<<<<<<< HEAD
    
    time.sleep(0.5)
    
    GPIO.output(18,False)
    
    print('open')
    
    time.sleep(2)
    
=======
    
    time.sleep(1)
    
    GPIO.output(18,False)
    
    print('open')
    
    time.sleep(3)
    
>>>>>>> 1bda1f936267f4a39530351f107806e16359a0c8
    GPIO.cleanup()
    
    print('cleanup')
    
    time.sleep(0.5)
Doorlock()