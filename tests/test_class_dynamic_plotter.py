# class approach for dynamic plotting
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Dynamic_Plotter:
    def __init__(self,filename):
        self.filename = filename
        self.i = 3000
    def animate():
        try:
            data = np.genfromtxt(self.filename,delimiter = ',')
        except UserWarning genfromtxt:
            print('Data not available yet')

        t_values = data[:,0]
        bpm_1 = data[:,1]
        bpm_2 = data[:,2]
        plt.cla()
        plt.plot(t_values,bpm_1, label = "BPM_1")
        plt.plot(t_values,bpm_2,label = "BPM_2")
        plt.legend()
  
animate = Dynamic_Plotter('PMDFDSF')
animate = animate.animate
ani = FuncAnimation(plt.gcf(),animate, interval = 3000)
plt.tight_layout()
plt.show()