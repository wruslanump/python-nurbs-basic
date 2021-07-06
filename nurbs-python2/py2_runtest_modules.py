#! /usr/bin/env python
"""
File  : py2_runtest_modules.py 
Author: wruslandr@gmail.com

wruslan@HPEliteBk8470p-ubstudio-20:~$ date
Wed 16 Jun 2021 08:00:39 PM +08

wruslan@HPEliteBk8470p-ubstudio-20:~$ uname -a
Linux HPEliteBk8470p-ubstudio-20 5.10.25-rt35 
#3 SMP PREEMPT_RT Wed Apr 7 12:33:26 +08 2021 x86_64 x86_64 x86_64 GNU/Linux
 
wruslan@HPEliteBk8470p-ubstudio-20:~$ lsb_release -a
LSB Version:	core-11.1.0ubuntu2-noarch:security-11.1.0ubuntu2-noarch
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.2 LTS
Release:	20.04
Codename:	focal
wruslan@HPEliteBk8470p-ubstudio-20:~$ 

===========================================================
"""
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
P2DTS.datetimestamp_us("Starting:  py2_runtest_modules.py ==> Bismillah Hirrahma Nirrahim in python2.7")

### =======================================================
### CODE BEGINS HERE

P2DTS.datetimestamp_us("### BASIC SYSTEM PACKAGES")

P2DTS.datetimestamp_us("import ... sys")
import sys          #(Access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.)
P2DTS.datetimestamp_us("import ... os")
import os           #(Automatically perform many operating system tasks, creating and removing a directory (folder), fetching its contents, etc)
P2DTS.datetimestamp_us("import ... time")
import time         #(Provides many ways of representing time in code, such as objects, numbers, and strings.) 
P2DTS.datetimestamp_us("import ... datetime")
import datetime     #(Module supplies classes to work with date and time.)
P2DTS.datetimestamp_us("import ... dateutil")
import dateutil     #(Built-in datetime module which is used for manipulating dates and times from simple to complex ways.) 
P2DTS.datetimestamp_us("import ... errno")
import errno        #(Module defines a number of symbolic error codes, such as ENOENT 
P2DTS.datetimestamp_us("import ... psutil")
import psutil

P2DTS.datetimestamp_us("### MATHEMATICAL PACKAGES")

P2DTS.datetimestamp_us("import ... numpy")
import numpy           #(NumPy is the fundamental package for array computing with Python.)
P2DTS.datetimestamp_us("import ... scipy")
import scipy           #(SciPy: Scientific Library for Python)  
P2DTS.datetimestamp_us("import ... random")
import random          #(Python 2 random module.)
P2DTS.datetimestamp_us("import ... random2")
import random2         #(Python 3 compatible Python 2 random module.)
P2DTS.datetimestamp_us("import ... math")
import math            #(Module provides functions useful in number theory as well as in representation theory, a related field.)
P2DTS.datetimestamp_us("import ... cmath")
import cmath           #(Complex number is a combination of a real number and an imaginary number.) 
P2DTS.datetimestamp_us("import ... decimal")
import decimal         #(Decimal module for fast correctly-rounded decimal floating point arithmetic. The exactness carries over into arithmetic.)
P2DTS.datetimestamp_us("import ... fractions")
import fractions       #(Rational number arithmetic. Allows to create a Fraction instance from integers, floats, numbers, decimals and strings.) 
P2DTS.datetimestamp_us("import ... statistics")
import statistics      #(Python's statistics is a built-in Python library for descriptive statistics. Not too large numbers) 
P2DTS.datetimestamp_us("import ... string")
import string          #(Module contains a single utility function - capwords(s, sep=None). This function split the specified string into words using str.) 
P2DTS.datetimestamp_us("import ... StringIO")
import StringIO        #(An in-memory file-like object. Object can be used as input/output to most function that would expect a standard file object.
P2DTS.datetimestamp_us("import ... mpmath")
import mpmath          #(Python library for real and complex floating-point arithmetic with arbitrary precision)

