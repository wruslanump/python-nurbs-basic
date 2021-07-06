#! /usr/bin/env python3
"""
File  : py3_runtest_modules.py 
Author: wruslandr@gmail.com

wruslan@HPEliteBk8470p-ubstudio-20:~$ date
Wed 16 Jun 2021 11:19:35 PM +08

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
sys.path.insert(0, './py3modules')
import py3_datetimestamp as P3DTS

## CAPTURE THE START TIME TO CALCULATE THE EXECUTION DURATION LATER
tstart1 = datetime.now()
P3DTS.datetimestamp_us("Starting:  py3_runtest_modules.py ==> Bismillah Hirrahma Nirrahim")

### =======================================================
### CODE BEGINS HERE

P3DTS.datetimestamp_us("### BASIC SYSTEM PACKAGES")

P3DTS.datetimestamp_us("import ... sys")
import sys          #(Access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.)
P3DTS.datetimestamp_us("import ... os")
import os           #(Automatically perform many operating system tasks, creating and removing a directory (folder), fetching its contents, etc)
P3DTS.datetimestamp_us("import ... time")
import time         #(Provides many ways of representing time in code, such as objects, numbers, and strings.) 
P3DTS.datetimestamp_us("import ... datetime")
import datetime     #(Module supplies classes to work with date and time.)
P3DTS.datetimestamp_us("import ... dateutil")
import dateutil     #(Built-in datetime module which is used for manipulating dates and times from simple to complex ways.) 
P3DTS.datetimestamp_us("import ... errno")
import errno        #(Module defines a number of symbolic error codes, such as ENOENT 
P3DTS.datetimestamp_us("import ... psutil")
import psutil

P3DTS.datetimestamp_us("### MATHEMATICAL PACKAGES")

P3DTS.datetimestamp_us("import ... numpy")
import numpy           #(NumPy is the fundamental package for array computing with Python.)
P3DTS.datetimestamp_us("import ... scipy")
import scipy           #(SciPy: Scientific Library for Python)  
P3DTS.datetimestamp_us("import ... random")
import random          #(Python 2 random module.)
P3DTS.datetimestamp_us("import ... random2")
import random2         #(Python 3 compatible Python 2 random module.)
P3DTS.datetimestamp_us("import ... math")
import math            #(Module provides functions useful in number theory as well as in representation theory, a related field.)
P3DTS.datetimestamp_us("import ... cmath")
import cmath           #(Complex number is a combination of a real number and an imaginary number.) 
P3DTS.datetimestamp_us("import ... fractions")
import fractions       #(Rational number arithmetic. Allows to create a Fraction instance from integers, floats, numbers, decimals and strings.) 
P3DTS.datetimestamp_us("import ... statistics")
import statistics      #(Python's statistics is a built-in Python library for descriptive statistics. Not too large numbers) 
P3DTS.datetimestamp_us("import ... io")
import io              #(Python io module allows us to manage the file-related input and output operations. Can write to Unicode data)
P3DTS.datetimestamp_us("import ... string")
import string          #(Module contains a single utility function - capwords(s, sep=None). This function split the specified string into words using str.) 
P3DTS.datetimestamp_us("import ... from io import StringIO")
from io import StringIO        #(An in-memory file-like object. Object can be used as input/output to most function that would expect a standard file object.
P3DTS.datetimestamp_us("import ... mpmath")
import mpmath          #(Python library for real and complex floating-point arithmetic with arbitrary precision)

P3DTS.datetimestamp_us("### EXECUTION AND PROCESSING PACKAGES")

P3DTS.datetimestamp_us("import ... mpi4py")
import mpi4py           #(Python bindings for the Message Passing Interface (MPI). API which grounds on the standard MPI-2 C++ bindings.)
P3DTS.datetimestamp_us("import ... threading")
import threading        #(Threading in python is used to run multiple threads (tasks, function calls) at the same time.)
P3DTS.datetimestamp_us("import ... multiprocessing")
import multiprocessing  #(Multiprocessing supports spawning processes using an API. Can fully leverage multiple processors on a given machine.)
P3DTS.datetimestamp_us("import ... concurrent")
import concurrent       #(Launching parallel tasks. )
P3DTS.datetimestamp_us("import ... trace")
import trace            #(Trace or track Python statement execution. It can be used in another program or from the command line.)
P3DTS.datetimestamp_us("import ... traceback")
import traceback        #(standard interface to extract, format and print stack traces of Python programs.) 
P3DTS.datetimestamp_us("import ... Concurrent_AP")
import Concurrent_AP    #(An implementation of asynchronous multiprocessing with progress logging.)
P3DTS.datetimestamp_us("import ... parallel_transform")
import parallel_transform  #(standard interface to extract, format and print stack traces of Python programs.) 
P3DTS.datetimestamp_us("import ... pytest_parallel")
import pytest_parallel     #(A pytest plugin for parallel and concurrent testing)

P3DTS.datetimestamp_us("import ... cython")
import cython     #(The C-interface for python)


P3DTS.datetimestamp_us("### GRAPHICS PROCESSING PACKAGES")

P3DTS.datetimestamp_us("import ... geomdl")
import geomdl      #(Python NURBS library)
P3DTS.datetimestamp_us("import ... plotly")
import plotly      #(Plotting Library)

P3DTS.datetimestamp_us("import ... plotlywidget")
import plotlywidget      #(Plotting Library)

P3DTS.datetimestamp_us("import ... chart_studio")
import chart_studio      #(Plotting Library)

P3DTS.datetimestamp_us("import ... matplotlib")
import matplotlib  #(Plotting library for Python and NumPy. Object-oriented API embedding plots using GUI toolkits Tkinter, wxPython, Qt, or GTK.)
P3DTS.datetimestamp_us("import ... matplotlib.pyplot")
import matplotlib.pyplot
P3DTS.datetimestamp_us("import ... pylab")
import pylab       #(Module that bulk imports matplotlib.pyplot (for plotting) and NumPy (for Mathematics) in a single name space.)
P3DTS.datetimestamp_us("import ... PyGnuplot")
import PyGnuplot   #(PyGnuplot: Python wrapper for Gnuplot.)
P3DTS.datetimestamp_us("import ... graphviz")
import graphviz    #(Graphviz module used to create graph objects which can be completed using different nodes and edges.)
P3DTS.datetimestamp_us("import ... pydot")
import pydot       #(pydot.PyPI - Python interface to Graphviz's Dot.)
P3DTS.datetimestamp_us("import ... pydotplus")
import pydotplus   #(PyDotPlus is an improved version of the old pydot project.)
P3DTS.datetimestamp_us("import ... tkinter")
import tkinter     #(Tkinter is the de facto way in Python to create Graphical User interfaces - GUIs) 
P3DTS.datetimestamp_us("import ... landscape_pdf")
import landscape_pdf  #(landscape style in PDF.) 
P3DTS.datetimestamp_us("import ... PyQt5")
import PyQt5  #(landscape style in PDF.) 

P3DTS.datetimestamp_us("### FILE PROCESSING PACKAGES")

P3DTS.datetimestamp_us("import ... io")
import io          #(Python io module allows us to manage the file-related input and output operations. Can write to Unicode data)
P3DTS.datetimestamp_us("import ... fileinput")
import fileinput   #(Module can iterate over lines from multiple input streams, write a loop over standard input or a list of files, etc)
P3DTS.datetimestamp_us("import ... difflib")
import difflib     #(Module provides classes and functions for comparing sequences. Can be used for comparing files, file differences, etc) 
P3DTS.datetimestamp_us("import ... filecmp")
import filecmp     #(Module defines functions to compare files and directories, with various optional time/correctness trade-offs.)

P3DTS.datetimestamp_us("### DATA PROCESSING PACKAGES")

P3DTS.datetimestamp_us("import ... h5py")
import h5py        #(H5PY package is a Pythonic interface to the HDF5 binary data format. For example: Scilab/Octave data outputs/inputs)
P3DTS.datetimestamp_us("import ... h5pyViewer")
import h5pyViewer  #(Python library viewer for large numeric data frames in HDF5.)
P3DTS.datetimestamp_us("import ... hdf5storage")
import hdf5storage #(Utilities to read/write Python types to/from HDF5 files, including MATLAB v7.3 MAT files.)
P3DTS.datetimestamp_us("import ... h5df")
import h5df         #(Utilities to read/write Python types to/from HDF5 files, including MATLAB v7.3 MAT files.)
P3DTS.datetimestamp_us("import ... csv")
import csv         #(Comma Separated Values - most common import and export format for spreadsheets and databases.)
P3DTS.datetimestamp_us("import ... pandas")
import pandas      #(Python Data Analysis - imports data various file formats like comma-separated values, JSON, SQL, Microsoft Excel.)
P3DTS.datetimestamp_us("import ... seaborn")
import seaborn     #(Python Data Visualization - attractive and informative statistical graphics, Matplotlib-based.)
P3DTS.datetimestamp_us("import ... vitables")
import vitables    #(ViTables is a graphical tool for browsing and editing files in both PyTables and HDF5 format)

P3DTS.datetimestamp_us("### DEEP LEARLING NEURAL NETWORKS")

P3DTS.datetimestamp_us("import ... sklearn")
import sklearn      #(Scikit Learn)
P3DTS.datetimestamp_us("import ... torch")
import torch        #(The package name for PyTorch is torch. With strong GPU acceleration.)
P3DTS.datetimestamp_us("import ... torchvision")
import torchvision  #(Image and video datasets and models for torch deep learning)
P3DTS.datetimestamp_us("import ... theano")
import theano       #(allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays)
P3DTS.datetimestamp_us("import ... tornado")
import tornado      #(non-blocking network I/O, Tornado can scale to tens of thousands of open connections, making it ideal for long polling,)
P3DTS.datetimestamp_us("import ... tensorflow")
import tensorflow   #(TensorFlow is one of the most famous machine learning libraries)
P3DTS.datetimestamp_us("import ... keras")
import keras        #(Keras is best for easy and fast prototyping as a deep learning library.)


### CODE ENDS HERE
### =======================================================

### WE CALCULATE DURATION SINCE START-TIME. NO NEED TO CAPTURE END-TIME AND SENT TO THE MODULE. 
### THE DATE-TIME STAMP MODULE CAPTURES AUTOMATICALLY END-TIME FROM THE SYSTEM CLOCK AS IT EXECUTES.
P3DTS.datetimestamp_us("Completed: py3_runtest_modules.py ==> Alhamdulillah Hirrabil Alamin")
P3DTS.execution_duration(tstart1, "for the total running time.")

"""
===========================================================
ALHAMDULILLAH 3 TIMES.
===========================================================
wruslan@HPEliteBook8570w-UbS2004:~/Documents/Documents/2021-06-20-The-NURBS-Book/python-nurbs-basic01/nurbs-python3$ python3 py3_runtest_modules.py 
2021-06-28 03:44:20.864289 ==>  Starting:  py3_runtest_modules.py ==> Bismillah Hirrahma Nirrahim
2021-06-28 03:44:20.864337 ==>  ### BASIC SYSTEM PACKAGES
2021-06-28 03:44:20.864354 ==>  import ... sys
2021-06-28 03:44:20.864392 ==>  import ... os
2021-06-28 03:44:20.864407 ==>  import ... time
2021-06-28 03:44:20.864421 ==>  import ... datetime
2021-06-28 03:44:20.864434 ==>  import ... dateutil
2021-06-28 03:44:20.864868 ==>  import ... errno
2021-06-28 03:44:20.865034 ==>  import ... psutil
2021-06-28 03:44:20.887573 ==>  ### MATHEMATICAL PACKAGES
2021-06-28 03:44:20.887621 ==>  import ... numpy
2021-06-28 03:44:21.025070 ==>  import ... scipy
2021-06-28 03:44:21.034066 ==>  import ... random
2021-06-28 03:44:21.034099 ==>  import ... random2
2021-06-28 03:44:21.034564 ==>  import ... math
2021-06-28 03:44:21.034587 ==>  import ... cmath
2021-06-28 03:44:21.034721 ==>  import ... fractions
2021-06-28 03:44:21.035809 ==>  import ... statistics
2021-06-28 03:44:21.036965 ==>  import ... io
2021-06-28 03:44:21.036999 ==>  import ... string
2021-06-28 03:44:21.037992 ==>  import ... from io import StringIO
2021-06-28 03:44:21.038024 ==>  import ... mpmath
2021-06-28 03:44:21.061099 ==>  ### EXECUTION AND PROCESSING PACKAGES
2021-06-28 03:44:21.061150 ==>  import ... mpi4py
2021-06-28 03:44:21.061540 ==>  import ... threading
2021-06-28 03:44:21.061564 ==>  import ... multiprocessing
2021-06-28 03:44:21.063231 ==>  import ... concurrent
2021-06-28 03:44:21.063431 ==>  import ... trace
2021-06-28 03:44:21.067211 ==>  import ... traceback
2021-06-28 03:44:21.067239 ==>  import ... Concurrent_AP
2021-06-28 03:44:21.810215 ==>  import ... parallel_transform
2021-06-28 03:44:21.810587 ==>  import ... pytest_parallel
2021-06-28 03:44:21.877225 ==>  ### GRAPHICS PROCESSING PACKAGES
2021-06-28 03:44:21.877332 ==>  import ... geomdl
2021-06-28 03:44:21.877563 ==>  import ... plotly
2021-06-28 03:44:21.878231 ==>  import ... matplotlib
2021-06-28 03:44:21.929963 ==>  import ... matplotlib.pyplot
2021-06-28 03:44:22.150756 ==>  import ... pylab
2021-06-28 03:44:22.151761 ==>  import ... PyGnuplot
2021-06-28 03:44:22.158296 ==>  import ... graphviz
2021-06-28 03:44:22.163246 ==>  import ... pydot
2021-06-28 03:44:22.165354 ==>  import ... pydotplus
2021-06-28 03:44:22.166869 ==>  import ... tkinter
2021-06-28 03:44:22.198215 ==>  import ... landscape_pdf
2021-06-28 03:44:22.202884 ==>  import ... PyQt5
2021-06-28 03:44:22.202938 ==>  ### FILE PROCESSING PACKAGES
2021-06-28 03:44:22.202971 ==>  import ... io
2021-06-28 03:44:22.202997 ==>  import ... fileinput
2021-06-28 03:44:22.203286 ==>  import ... difflib
2021-06-28 03:44:22.203312 ==>  import ... filecmp
2021-06-28 03:44:22.203630 ==>  ### DATA PROCESSING PACKAGES
2021-06-28 03:44:22.203662 ==>  import ... h5py
2021-06-28 03:44:22.222835 ==>  import ... h5pyViewer
2021-06-28 03:44:22.223128 ==>  import ... hdf5storage
2021-06-28 03:44:22.224734 ==>  import ... h5df
2021-06-28 03:44:22.429964 ==>  import ... csv
2021-06-28 03:44:22.430025 ==>  import ... pandas
2021-06-28 03:44:22.430059 ==>  import ... seaborn
2021-06-28 03:44:22.618705 ==>  import ... vitables
2021-06-28 03:44:22.618981 ==>  ### DEEP LEARLING NEURAL NETWORKS
2021-06-28 03:44:22.619003 ==>  import ... sklearn
2021-06-28 03:44:22.619027 ==>  import ... torch
2021-06-28 03:44:23.071513 ==>  import ... torchvision
2021-06-28 03:44:23.123642 ==>  import ... theano
2021-06-28 03:44:23.988811 ==>  import ... tornado
2021-06-28 03:44:23.989169 ==>  import ... tensorflow
2021-06-28 03:44:24.289802: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcudart.so.11.0
2021-06-28 03:44:25.396623 ==>  import ... keras
2021-06-28 03:44:25.608391 ==>  Completed: py3_runtest_modules.py ==> Alhamdulillah Hirrabil Alamin
2021-06-28 03:44:25.608452 ==>  Duration: 4.744167 seconds execution for the total running time.
wruslan@HPEliteBook8570w-UbS2004:~/Documents/Documents/2021-06-20-The-NURBS-Book/python-nurbs-basic01/nurbs-python3$ 

"""

