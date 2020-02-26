'''
pipeline_name
=============

:Author: |author_name|
:Release: |version|
:Date: |today|


Overview
========

|long_description|


Purpose
=======

.. briefly describe the main purpose and methods of the pipeline



Usage and options
=================

These are based on CGATPipelines_ and Ruffus_, not docopt.

.. _CGATPipelines: https://github.com/CGATOxford/CGATPipelines

.. _Ruffus: http://www.ruffus.org.uk/


For command line help type:

    python pipeline_pq_example.py --help

Configuration
=============

This pipeline is built using a Ruffus/CGAT approach. You need to have Python,
Ruffus, CGAT core tools and any other specific dependencies needed for this
script.

A configuration file was created at the same time as this script.

Use this to extract any arbitrary parameters that could be changed in future
re-runs of the pipeline.


Input files
===========

.. Describe the input files needed, urls for reference and preferably place
example data somewhere.


Pipeline output
===============

.. Describe output files and results


Requirements
============

cgat-core as well as the following software need to be in the path:

.. Add any additional external requirements such as 3rd party software
   or R modules below:

Requirements:

* R >= 3.4
* Python >= 3.5

Documentation
=============

    For more information see:

        |url|

'''
################
# Get modules needed:
import sys
import os
import re
import subprocess

# Pipeline:
from ruffus import *

# Database:
import sqlite3

# CGAT tools:
import cgatcore.iotools as iotools
import cgatcore.pipeline as P
import cgatcore.experiment as E


# Import this project's module, uncomment if building something more elaborate: 
#try: 
#    import  pipeline_template.module_template

#except ImportError: 
#    print("Could not import this project's module, exiting") 
#    raise 

# Import additional packages:
# Set path if necessary:
#os.system('''export PATH="~/xxxx/xxxx:$PATH"''')
################

################
# Get locations of source code (this file)
    # os.path.join note: a subsequent argument with an '/' discards anything
    # before it
    # For function to search path see: 
    # http://stackoverflow.com/questions/4519127/setuptools-package-data-folder-location
# MANIFEST.in file instructs the project_quickstart/templates folder to be included in installation

_ROOT = os.path.abspath(os.path.dirname(__file__))
def getDir(path = _ROOT):
    ''' Get the absolute path to where this function resides. Useful for
    determining the user's path to a package. If a sub-directory is given it
    will be added to the path returned. Use '..' to go up directory levels. '''
   # src_top_dir = os.path.abspath(os.path.join(_ROOT, '..'))
    src_dir = _ROOT
    return(os.path.abspath(os.path.join(src_dir, path)))
################

################
# Load options from the config file
# Pipeline configuration
ini_paths = [os.path.abspath(os.path.dirname(sys.argv[0])),
             "../",
             os.getcwd(),
             ]

def getParamsFiles(paths = ini_paths):
    '''
    Search for python ini files in given paths, append files with full
    paths for P.getParameters() to read.
    Current paths given are:
    where this code is executing, one up, current directory
    '''
    p_params_files = []
    for path in ini_paths:
        for f in os.listdir(os.path.abspath(path)):
            ini_file = re.search(r'pipelin(.*).yml', f)
            if ini_file:
                ini_file = os.path.join(os.path.abspath(path), ini_file.group())
                p_params_files.append(ini_file)
    return(p_params_files)

P.Parameters.get_params()
P.get_parameters(
        ["%s/pipeline.yml" % os.path.splitext(__file__)[0],
            "../pipeline.yml",
            "pipeline.yml"],
        )


PARAMS = P.PARAMS
# Print the options loaded from ini files and possibly a .cgat file:
#pprint.pprint(PARAMS)
# From the command line:
#python ../code/pq_example/pipeline_pq_example/pipeline_pq_example.py printconfig


# Set global parameters here, obtained from the ini file
# e.g. get the cmd tools to run if specified:
#cmd_tools = P.asList(PARAMS["cmd_tools_to_run"])

def get_py_exec():
    '''
    Look for the python executable. This is only in case of running on a Mac
    which needs pythonw for matplotlib for instance.
    '''

    try:
        if str('python') in PARAMS["general"]["py_exec"]:
            py_exec = '{}'.format(PARAMS["general"]["py_exec"])
    except NameError:
        E.warn('''
               You need to specify the python executable, just "python" or
               "pythonw" is needed in pipeline.yml.
               ''')
    #else:
    #    test_cmd = subprocess.check_output(['which', 'pythonw'])
    #    sys_return = re.search(r'(.*)pythonw', str(test_cmd))
    #    if sys_return:
    #        py_exec = 'pythonw'
    #    else:
    #        py_exec = 'python'
    return(py_exec)
#get_py_exec()

def getINIpaths():
    '''
    Get the path to scripts for this project, e.g.
    project_xxxx/code/project_xxxx/:
    e.g. my_cmd = "%(scripts_dir)s/bam2bam.py" % P.Parameters.get_params()
    '''
    # Check getParams as was updated to get_params but
    # PARAMS = P.Parameters.get_parameters(getParamsFiles())
    # is what seems to work
    try:
        project_scripts_dir = '{}/'.format(PARAMS['general']['project_scripts_dir'])
        E.info('''
               Location set for the projects scripts is:
               {}
               '''.format(project_scripts_dir)
               )
    except KeyError:
        E.warn('''
               Could not set project scripts location, this needs to be
               specified in the project ini file.
               ''')
        raise

    return(project_scripts_dir)
################

