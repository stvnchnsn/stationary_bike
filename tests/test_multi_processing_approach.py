# class approach for dynamic plotting
import multiprocessing
import test_dynamic_plotting as plotter
import test_optmizing_BPM as BPM
import tests_rpm as RPM

BPM_proc = multiprocessing.Process(target = BPM.run_it)
plotter_proc = multiprocessing.Process(target = plotter.run_it)
RPM_proc = multiprocessing.Process(target = RPM.run_it)

BPM_proc.start()
RPM_proc.start()

plotter_proc.start()



### need to make dynamic plotter and bpm callable 
    