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
P2DTS.datetimestamp_us("Bismillah Hirrahma Nirrahim")
P2DTS.datetimestamp_us("Reference: https://nurbs-python.readthedocs.io/en/5.x/basics.html")
P2DTS.datetimestamp_us("Starting:  test01.py ==> example BSpline to a 3-dimensional curve.")

### =======================================================
### CODE BEGINS HERE

# Importing NURBS module
from geomdl import BSpline

# Create the curve instance
crv = BSpline.Curve()

# Set degree
crv.degree = 2

# Set control points
crv.ctrlpts = [[1, 0, 0], [1, 1, 0], [0, 1, 0]]

# Set knot vector
crv.knotvector = [0, 0, 0, 1, 1, 1]

### CODE ENDS HERE
### =======================================================
### WE CALCULATE DURATION SINCE START-TIME. NO NEED TO CAPTURE END-TIME AND SENT TO THE MODULE. 
### THE DATE-TIME STAMP MODULE CAPTURES AUTOMATICALLY END-TIME FROM THE SYSTEM CLOCK AS IT EXECUTES.
P2DTS.datetimestamp_us("Completed: test01.py ==> example BSpline to a 3-dimensional curve.")
P2DTS.datetimestamp_us("Alhamdulillah Hirrabil Alamin")
P2DTS.execution_duration(tstart1, "for the total running time.dxx")

### =======================================================
'''
wruslan@HPEliteBk8470p-ubstudio-20:~/github-tests/python-nurbs/python2$ python test01.py 
2021-06-20 01:37:13.494045 ==>  Bismillah Hirrahma Nirrahim
2021-06-20 01:37:13.494089 ==>  Reference: https://nurbs-python.readthedocs.io/en/5.x/basics.html
2021-06-20 01:37:13.494118 ==>  Starting:  test01.py ==> example BSpline to a 3-dimensional curve.
2021-06-20 01:37:13.566363 ==>  Completed: test01.py ==> example BSpline to a 3-dimensional curve.
2021-06-20 01:37:13.566451 ==>  Alhamdulillah Hirrabil Alamin
2021-06-20 01:37:13.566524 ==>  Duration: 0.072487 seconds execution for the total running time of test01.py
wruslan@HPEliteBk8470p-ubstudio-20:~/github-tests/python-nurbs/python2$ 
'''


