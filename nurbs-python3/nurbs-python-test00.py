
## IMPORTS FOR SYSTEM-DEFINED MODULES
## For python time stamp
import time
from datetime import datetime

## IMPORTS FOR USER-DEFINED MODULES
import sys
sys.path.insert(0, './py3modules')
import py3_datetimestamp as P3DTS

## CAPTURE THE START TIME TO CALCULATE THE EXECUTION DURATION LATER
tstart1 = datetime.now()
P3DTS.datetimestamp_us("Starting:  nurbs-python-test00.py ==> Bismillah Hirrahma Nirrahim WRY.")

### =======================================================
### CODE BEGINS HERE

# Importing NURBS module
import geomdl
import geomdl.NURBS as NURBS

# Importing visualization module
from geomdl.visualization import VisMPL as vis

# Creating a curve instance
crv = NURBS.Curve()

# Make a quadratic curve
crv.degree = 2

#######################################################
# Skipping control points and knot vector assignments #
#######################################################

# Set the visualization component and render the curve
crv.vis = vis.VisCurve3D()
## crv.render()

### CODE ENDS HERE
### =======================================================

### WE CALCULATE DURATION SINCE START-TIME. NO NEED TO CAPTURE END-TIME AND SENT TO THE MODULE. 
### THE DATE-TIME STAMP MODULE CAPTURES AUTOMATICALLY END-TIME FROM THE SYSTEM CLOCK AS IT EXECUTES.
P3DTS.datetimestamp_us("Completed: nurbs-python-test00.py ==> Alhamdulillah Hirrabil Alamin WRY.")
P3DTS.execution_duration(tstart1, "for the total running time of nurbs-python-test00.py")

### =======================================================
### ALHAMDULILLAH 3 TIMES WRY
### =======================================================
'''
wruslan@HPEliteBk8470p-ubstudio-20:~/Documents/2021-06-20-The-NURBS-Book/python-nurbs-basic01/nurbs-python3$ python3 nurbs-python-test00.py 
2021-06-20 16:08:20.245334 ==>  Starting:  nurbs-python-test00.py ==> Bismillah Hirrahma Nirrahim WRY.
/usr/lib/python3/dist-packages/mpl_toolkits/mplot3d/art3d.py:20: MatplotlibDeprecationWarning: 
The deprecated function was deprecated in Matplotlib 3.4 and will be removed two minor releases later.
  from . import proj3d
/usr/lib/python3/dist-packages/mpl_toolkits/mplot3d/axes3d.py:32: MatplotlibDeprecationWarning: 
The deprecated function was deprecated in Matplotlib 3.4 and will be removed two minor releases later.
  from . import art3d
/usr/lib/python3/dist-packages/mpl_toolkits/mplot3d/axes3d.py:34: MatplotlibDeprecationWarning: 
The deprecated function was deprecated in Matplotlib 3.4 and will be removed two minor releases later.
  from . import axis3d
Traceback (most recent call last):
  File "nurbs-python-test00.py", line 24, in <module>
    from geomdl.visualization import VisMPL as vis
  File "/usr/local/lib/python3.8/dist-packages/geomdl/visualization/VisMPL.py", line 14, in <module>
    import matplotlib.pyplot as plt
  File "/usr/local/lib/python3.8/dist-packages/matplotlib-3.4.2-py3.8-linux-x86_64.egg/matplotlib/pyplot.py", line 44, in <module>
    from matplotlib.figure import Figure, figaspect
  File "/usr/local/lib/python3.8/dist-packages/matplotlib-3.4.2-py3.8-linux-x86_64.egg/matplotlib/figure.py", line 24, in <module>
    from matplotlib import docstring, projections
  File "/usr/local/lib/python3.8/dist-packages/matplotlib-3.4.2-py3.8-linux-x86_64.egg/matplotlib/projections/__init__.py", line 4, in <module>
    from mpl_toolkits.mplot3d import Axes3D
  File "/usr/lib/python3/dist-packages/mpl_toolkits/mplot3d/__init__.py", line 1, in <module>
    from .axes3d import Axes3D
  File "/usr/lib/python3/dist-packages/mpl_toolkits/mplot3d/axes3d.py", line 42, in <module>
    class Axes3D(Axes):
  File "/usr/lib/python3/dist-packages/mpl_toolkits/mplot3d/axes3d.py", line 50, in Axes3D
    def __init__(
  File "/usr/local/lib/python3.8/dist-packages/matplotlib-3.4.2-py3.8-linux-x86_64.egg/matplotlib/docstring.py", line 40, in __call__
    func.__doc__ = inspect.cleandoc(func.__doc__) % self.params
KeyError: 'scale'
wruslan@HPEliteBk8470p-ubstudio-20:~/Documents/2021-06-20-The-NURBS-Book/python-nurbs-basic01/nurbs-python3$ 
'''
