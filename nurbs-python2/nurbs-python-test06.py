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
P2DTS.datetimestamp_us("Starting:  nurbs-python-test06.py ==> Bismillah Hirrahma Nirrahim WRY.")

### =======================================================
### CODE BEGINS HERE

P2DTS.datetimestamp_us("This python code will display a 3D curve using BSpline in NURBS.")

# Importing NURBS module
## MPL means Matplotlib
import geomdl
import geomdl.NURBS   as NURBS
import geomdl.BSpline as BSpline
import geomdl.visualization.VisMPL as VisMPL

# Create the curve instance
crv = BSpline.Curve()

# Set degree
crv.degree = 2

# Set control points
crv.ctrlpts = [[1, 0, 0], [1, 1, 0], [0, 1, 0]]

# Set knot vector
crv.knotvector = [0, 0, 0, 1, 1, 1]

# Set the visualization component of the curve
crv.vis = VisMPL.VisCurve3D()

# Plot the curve
crv.render()

### CODE ENDS HERE
### =======================================================

### WE CALCULATE DURATION SINCE START-TIME. NO NEED TO CAPTURE END-TIME AND SENT TO THE MODULE. 
### THE DATE-TIME STAMP MODULE CAPTURES AUTOMATICALLY END-TIME FROM THE SYSTEM CLOCK AS IT EXECUTES.
P2DTS.datetimestamp_us("Completed: nurbs-python-test06.py ==> Alhamdulillah Hirrabil Alamin WRY.")
P2DTS.execution_duration(tstart1, "for the total running time of nurbs-python-test06.py")

### =======================================================
### ALHAMDULILLAH 3 TIMES WRY.
### =======================================================
'''
wruslan@HPEliteBk8470p-ubstudio-20:~/Documents$ python nurbs-python-test06.py 
2021-06-20 14:07:18.322005 ==>  Starting:  nurbs-python-test06.py ==> Bismillah Hirrahma Nirrahim WRY.
2021-06-20 14:07:18.322049 ==>  This python code will display a 3D curve using BSpline in NURBS.
2021-06-20 14:07:24.887682 ==>  Completed: nurbs-python-test06.py ==> Alhamdulillah Hirrabil Alamin WRY.
2021-06-20 14:07:24.887781 ==>  Duration: 6.565785 seconds execution for the total running time of nurbs-python-test06.py
wruslan@HPEliteBk8470p-ubstudio-20:~/Documents$ 
'''
