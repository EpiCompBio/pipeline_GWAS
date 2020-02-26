#!/usr/bin/env Rscript

######################
# R script to run with docopt for command line options:
'
script_name
===============

Author: |author_names|
Release: |version|
Date: |today|


Purpose
=======

|description|


Usage and options
=================

These are based on docopt_ for R:

https://github.com/docopt/docopt.R
https://cran.r-project.org/web/packages/docopt/index.html

To run, type:
    Rscript script_name -I <INPUT_FILE> [options]

Usage: script_name (-I <INPUT_FILE>)
       script_name [options]
       script_name [-h | --help]

Options:
  -I <INPUT_FILE>                 Input file name
  -O <OUTPUT_FILE>                Output file name
  --session                       R session if to be saved
  -h --help                       Show this screen
  -var                            some numeric argument [default: 0.001].

Input:

    A tab separated file with headers. This is read with data.table and stringsAsFactors = FALSE

Output:



Requirements:

    library(docopt)
    library(data.table)
    library(ggplot2)

Documentation
=============

    For more information see:

    |url|
' -> doc

# Load docopt:
library(docopt, quietly = TRUE)
# Retrieve the command-line arguments:
args <- docopt(doc)
# See:
# https://cran.r-project.org/web/packages/docopt/docopt.pdf
# docopt(doc, args = commandArgs(TRUE), name = NULL, help = TRUE,
# version = NULL, strict = FALSE, strip_names = !strict,
# quoted_args = !strict)

# Print to screen:
str(args)
# Within the script specify options as:
# args[['--session']]
# args $ `-I` == TRUE
######################

######################
# Logging
# This can be taken care of by CGAT Experiment.py if running as a pipeline.
# Otherwise there seem to be few good alternatives. A workaround is the code in:
# XXXX/project_quickstart/templates/script_templates/logging.R
# It does not run on its own though, needs copy/pasting for now.
######################

######################
# Load a previous R session, data and objects:
#load('R_session_saved_image_order_and_match.RData', verbose=T)
######################

######################
# This function allows other R scripts to obtain the path to a script directory
# (ie where this script lives). Useful when using source('some_script.R')
# without having to pre-specify the location of where that script is.
# This is taken directly from:
# How to source another_file.R from within your R script molgenis/molgenis-pipelines Wiki
# https://github.com/molgenis/molgenis-pipelines/wiki/How-to-source-another_file.R-from-within-your-R-script
# Couldn't find a licence at the time (12 June 2018)
LocationOfThisScript = function() # Function LocationOfThisScript returns the location of this .R script (may be needed to source other files in same dir)
{
    this.file = NULL
    # This file may be 'sourced'
    for (i in -(1:sys.nframe())) {
        if (identical(sys.function(i), base::source)) this.file = (normalizePath(sys.frame(i)$ofile))
    }

    if (!is.null(this.file)) return(dirname(this.file))

    # But it may also be called from the command line
    cmd.args = commandArgs(trailingOnly = FALSE)
    cmd.args.trailing = commandArgs(trailingOnly = TRUE)
    cmd.args = cmd.args[seq.int(from = 1, length.out = length(cmd.args) - length(cmd.args.trailing))]
    res = gsub("^(?:--file=(.*)|.*)$", "\\1", cmd.args)

    # If multiple --file arguments are given, R uses the last one
    res = tail(res[res != ""], 1)
    if (0 < length(res)) return(dirname(res))

    # Both are not the case. Maybe we are in an R GUI?
    return(NULL)
}
Rscripts_dir <- LocationOfThisScript()
print('Location where this script lives:')
Rscripts_dir
# R scripts sourced with source() have to be in the same directory as this one
# (or the path constructed appropriately with file.path) eg:
#source(file.path(Rscripts_dir, 'moveme.R')) #, chdir = TRUE)
######################

######################
# Import libraries
# source('http://bioconductor.org/biocLite.R')
# biocLite()
library(ggplot2)
library(data.table)
library(svglite) # prefer over base R svg()

# source functions from a different R script:
#source(file.path(Rscripts_dir, 'moveme.R')) #, chdir = TRUE)
######################

######################
##########
# Read files, this is with data.table:
if (!is.null(args[['-I']])) { # for docopt this will be NULL or chr, if boolean
	                            # remove is.null function and test with ==
  input_name <- as.character(args[['-I']])
  # For tests:
  # input_name <- 'XXX'
  # setwd('~/xxxx/')
  input_data <- fread(input_name, sep = '\t', header = TRUE, stringsAsFactors = FALSE)
} else {
  # Stop if arguments not given:
  print('You need to provide an input file. This has to be tab separated with headers.')
  stopifnot(!is.null(args[['-I']]))
}

print('File being used: ')
print(input_name)
##########

##########
# Set output file names:
suffix <- 'my_output'
if (is.null(args[['-O']])) { # arg is NULL
  # Split infile name at the last '.':
  output_name <- strsplit(input_name, "[.]\\s*(?=[^.]+$)", perl = TRUE)[[1]][1]
  output_file_name <- sprintf('%s.%s', input_name, suffix)
  print('Output file name not given. Using: ')
  print(output_file_name)
} else {
  output_name <- as.character(args[['-O']])
  # output_file_name <- 'testing'
  output_file_name <- sprintf('%s.%s', output_name, suffix)
  print(sprintf('Output file name provided: %s', output_file_name))
  print(output_file_name)
}
##########
######################

######################
# Some code
######################

######################
# More code
######################

######################
## Save some text:
# Methods
# Legend
# Interpretation
# cat(file <- output_file, some_var, '\t', another_var, '\n', append = TRUE)
######################

######################
# Save file:
fwrite(object_x, output_file_name,
       sep = '\t', na = 'NA',
       col.names = TRUE, row.names = FALSE,
       quote = FALSE)
######################

######################
# The end:
# Remove objects that are not necessary to save:
# ls()
# object_sizes <- sapply(ls(), function(x) object.size(get(x)))
# as.matrix(rev(sort(object_sizes))[1:10])
#rm(list=ls(xxx))
#objects_to_save <- (c('xxx_var'))
#save(list=objects_to_save, file=R_session_saved_image, compress='gzip')

# Filename to save current R session, data and objects at the end:
if (!is.null(args[['--session']])) { # arg is NULL
	save_session <- sprintf('%s_%s.RData', output_name, suffix)
  print(sprintf('Saving an R session image as: %s', save_session))
  save.image(file = save_session, compress = 'gzip')
} else {
  print('Not saving an R session image, this is the default. Specify the --session option otherwise')
}

# If using Rscript and creating plots, Rscript will create the file Rplots.pdf
# by default, it doesn't look like there is an easy way to suppress it, so deleting here:
print('Deleting the file Rplots.pdf...')
system('rm -f Rplots.pdf')
print('Finished successfully.')
sessionInfo()
q()

# Next: run the script for xxx
######################