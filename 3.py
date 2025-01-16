Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import OPi.GPIO as GPIO
... import time
... 
... # Установка номеров пинов GPIO для двигателей
... motor_pin1 = 10
... motor_pin2 = 11
... 
... # Настройка GPIO
... GPIO.setmode(GPIO.BOARD)
... GPIO.setup(motor_pin1, GPIO.OUT)
... GPIO.setup(motor_pin2, GPIO.OUT)
... 
... # Функция для движения машинки назад
... def move_backward():
...     GPIO.output(motor_pin1, GPIO.LOW)
...     GPIO.output(motor_pin2, GPIO.HIGH)
... 
... # Функция для остановки движения
... def stop_movement():
...     GPIO.output(motor_pin1, GPIO.LOW)
...     GPIO.output(motor_pin2, GPIO.LOW)
... 
... try:
...     move_backward()
...     time.sleep(2)  # Движение назад на 2 секунды
...     stop_movement()
... 
... except KeyboardInterrupt:
...     stop_movement()
