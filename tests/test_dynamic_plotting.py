import RPi.GPIO as GPIO
import datetime as dt
from time import sleep
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd


def animate(i):
    try:
        bpm_data = np.genfromtxt('BPM_tests',delimiter = ',')
        t_values = bpm_data[:,0]
        bpm_1 = bpm_data[:,1]
        bpm_2 = bpm_data[:,2]
    except UserWarning:
        print('No BPM data?')
    try:
        rpm_data = np.genfromtxt('RPM_tests',delimiter = ',')
        t_rpm = rpm_data[:,0]
        rpm = rpm_data[:,1]
    except UserWarning:
        print('No RPM data?')
    plt.cla() # clear current axis
    plt.plot(t_values,bpm_1, label = "BPM_1")
    plt.plot(t_values,bpm_2,label = "BPM_2")
    plt.plot(t_rpm,rpm,label = 'RPM')
    plt.legend()

def animate_subplot(i):
    try:
        bpm_data = np.genfromtxt('BPM_tests',delimiter = ',')
    except UserWarning:
        print('No BPM data?')
    t_bpm = bpm_data[:,0]
    bpm_1 = bpm_data[:,1]
    bpm_2 = bpm_data[:,2]
    try:
        rpm_data = np.genfromtxt('RPM_tests',delimiter = ',')
    except UserWarning:
        print('No RPM data?')
    t_rpm = rpm_data[:,0]
    rpm = rpm_data[:,1]
    plt.cla()
    f, (axis) = plt.subplots(ncols = 2,nrows = 1)
    axis[0].plot(t_bpm,bpm_1, label = 'BPM_Single')
    axis[0].plot(t_bpm,bpm_2, label = 'BPM_Average')
    axis[1].plot(t_rpm,rpm, label = 'RPM')
    
    
def run_it():
    print ('test_dynamic_plotting.py Starting...')
    sleep(10)
    try:
        print('Plotting')
        ani = FuncAnimation(plt.gcf(),animate, interval = 1000)
        plt.tight_layout()
        plt.show()
        #animate(3000)
    except IndexError:
        print('No data?')
        plt.close()
        run_it()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        plt.close()
            
        

if __name__ == '__main__':     # Program entrance
    run_it()