
## IMPORTS FOR SYSTEM-DEFINED MODULES
## For python time stamp
import time
from datetime import datetime

## IMPORTS FOR USER-DEFINED MODULES
import sys
sys.path.insert(0, './py2modules')
import py2_datetimestamp as P2DTS

## CAPTURE THE START TIME TO CALCULATE THE EXECUTION DURATION LATER
tstart1 = datetime.now()
P2DTS.datetimestamp_us("Starting:  nurbs-python-test00.py ==> Bismillah Hirrahma Nirrahim WRY.")

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

## Before render() Please set the following variables before evaluation: ctrlpts,knotvector
## crv.render()

### CODE ENDS HERE
### =======================================================

### WE CALCULATE DURATION SINCE START-TIME. NO NEED TO CAPTURE END-TIME AND SENT TO THE MODULE. 
### THE DATE-TIME STAMP MODULE CAPTURES AUTOMATICALLY END-TIME FROM THE SYSTEM CLOCK AS IT EXECUTES.
P2DTS.datetimestamp_us("Completed: nurbs-python-test00.py ==> Alhamdulillah Hirrabil Alamin WRY.")
P2DTS.execution_duration(tstart1, "for the total running time of nurbs-python-test00.py")

### =======================================================
### ALHAMDULILLAH 3 TIMES WRY
### =======================================================
'''
wruslan@HPEliteBk8470p-ubstudio-20:~/Documents$ python nurbs-python-test00.py 
2021-06-20 15:50:35.237604 ==>  Starting:  nurbs-python-test00.py ==> Bismillah Hirrahma Nirrahim WRY.
2021-06-20 15:50:36.618595 ==>  Completed: nurbs-python-test00.py ==> Alhamdulillah Hirrabil Alamin WRY.
2021-06-20 15:50:36.618709 ==>  Duration: 1.381112 seconds execution for the total running time of nurbs-python-test00.py
wruslan@HPEliteBk8470p-ubstudio-20:~/Documents$ 
'''


