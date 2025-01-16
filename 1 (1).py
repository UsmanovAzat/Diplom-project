import OPi.GPIO as GPIO
from time import sleep
import time
GPIO.setboard(GPIO.ZEROPLUS2H5)
GPIO.setmode(GPIO.BOARD)
# Настройка GPIO
delay_time = 0.1
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
pwmOutput_0 = GPIO.PWM(7, 20)
pwmOutput_0.start(0)
GPIO.output(11, 1)

GPIO.setup(15, GPIO.OUT)
pwmOutput_1 = GPIO.PWM(15, 20)
pwmOutput_1.start(0)
# Функция для движения машинки вперёд на 10 сек
try:
	while True:
		for dutyCycle in range (0, 20, 1):
			pwmOutput_0.ChangeDutyCycle (dutyCycle)
			sleep(delay_time)

except KeyboardInterrupt:
	pwmOutput_0.ChangeDutyCycle (20)
	sleep(5)
	pwmOutput_0.stop()
	GPIO.cleanup()

try:
	while True:
		for dutyCycle1 in range (0, 20, 1):
			pwmOutput_1.ChangeDutyCycle (dutyCycle1)
			sleep(delay_time)

except KeyboardInterrupt:
	pwmOutput_1.ChangeDutyCycle (20)
	sleep(5)
	pwmOutput_1.stop()
	GPIO.cleanup()
