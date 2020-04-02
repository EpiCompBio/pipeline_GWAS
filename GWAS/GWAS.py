#!/usr/bin/env python3
'''
template.py
================

:Author: |author_names|
:Release: |version|
:Date: |today|


Purpose
=======

|description|


Usage and options
=================

These are based on docopt_, see examples_.

.. _docopt: https://github.com/docopt/docopt

.. _examples: https://github.com/docopt/docopt/blob/master/examples/options_example.py


Usage:
       template.py [-I FILE] [-O FILE]
       template.py [-h | --help] [-V | --version] [-f --force] [-L | --log]

Options:
    -I FILE             Input file name
    -O FILE             Output file name
    -h --help           Show this screen
    -V --version        Show version
    -f --force          Force overwrite
    -L --log            Log file name


Input:


Output:


Requirements:


Documentation
=============

    For more information see:

        |url|

'''
##############
# Get all the modules needed
# System:
import os
import sys
import glob

# Options and help:
import docopt

# Data science:
import pandas
#import numpy
import matplotlib.pyplot as plt
import scipy.stats as stats

# required to make iteritems python2 and python3 compatible
from builtins import dict

# Try getting CGAT:
try:
    import CGAT.iotools as iotools
    import CGATPipeline.Pipeline as P
    import CGATPipeline.Experiment as E

except ImportError:
    print('\n', "Warning: Couldn't import CGAT modules, continuing without")
    pass

# Import this project's module, uncomment if building something more elaborate:
#try:
#    import module_template.py

#except ImportError:
#    print("Could not import this project's module, exiting")
#    raise

# Import additional packages:
#import string # this is used in the pandas function
##############

##############
#####
# If this becomes a more complex project you could move all functions (except
# e.g. main()) to a module.py script.

def createGreat(my_msg = 'Great stuff!'):
    '''
    Useful explanation here for docstrings. Try to follow these conventions:
    https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt#id5
    See the next function as a docs example (taken directly from the IDE
    Spyder).
    '''
    # Do something great
    great = my_msg
    print(great)
    return(great)

def average(a, b):
    """
    Given two numbers a and b, return their average value.

    Parameters
    ----------
    a : number
      A number
    b : number
      Another number

    Returns
    -------
    res : number
      The average of a and b, computed using 0.5*(a + b)

    Example
    -------
    >>> average(5, 10)
    7.5

    """

    return (a + b) * 0.5

#####
##############

##############
def main():
    ''' with docopt main() expects a dictionary with arguments from docopt()
    docopt will automatically check your docstrings for usage, set -h, etc.
    '''
    options = docopt.docopt(__doc__)
    welcome_msg = str('\n' + 'Welcome to template.py.')
    print(welcome_msg)
    docopt_error_msg = str('\n' + 'template.py exited due to an error.' + '\n')
    docopt_error_msg = str(docopt_error_msg
                           + '\n'
                           + 'Try template.py --help'
                           + '\n' + '\n'
                           + 'Options in place:'
                           + '\n'
                           + str(options)
                           + '\n'
                           )

    try:
        if True:
            createGreat()
            print('Finished successfully')

        else:
            print(docopt_error_msg)
            print(''' Some helpfule message
                      Exiting...
                  ''')
            sys.exit()

    # Handle exceptions:
    except docopt.DocoptExit:
        print(docopt_error_msg)
        raise
##############


##############
# Finish and exit with docopt arguments:
if __name__ == '__main__':
    sys.exit(main())
##############