################
# Utility functions
def connect():
    '''utility function to connect to database.

    Use this method to connect to the pipeline database.
    Additional databases can be attached here as well.

    Returns an sqlite3 database handle.
    '''

    dbh = sqlite3.connect(PARAMS["database"]["name"])
    statement = '''ATTACH DATABASE '%s' as annotations''' % (
        PARAMS["annotations"]["database"])
    cc = dbh.cursor()
    cc.execute(statement)
    cc.close()

    return dbh
################

################
# Specific pipeline tasks
# Tools called need the full path or be directly callable

@transform((INI_file, "conf.py"),
           regex("(.*)\.(.*)"),
           r"\1.counts")
def countWords(infile, outfile):
    '''count the number of words in the pipeline configuration files.'''

    # the command line statement we want to execute
    statement = '''awk 'BEGIN { printf("word\\tfreq\\n"); }
    {for (i = 1; i <= NF; i++) freq[$i]++}
    END { for (word in freq) printf "%%s\\t%%d\\n", word, freq[word] }'
    < %(infile)s > %(outfile)s'''

    # execute command in variable statement.
    #
    # The command will be sent to the cluster.  The statement will be
    # interpolated with any options that are defined in in the
    # configuration files or variable that are declared in the calling
    # function.  For example, %(infile)s will we substituted with the
    # contents of the variable "infile".
    P.run(statement)


@transform(countWords,
           suffix(".counts"),
           "_counts.load")
def loadWordCounts(infile, outfile):
    '''load results of word counting into database.'''
    P.load(infile, outfile, "--add-index=word")
################

################
# Copy to log enviroment from conda:
@follows(loadWordCounts)
@originate('conda_info.txt')
def conda_info(outfile):
    '''
    Save to logs conda information and packages installed.
    '''
    packages = 'conda_packages.txt'
    channels = 'conda_channels.txt'
    environment = 'environment.yml'

    statement = '''conda info -a > %(outfile)s ;
                   conda list -e > %(packages)s ;
                   conda list --show-channel-urls > %(channels)s ;
                   conda env export > %(environment)s
                '''
    P.run(statement)
################

################
# Create the "full" pipeline target to run all functions specified
@follows(conda_info)
@originate('pipeline_complete.touch')
def full(outfile):
    statement = 'touch %(outfile)s'
    P.run(statement)
################

################
# Build report with pre-configured files using sphinx-quickstart
# Convert any svg files to PDF if needed:
@transform('*.svg', suffix('.svg'), '.pdf')
def svg_to_pdf(infile, outfile):
    '''
    Simple conversion of svg to pdf files with inkscape
    '''
    statement = '''
                inkscape --without-gui \
                         --export-area-drawing \
                         --export-margin=2 \
                         --file=%(infile)s \
                         --export-pdf=%(outfile)s
                '''
    P.run(statement)


# Build the report:
report_dir = 'pipeline_report'
@follows(svg_to_pdf)
@follows(mkdir(report_dir))
def make_report():
    ''' Generates html and pdf versions of restructuredText files
        using sphinx-quickstart pre-configured files (conf.py and Makefile).
        Pre-configured files need to be in a pre-existing report directory.
        Existing reports are overwritten.
    '''
    report_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                               'pipeline_report'
                                               ))
    print('Copying report templates from: {}'.format(report_path))

    if (os.path.exists(report_dir) and
            os.path.isdir(report_dir) and not
            os.listdir(report_dir)):
        statement = '''cp %(report_path)s/* pipeline_report ;
                       cd {} ;
                       ln -s ../pipeline.yml . ;
                       make html ;
                       ln -sf _build/html/report_pipeline_pq_example.html . ;
                       make latexpdf ;
                       ln -sf _build/latex/pq_example.pdf .
                    '''.format(report_dir)
        E.info('''Building pdf and html versions of your rst files in
                  {}.'''.format(report_dir))
        P.run(statement)

    elif (os.path.exists(report_dir) and
            os.path.isdir(report_dir) and
            os.listdir(report_dir)):
        sys.exit(''' {} exists, not overwriting. You can manually run:
                       cd {} ;
                       ln -s ../pipeline.yml . ;
                       make html ;
                       ln -sf _build/html/report_XXXX.html . ;
                       make latexpdf ;
                       ln -sf _build/latex/XXXX.pdf .
                       Or delete the folder and re-run make_report
                 '''.format(report_dir))

    else:
        sys.exit(''' The directory "pipeline_report" does not exist.
                     Are the paths correct?
                     Template files were tried to be copied from:
                     {}
                     You can also manually copy files and run "make html" or
                     "make latexpdf".
                 '''.format(report_path))

    return

#    if (os.path.exists('pipeline_report/_build/html/index.hmtl') and
#       os.path.exists(os.path.join('pipeline_report/_build/latex/',
#                                   project_name, '.pdf'))):
#        statement = '''
#                    ln -s pipeline_report/_build/html/index.hmtl %(project_name)s.html ;
#                    ln -s pipeline_report/_build/latex/%(project_name)s.pdf .
#                    '''
#        E.info('''Done, links to the pdf and html versions of your rst files are in the main
#               folder.''')
#        P.run()
#
#    else:
#        E.info('''
#               The html and/or latex/pdf files did not build correctly. See the
#               logs and go into pipeline_report to find out. You can also try
#               building the report manually with make html and make latexpdf.
#               ''')
#        sys.exit()
################
# This is if pipeline is called directly from CLI:
# TO DO:
# Check if docopt and argparse can play to show my_pipeline options and P.py
# options

def main():
    sys.exit(P.main(sys.argv))

#def main(argv=None):
#    if argv is None:
#        argv = sys.argv
#    P.main(argv)
################

################
# Otherwise just end pipeline as normally (with sys.exit commented):
if __name__ == "__main__":
    main()
    #sys.exit(P.main(sys.argv))
################
