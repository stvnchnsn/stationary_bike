import RPi.GPIO as GPIO
import datetime as dt
from time import sleep
import time
import numpy as np
import csv
from datetime import datetime as dt

sensorPin = 31

monkeybutts = ["time","BPM_1","BPM_2"]
filename = 'BPM_tests'
#filename = filename+'_'+dt.strftime(dt.now(),format = '%Y-%m-%d')+'_'+dt.strftime(dt.now(),format = '%s')[-5:]+'.csv'
with open(filename,'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file,fieldnames = monkeybutts)


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensorPin, GPIO.IN)

check_interval = 3

def loop3():
    num_of_loops = 0
    t0_log = time.time() # t0 for plotting 
    while True:
        t0_multi = time.time() #t0 for the collect_loop count
        t0_single = False# t0 for single beat counter
        td_interval = False # dummy for multibeat counter
        beat_count = 0
        collect_loop = True
        single_beats = []
        while collect_loop:
            
            if GPIO.input(sensorPin)==GPIO.HIGH: # beat detect
                beat_count+=1
                tf_single=np.round(time.time() - t0_single,3)
                t0_single = time.time()
                sleep(0.10)
                t0_single = time.time()
                td_interval = np.round(time.time() - t0_multi,2)
                BPM_single = np.round(60/tf_single,2)
                single_beats.append(BPM_single)
                #print('BPM based on single beat = ',BPM_single)
             
            if  td_interval >= check_interval:
                collect_loop = False
                bpm = np.round((beat_count*60/td_interval),1)
                #print('BPM = ', bpm)
                #print('beat_count = ',beat_count)
                #print('td = ',td)
        with open(filename,'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file,fieldnames = monkeybutts)
            info = {
                "time":np.round(time.time()-t0_log,3),
                "BPM_1":BPM_single,
                "BPM_2":bpm}
            csv_writer.writerow(info)
            print(np.round(time.time()-t0_log,3))
            print('bpm single = ', BPM_single)
            print('bpm multiple = ',bpm)
            
        num_of_loops +=1
        

def run_it():
    print ('test_optmizing_BPM.py Starting...')
    setup()
    try:
        loop3()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()



def destroy():
    GPIO.cleanup()

if __name__ == '__main__':     # Program entrance
    print ('test_optmizing_BPM.py Starting...')
    setup()
    try:
        loop3()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()