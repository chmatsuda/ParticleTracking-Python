import numpy as np
from trackmem import trackmem
import os

#added argument mt=None (so doesn't have to read file), also fovn is now optional
def ultimateimport():
    #importing the required modules
    import numpy as np #Numerical Python
    import scipy #Scientific Python

    %matplotlib inline

    import mpld3 #For making nice looking plots
    #If mpld3 is not available, install with conda (run "conda install mpld3" in Anaconda
    # command prompt)

    mpld3.enable_notebook()
    import matplotlib
    from matplotlib import pylab

    #For making interactive user interfaces (buttons and sliders and such)
    import ipywidgets as widgets
    from ipywidgets import Layout, interact, fixed

    #Loading the particle tracking software
    import sys
    ##MAC
    #sys.path.append("..//track") #Locate code
    ##PC
    sys.path.append("..\\track")
    import mpretrack #The file mpretrack.py and trackmem.py should be in the location above
    import trackmem
    import bpass
    import tiff_file #Ignore any warnings importing this may cause
    import pickle