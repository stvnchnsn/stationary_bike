import RPi.GPIO as GPIO
import datetime as dt
from time import sleep
import time
import numpy as np
import matplotlib.pyplot as plt
import csv
from datetime import datetime as dt

sensorPin = 7
rest = 0.10
wheel_pedal_ratio = 2.75 # not sure what the gear ratio is exactly 

monkeybutts = ["time","RPM"]
filename = 'RPM_tests'
#filename = filename+'_'+dt.strftime(dt.now(),format = '%Y-%m-%d')+'_'+dt.strftime(dt.now(),format = '%s')[-5:]+'.csv'
with open(filename,'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file,fieldnames = monkeybutts)

with open(filename,'a') as csv_file:
    csv_writer = csv.DictWriter(csv_file,fieldnames = monkeybutts)
    info = {"time":0,
                "RPM":0}
    csv_writer.writerow(info)


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensorPin, GPIO.IN)

def loop3():
    first_hit = True
    t0_log = time.time() # t0 for plotting 
    rpm = 0 
    while True:
        wheel_rotations = 0
        collect_loop = True
        t0 = False
        timeout0 = time.time() # used to generate an rpm of 0 if no rotation detected after 2 seconds
        
        while collect_loop:
            if GPIO.input(sensorPin)==GPIO.LOW:
                if first_hit==True:
                    first_hit = False
                    t0 = time.time()  
                wheel_rotations +=1           
                sleep(rest)
                if wheel_rotations >= 2:
                    collect_loop = False
                    td=np.round(time.time() - t0,4)
                    timeout0 = time.time() 
                    rpm = np.round((1/(td*wheel_pedal_ratio))*60,1)
                    
                t0 = time.time()
            if (time.time() - timeout0 >2) & (wheel_rotations==0):
                rpm = 0
                sleep(rest)
                print('Sleeping at the wheel!?!')
                collect_loop = False
        with open(filename,'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file,fieldnames = monkeybutts)
            tx = np.round(time.time()-t0_log,3)
            info = {
                    "time":tx,
                    "RPM":rpm}
            csv_writer.writerow(info)
            print('RPM = ' ,rpm)
            print('Time = ',tx)

def destroy():
    GPIO.cleanup()

def run_it():
    print ('tests_rpm.py is starting...')
    setup()
    try:
        loop3()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

if __name__ == '__main__':     # Program entrance
    print ('tests_rpm.py is starting...')
    setup()
    try:
        loop3()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()