P2DTS.datetimestamp_us("### EXECUTION AND PROCESSING PACKAGES")

P2DTS.datetimestamp_us("import ... mpi4py")
import mpi4py           #(Python bindings for the Message Passing Interface (MPI). API which grounds on the standard MPI-2 C++ bindings.)
P2DTS.datetimestamp_us("import ... threading")
import threading        #(Threading in python is used to run multiple threads (tasks, function calls) at the same time.)
P2DTS.datetimestamp_us("import ... multiprocessing")
import multiprocessing  #(Multiprocessing supports spawning processes using an API. Can fully leverage multiple processors on a given machine.)
P2DTS.datetimestamp_us("import ... concurrent")
import concurrent       #(Launching parallel tasks. )
P2DTS.datetimestamp_us("import ... trace")
import trace            #(Trace or track Python statement execution. It can be used in another program or from the command line.)
P2DTS.datetimestamp_us("import ... traceback")
import traceback        #(standard interface to extract, format and print stack traces of Python programs.) 
P2DTS.datetimestamp_us("import ... traceback2")
import traceback2       #(In Python 2.x, unlike traceback, traceback2 creates unicode output)

P2DTS.datetimestamp_us("import ... cython")
import cython       #(In Python 2.x, unlike traceback, traceback2 creates unicode output)

P2DTS.datetimestamp_us("### GRAPHICS PROCESSING PACKAGES")

P2DTS.datetimestamp_us("import ... matplotlib")
import matplotlib  #(Plotting library for Python and NumPy. Object-oriented API embedding plots using GUI toolkits Tkinter, wxPython, Qt, or GTK.)
P2DTS.datetimestamp_us("import ... matplotlib.pyplot")
import matplotlib.pyplot
P2DTS.datetimestamp_us("import ... pylab")
import pylab       #(Module that bulk imports matplotlib.pyplot (for plotting) and NumPy (for Mathematics) in a single name space.)

P2DTS.datetimestamp_us("import ... plotly")
import plotly      #(Plotting library)
P2DTS.datetimestamp_us("import ... plotlywidget")
import plotlywidget      #(Plotting library)
P2DTS.datetimestamp_us("import ... chart_studio")
import chart_studio      #(Plotting library)

P2DTS.datetimestamp_us("import ... geomdl")
import geomdl      #(Python-NURBS library)
P2DTS.datetimestamp_us("import ... Gnuplot")
import Gnuplot     #(Python package that interfaces to gnuplot. Can plot data on the fly as they are computed.)
P2DTS.datetimestamp_us("import ... PyGnuplot")
import PyGnuplot   #(PyGnuplot: Python wrapper for Gnuplot.)
P2DTS.datetimestamp_us("import ... pygnuplot")
import pygnuplot   #(Python wrapper for Gnuplot.) 
P2DTS.datetimestamp_us("import ... graphviz")
import graphviz    #(Graphviz module used to create graph objects which can be completed using different nodes and edges.)
P2DTS.datetimestamp_us("import ... PyPDF2")
import PyPDF2      #(Python program to dynamically generate a graph, digraph in Graphviz's Dot.)
P2DTS.datetimestamp_us("import ... pydot")
import pydot       #(pydot.PyPI - Python interface to Graphviz's Dot.)
P2DTS.datetimestamp_us("import ... pydotplus")
import pydotplus   #(PyDotPlus is an improved version of the old pydot project.)
P2DTS.datetimestamp_us("import ... tkinter")
import tkinter     #(Tkinter is the de facto way in Python to create Graphical User interfaces - GUIs) 
P2DTS.datetimestamp_us("import ... PyQt4")
import PyQt4       #(PyQt4 is a comprehensive set of Python bindings for Digia's Qt cross platform GUI toolkit.) 
P2DTS.datetimestamp_us("import ... PyQt5")
import PyQt5       #(PyQt5 is a comprehensive set of Python bindings for Qt v5. It is implemented as more than 35 extension modules)

