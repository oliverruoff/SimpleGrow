import RPi.GPIO as gp
import time
from datetime import datetime

# Pins used for water pump and humidity sensor
PUMP_PIN = 18

# Setting up the pins
gp.setmode(gp.BCM)
gp.setup(PUMP_PIN, gp.IN)

def run_pump(pump_time):
    '''Activating the water pump for `PUMP_TIME` seconds.
    '''
    # Activating pump (HIGH / LOW is not enough for 5v relays)
    gp.setup(PUMP_PIN, gp.OUT)
    gp.output(PUMP_PIN, gp.HIGH)
    # Waiting for water to flow
    time.sleep(pump_time)
    # Deactivating pump
    gp.setup(PUMP_PIN, gp.IN)

if __name__ == '__main__':
    run_pump(5)