import OPi.GPIO as GPIO
from time import sleep
import time
GPIO.setboard(GPIO.ZEROPLUS2H5)
GPIO.setmode(GPIO.BOARD)
speed1 = 20
speed2 = 30
# Настройка GPIO
delay_time = 0.03
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
pwmOutput_0 = GPIO.PWM(7, speed1)
pwmOutput_0.start(0)
GPIO.output(11, 1)

GPIO.setup(15, GPIO.OUT)
pwmOutput_1 = GPIO.PWM(15, speed2)
pwmOutput_1.start(0)

GPIO.output(13, 1)
# Функция для движения машинки вперёд с ускорением
for dutyCycle in range (0, speed1, 1):
	pwmOutput_0.ChangeDutyCycle (dutyCycle)
	pwmOutput_1.ChangeDutyCycle (dutyCycle + 1)
	sleep(delay_time)
	
pwmOutput_0.ChangeDutyCycle (speed1)
pwmOutput_1.ChangeDutyCycle (speed2)
sleep(10)
pwmOutput_0.stop()
pwmOutput_1.stop()
GPIO.cleanup()