P2DTS.datetimestamp_us("### FILE PROCESSING PACKAGES")

P2DTS.datetimestamp_us("import ... io")
import io          #(Python io module allows us to manage the file-related input and output operations. Can write to Unicode data)
P2DTS.datetimestamp_us("import ... fileinput")
import fileinput   #(Module can iterate over lines from multiple input streams, write a loop over standard input or a list of files, etc)
P2DTS.datetimestamp_us("import ... difflib")
import difflib     #(Module provides classes and functions for comparing sequences. Can be used for comparing files, file differences, etc) 
P2DTS.datetimestamp_us("import ... filecmp")
import filecmp     #(Module defines functions to compare files and directories, with various optional time/correctness trade-offs.)
P2DTS.datetimestamp_us("import ... FileDialog")
import FileDialog  #(File selection dialogs. The tkinter.filedialog module provides classes for creating file/directory selection windows).

P2DTS.datetimestamp_us("### DATA PROCESSING PACKAGES")

P2DTS.datetimestamp_us("import ... h5py")
import h5py        #(H5PY package is a Pythonic interface to the HDF5 binary data format. For example: Scilab/Octave data outputs/inputs)
P2DTS.datetimestamp_us("import ... h5pyViewer")
import h5pyViewer  #(Python library viewer for large numeric data frames in HDF5.)
P2DTS.datetimestamp_us("import ... hdf5storage")
import hdf5storage #(Utilities to read/write Python types to/from HDF5 files, including MATLAB v7.3 MAT files.)
P2DTS.datetimestamp_us("import ... csv")
import csv         #(Comma Separated Values - most common import and export format for spreadsheets and databases.)
P2DTS.datetimestamp_us("import ... pandas")
import pandas      #(Python Data Analysis - imports data various file formats like comma-separated values, JSON, SQL, Microsoft Excel.)
P2DTS.datetimestamp_us("import ... seaborn")
import seaborn     #(Python Data Visualization - attractive and informative statistical graphics, Matplotlib-based.)

### CODE ENDS HERE

### WE CALCULATE DURATION SINCE START-TIME. NO NEED TO CAPTURE END-TIME AND SENT TO THE MODULE. 
### THE DATE-TIME STAMP MODULE CAPTURES AUTOMATICALLY END-TIME FROM THE SYSTEM CLOCK AS IT EXECUTES.
P2DTS.datetimestamp_us("Completed: py2_runtest_modules.py ==> Alhamdulillah Hirrabil Alamin in python2.7")
P2DTS.execution_duration(tstart1, "for the total running time of py2_runtest_modules.py")

