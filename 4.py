import OPi.GPIO as GPIO
import time

# Установка номеров пинов GPIO для двигателей
motor1_pin1 = 10
motor1_pin2 = 11
motor2_pin1 = 12
motor2_pin2 = 13

# Настройка GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)

# Функция для поворота машинки влево
def turn_left():
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin2, GPIO.LOW)

# Функция для поворота машинки вправо
def turn_right():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.HIGH)

# Функция для остановки движения
def stop_movement():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.LOW)

try:
    turn_left()
    time.sleep(2)  # Поворот влево на 2 секунды
    turn_right()
    time.sleep(2)  # Поворот вправо на 2 секунды
    stop_movement()

except KeyboardInterrupt:
    stop_movement()
    GPIO.cleanup()
