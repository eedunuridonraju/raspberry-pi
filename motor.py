import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
Motor1A=16
Motor1B=22
Motor1E=18

Motor2A=8
Motor2B=10
Motor2E=18

Motor3A=32
Motor3B=36
Motor3E=18

Motor4A=38
Motor4B=40
Motor4E=18

GPIO.setup(16,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)


while   True:
#frwd
	GPIO.output(16,GPIO.LOW)
	GPIO.output(22,GPIO.HIGH) 
	GPIO.output(18,GPIO.HIGH)
 
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH) 
        GPIO.output(18,GPIO.HIGH)
 
        GPIO.output(32,GPIO.LOW)
        GPIO.output(36,GPIO.HIGH) 
        GPIO.output(18,GPIO.HIGH)

        GPIO.output(38,GPIO.LOW)
        GPIO.output(40,GPIO.HIGH) 
        GPIO.output(18,GPIO.HIGH)
	sleep(10)
#backwrd
	GPIO.output(16,GPIO.HIGH)
	GPIO.output(22,GPIO.LOW)
	GPIO.output(18,GPIO.HIGH) 
        
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH) 

        GPIO.output(32,GPIO.HIGH)
        GPIO.output(36,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH) 

        GPIO.output(38,GPIO.HIGH)
        GPIO.output(40,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH) 
	sleep(10)      
	
#stop       
        GPIO.output(18,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
       
        GPIO.output(18,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)

        GPIO.output(18,GPIO.LOW)
        GPIO.output(32,GPIO.LOW)
        GPIO.output(36,GPIO.LOW)

        GPIO.output(18,GPIO.LOW)
        GPIO.output(38,GPIO.LOW)
        GPIO.output(40,GPIO.LOW)


        sleep(10)


#turning LEFT
        GPIO.output(16,GPIO.LOW)
        GPIO.output(22,GPIO.HIGH) 
        GPIO.output(18,GPIO.HIGH)
 
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW) 
        GPIO.output(18,GPIO.HIGH)
 
        GPIO.output(32,GPIO.LOW)
        GPIO.output(36,GPIO.HIGH) 
        GPIO.output(18,GPIO.HIGH)

        GPIO.output(38,GPIO.HIGH)
        GPIO.output(40,GPIO.LOW) 
        GPIO.output(18,GPIO.HIGH)
        sleep(10)
        
#turning right
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(22,GPIO.LOW) 
        GPIO.output(18,GPIO.HIGH)
 
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH) 
        GPIO.output(18,GPIO.HIGH)
 
        GPIO.output(32,GPIO.HIGH)
        GPIO.output(36,GPIO.LOW) 
        GPIO.output(18,GPIO.HIGH)

        GPIO.output(38,GPIO.LOW)
        GPIO.output(40,GPIO.HIGH) 
        GPIO.output(18,GPIO.HIGH)
        sleep(10)

        #stop       
        GPIO.output(18,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
       
        GPIO.output(18,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)

        GPIO.output(18,GPIO.LOW)
        GPIO.output(32,GPIO.LOW)
        GPIO.output(36,GPIO.LOW)

        GPIO.output(18,GPIO.LOW)
        GPIO.output(38,GPIO.LOW)
        GPIO.output(40,GPIO.LOW)


        sleep(15)


 
GPIO.cleanup()