"""
===========================================================
ALHAMDULILLAH 3 TIMES.
===========================================================
wruslan@HPEliteBk8470p-ubstudio-20:~/Documents/2021-06-19-The-NURBS-Book/python-nurbs-basic01/nurbs-python2$ python  py2_runtest_modules.py 
2021-06-20 13:21:24.352538 ==>  Starting:  py2_runtest_modules.py ==> Bismillah Hirrahma Nirrahim in python2.7
2021-06-20 13:21:24.352602 ==>  ### BASIC SYSTEM PACKAGES
2021-06-20 13:21:24.352636 ==>  import ... sys
2021-06-20 13:21:24.352672 ==>  import ... os
2021-06-20 13:21:24.352703 ==>  import ... time
2021-06-20 13:21:24.352728 ==>  import ... datetime
2021-06-20 13:21:24.352753 ==>  import ... dateutil
2021-06-20 13:21:24.353426 ==>  import ... errno
2021-06-20 13:21:24.353449 ==>  ### MATHEMATICAL PACKAGES
2021-06-20 13:21:24.353468 ==>  import ... numpy
2021-06-20 13:21:24.468714 ==>  import ... scipy
2021-06-20 13:21:24.474386 ==>  import ... random
2021-06-20 13:21:24.474428 ==>  import ... random2
2021-06-20 13:21:24.475167 ==>  import ... math
2021-06-20 13:21:24.475194 ==>  import ... cmath
2021-06-20 13:21:24.475258 ==>  import ... decimal
2021-06-20 13:21:24.475287 ==>  import ... fractions
2021-06-20 13:21:24.478381 ==>  import ... statistics
2021-06-20 13:21:24.479062 ==>  import ... string
2021-06-20 13:21:24.479125 ==>  import ... StringIO
2021-06-20 13:21:24.479167 ==>  import ... mpmath
2021-06-20 13:21:24.508806 ==>  ### EXECUTION AND PROCESSING PACKAGES
2021-06-20 13:21:24.508892 ==>  import ... psutil
2021-06-20 13:21:24.540797 ==>  import ... mpi4py
2021-06-20 13:21:24.541169 ==>  import ... threading
2021-06-20 13:21:24.541219 ==>  import ... multiprocessing
2021-06-20 13:21:24.543900 ==>  import ... concurrent
2021-06-20 13:21:24.546284 ==>  import ... trace
2021-06-20 13:21:24.562764 ==>  import ... traceback
2021-06-20 13:21:24.562829 ==>  import ... traceback2
2021-06-20 13:21:24.577789 ==>  ### GRAPHICS PROCESSING PACKAGES
2021-06-20 13:21:24.577879 ==>  import ... matplotlib
2021-06-20 13:21:24.678941 ==>  import ... matplotlib.pyplot
2021-06-20 13:21:25.437779 ==>  import ... pylab
2021-06-20 13:21:25.443566 ==>  import ... plotly
2021-06-20 13:21:25.721262 ==>  import ... geomdl
2021-06-20 13:21:25.722586 ==>  import ... Gnuplot
2021-06-20 13:21:25.724401 ==>  import ... PyGnuplot
2021-06-20 13:21:25.735394 ==>  import ... pygnuplot
2021-06-20 13:21:25.736237 ==>  import ... graphviz
2021-06-20 13:21:25.743858 ==>  import ... PyPDF2
2021-06-20 13:21:25.754126 ==>  import ... pydot
2021-06-20 13:21:25.758088 ==>  import ... pydotplus
2021-06-20 13:21:25.760550 ==>  import ... tkinter
2021-06-20 13:21:25.761209 ==>  import ... PyQt4
2021-06-20 13:21:25.761851 ==>  import ... PyQt5
2021-06-20 13:21:25.762461 ==>  ### FILE PROCESSING PACKAGES
2021-06-20 13:21:25.762487 ==>  import ... io
2021-06-20 13:21:25.762517 ==>  import ... fileinput
2021-06-20 13:21:25.765186 ==>  import ... difflib
2021-06-20 13:21:25.765256 ==>  import ... filecmp
2021-06-20 13:21:25.766657 ==>  import ... FileDialog
2021-06-20 13:21:25.766690 ==>  ### DATA PROCESSING PACKAGES
2021-06-20 13:21:25.766714 ==>  import ... h5py
2021-06-20 13:21:25.803255 ==>  import ... h5pyViewer
2021-06-20 13:21:25.803510 ==>  import ... hdf5storage
2021-06-20 13:21:26.045136 ==>  import ... csv
2021-06-20 13:21:26.045214 ==>  import ... pandas
2021-06-20 13:21:26.858619 ==>  import ... seaborn
2021-06-20 13:21:27.732705 ==>  Completed: py2_runtest_modules.py ==> Alhamdulillah Hirrabil Alamin in python2.7
2021-06-20 13:21:27.732761 ==>  Duration: 3.380234 seconds execution for the total running time of py2_runtest_modules.py
wruslan@HPEliteBk8470p-ubstudio-20:~/Documents/2021-06-19-The-NURBS-Book/python-nurbs-basic01/nurbs-python2$ 

"""

