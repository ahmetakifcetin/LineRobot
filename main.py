import RPi.GPIO as GPIO
import time

sol_motor_ileri = 17
sol_motor_geri = 18
sag_motor_ileri = 27
sag_motor_geri = 22
sensor_sol = 23
sensor_sag = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(sol_motor_ileri, GPIO.OUT)
GPIO.setup(sol_motor_geri, GPIO.OUT)
GPIO.setup(sag_motor_ileri, GPIO.OUT)
GPIO.setup(sag_motor_geri, GPIO.OUT)
GPIO.setup(sensor_sol, GPIO.IN)
GPIO.setup(sensor_sag, GPIO.IN)

def ileri():
    GPIO.output(sol_motor_ileri, GPIO.HIGH)
    GPIO.output(sol_motor_geri, GPIO.LOW)
    GPIO.output(sag_motor_ileri, GPIO.HIGH)
    GPIO.output(sag_motor_geri, GPIO.LOW)

def geri():
    GPIO.output(sol_motor_ileri, GPIO.LOW)
    GPIO.output(sol_motor_geri, GPIO.HIGH)
    GPIO.output(sag_motor_ileri, GPIO.LOW)
    GPIO.output(sag_motor_geri, GPIO.HIGH)

def dur():
    GPIO.output(sol_motor_ileri, GPIO.LOW)
    GPIO.output(sol_motor_geri, GPIO.LOW)
    GPIO.output(sag_motor_ileri, GPIO.LOW)
    GPIO.output(sag_motor_geri, GPIO.LOW)

def sola_don():
    GPIO.output(sol_motor_ileri, GPIO.LOW)
    GPIO.output(sol_motor_geri, GPIO.HIGH)
    GPIO.output(sag_motor_ileri, GPIO.HIGH)
    GPIO.output(sag_motor_geri, GPIO.LOW)

def saga_don():
    GPIO.output(sol_motor_ileri, GPIO.HIGH)
    GPIO.output(sol_motor_geri, GPIO.LOW)
    GPIO.output(sag_motor_ileri, GPIO.LOW)
    GPIO.output(sag_motor_geri, GPIO.HIGH)

def hat_takip_et():
    while True:
        sol_sensor = GPIO.input(sensor_sol)
        sag_sensor = GPIO.input(sensor_sag)

        if sol_sensor == 0 and sag_sensor == 0:
            ileri()
        elif sol_sensor == 1 and sag_sensor == 0:
            sola_don()
        elif sol_sensor == 0 and sag_sensor == 1:
            saga_don()
        else:
            geri()

        time.sleep(0.1)

try:
    hat_takip_et()
except KeyboardInterrupt:
    dur()
    GPIO.cleanup()
