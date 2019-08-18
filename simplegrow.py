import RPi.GPIO as gp
import time
from datetime import datetime

### ENTER HERE THE TIMES YOU WISH THE SYSTEM WATER YOUR PLANT
TIMES_TO_WATER = ['14:50','14:55']
### ENTER HERE FOR HOW LONG THE PUMP SHOULD RUN PER WATERING (in seconds)
PUMP_WATERING_TIME = 15

# Pins used for water pump and humidity sensor
PUMP_PIN = 18

# Setting up the pins
gp.setmode(gp.BCM)
gp.setup(PUMP_PIN, gp.IN)

def watertime_to_datetime(watertime):
    water_hour = int(watertime.split(':')[0])
    water_minute = int(watertime.split(':')[1])
    now = datetime.now()
    return datetime(year=now.year, month=now.month,
     day=now.day, hour=water_hour, minute=water_minute)

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
    while(True):
        now = datetime.now()
        now_minute_precision = datetime(year=now.year,
        month=now.month, day=now.day, hour=now.hour, minute=now.minute)
        for watertime in TIMES_TO_WATER:
            wt = watertime_to_datetime(watertime)
            if now_minute_precision == wt:
                print(datetime.now(), 'Watering the plant!')
                run_pump(PUMP_WATERING_TIME)
        time.sleep(60)