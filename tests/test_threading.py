# purpose: test threading approach
import threading
import test_dynamic_plotting
import test_optimizing_BPM

bpm_recorder = threading.Thread(target = test_optimizing_BPM)
dynamic_plotter = threadin.Thread(target = test_dynamic_plotting)

