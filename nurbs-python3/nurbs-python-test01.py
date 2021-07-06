#! /usr/bin/env  python2

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
P3DTS.datetimestamp_us("Bismillah Hirrahma Nirrahim")
P3DTS.datetimestamp_us("Reference: https://nurbs-python.readthedocs.io/en/5.x/basics.html")
P3DTS.datetimestamp_us("Starting:  test01.py ==> example BSpline to a 3-dimensional curve.")

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
P3DTS.datetimestamp_us("Completed: test01.py ==> example BSpline to a 3-dimensional curve.")
P3DTS.datetimestamp_us("Alhamdulillah Hirrabil Alamin")
P3DTS.execution_duration(tstart1, "for the total running time.dxx")

### =======================================================
'''
wruslan@HPEliteBk8470p-ubstudio-20:~/github-tests/python-nurbs/python3$ python3 test01.py 
2021-06-20 01:46:28.205695 ==>  Bismillah Hirrahma Nirrahim
2021-06-20 01:46:28.205757 ==>  Reference: https://nurbs-python.readthedocs.io/en/5.x/basics.html
2021-06-20 01:46:28.205781 ==>  Starting:  test01.py ==> example BSpline to a 3-dimensional curve.
2021-06-20 01:46:28.299612 ==>  Completed: test01.py ==> example BSpline to a 3-dimensional curve.
2021-06-20 01:46:28.299658 ==>  Alhamdulillah Hirrabil Alamin
2021-06-20 01:46:28.299687 ==>  Duration: 0.093997 seconds execution for the total running time.dxx
wruslan@HPEliteBk8470p-ubstudio-20:~/github-tests/python-nurbs/python3$ 
'''
