#!/usr/bin/env python3
'''
svg_template.py
===============

:Author: |author_name|
:Release: |version|
:Date: |today|


Purpose
=======

|description|

Make a figure layout using the python package svgutils.

See examples and information from svgutils:

    - https://neuroscience.telenczuk.pl/?p=331
    - http://svgutils.readthedocs.io/en/latest/tutorials/composing_multipanel_figures.html
    - https://svgutils.readthedocs.io/en/latest/compose.html
    - http://cairosvg.org/
    - https://inkscape.org/en/


Usage and options
=================

These are based on docopt_, see examples_.

.. _docopt: https://github.com/docopt/docopt

.. _examples: https://github.com/docopt/docopt/blob/master/examples/options_example.py


Usage:
       svg_template.py (--plotA=<file_name>) (--plotB=<file_name>)
                       [--plotC=<file_name>] [--plotD=<file_name>]
                       (-O FILE)
       svg_template.py [-h | --help]

Options:
    --plotA <file_name>       Plot name for position A
    --plotB <file_name>       Plot name for position B
    --plotC <file_name>       Plot name for position C
    --plotD <file_name>       Plot name for position D
    -O FILE                   Output file name
    -h --help                 Show this screen


Input:

    Requires svg files as input.


Output:

    Outputs svg and pdf formats of a multi-panel plot.

Requires:

    Python packages and optionally Inkscape


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

# Get svgutils and PDF converter if not using Inkscape:
from svgutils.compose import *
import cairosvg

# Get additional packages needed:
import string

# Import this project's module, uncomment if building something more elaborate:
#try:
#    import module_template.py

#except ImportError:
#    print("Could not import this project's module, exiting")
#    raise
##############


##############
def plotMultiSVG(plots_given, outfile, **kwargs):
    ''' Takes two to four svg files and outputs a multi-panel figure in svg and
        pdf formats.
    '''
    plot_names = []

    for option in plots_given:
        plot_name = str(option).strip('[]').strip("''")
        plot_names.append(plot_name)

    print(''' The multi-panel figure will have the following {} plots:
              {}
          '''.format(len(plot_names), plot_names))

    # Name the final figure panel (which will be "F{figure_number}_{figure_name}.{format}", 
    # Only svg can be output with svgutils:
    figure_name = outfile
    file_format_in = 'svg'
    file_format_out = 'pdf'
    layout_name_1 = str('{}.{}'.format(figure_name,
                                       file_format_in))
    layout_name_2 = str('{}.{}'.format(figure_name,
                                       file_format_out))

    # Set up svgutils arguments:
    fig_size1 = "21cm"
    fig_size2 = "19cm" # A4 paper is 210 mm x 197 mm
    size = 11
    weight = "bold"
    pos1 = 10
    pos2 = 10
    scale = 0.6

    def getPanel():
        ''' Get a panel for each plot passed in the arguments
            In svgutils Panel() groups all elements belonging to one plot/panel
        '''
        # TO DO: get any number of panels from any number of plots given in the
        # CLI. Change docopt options to repeating arguments eg 
        # my_script.py --plot-names <plot_name> <plot_name>...
        # which would then be tiled left to right, top to bottom
        # switch to tile after PR or fork and update upstream
        # provide scale, moves, grid, fig sizes, size, weight, pos1, pos2, etc.
        # as CLI options with current defaults
        svg_panels = []
        letters = ['A', 'B', 'C', 'D'] # TO DO change to string upper case
        moves = [(20, 20), (380, 20), (20, 380), (380, 380)] # These move the plots
                                                             # but are temporary,
                                                             # and unlikely to
                                                             # work, as just
                                                             # guesses.
                                                             # Use tile() instead
                                                             # when PR is done, see
                                                             # below.
                                                             # move(horizontal px,
                                                             # vertical px)
        for idx,val in enumerate(plot_names):
            move_h, move_v = moves[idx][0], moves[idx][1]
            # vals are the actual plot to use
            # moves will place the plot at a given position

            panel_func = Panel(SVG(val).scale(scale), # scale only the plot, not the text
                                        Text(letters[idx], # Place Text() after SVG(), otherwise it doesn't plot
                                        pos1, pos2,
                                        size = size,
                                        weight = weight),
                                ).move(move_h, move_v) # move the whole panel
            svg_panels.append(panel_func)
        return(svg_panels)


    def getFigure():
        ''' Create the figure with the panels using svgutils Figure() funciton
        '''
        svg_panels = getPanel()
        fig_layout = Figure(fig_size1, fig_size2,
                            *svg_panels,
                                    # Grid(20, 20) # Generates a grid of horizontal and vertical lines 
                                                   # labelled with their position in pixel units
                                                   # Use to test if figure is placed correctly, then
                                                   # comment out. Use within Figure()
                                                   # e.g. Figure(XXX, Grid(20, 20), Panel(XXX))
                                    )
                                    #.tile(2, 1) # (ncols, nrows), use before .save()
                                    #.tile() errors, see:
                #https://stackoverflow.com/questions/45850144/is-there-a-bug-in-svgutils-compose-module-regarding-the-arrangement-of-figures/45863869#45863869

        # Save the Figure:
        fig_layout.save(layout_name_1)

        # Convert SVG file to PDF:
        #cairosvg.svg2pdf(url = layout_name_1,
        #                 write_to = layout_name_2
        #                 )

        # Alternatively with inkscape:
        os.system('''inkscape --without-gui \
                              --export-area-drawing \
                              --export-margin=2 \
                              --file={} \
                              --export-pdf={}'''.format(layout_name_1,
                                                        layout_name_2)
                 )
        # Inkscape has many more options, e.g. 
        # --export-background=white --export-dpi=300
        # See:
        #https://inkscape.org/sk/doc/inkscape-man.html

    # Call this function:
    getFigure()

    # TO DO: How to add legends directly?
    # Otherwise pull into an rst file and add there. 
##############

##############
def main():
    ''' with docopt main() expects a dictionary with arguments from docopt()
    docopt will automatically check your docstrings for usage, set -h, etc.
    '''
    options = docopt.docopt(__doc__)
    welcome_msg = str('\n' + 'Welcome to svgutils_template.py')
    print(welcome_msg)
    docopt_error_msg = str('\n' + 'svgutils_template.py exited due to an error.' + '\n')
    docopt_error_msg = str(docopt_error_msg
                           + '\n'
                           + 'Try svgutils_template.py --help'
                           + '\n' + '\n'
                           + 'Options in place:'
                           + '\n'
                           + str(options)
                           + '\n'
                           )

    try:
        # Names of the plots to read in, these have to be svg files:
        cond1 = options['--plotA'] and options['--plotB'] and options['-O']
        cond2 = cond1 and options['--plotC']
        cond3 = cond2 and options['--plotD']
        plots_given = []
        outfile = str(options["-O"]).strip('[]').strip("''")
        print(cond1, cond2, cond3)

        # Exit if one of plotA, plotB or outfile name are not given:
        if not (cond1 or cond2 or cond3):
            print(''' You need to provide at least two plots and an output file
                      name to make a multi-panel figure. Pass plots A and B or up
                      to four plots in svg format.
                   ''')
            print(docopt_error_msg)
            sys.exit()

        # If at least two plots are given run:
        if cond1 and not cond2 and not cond3:
            plots_given.append(options['--plotA'])
            plots_given.append(options['--plotB'])
            plotMultiSVG(plots_given = plots_given, outfile = outfile)

        elif cond2 and not cond3:
            plots_given.append(options['--plotA'])
            plots_given.append(options['--plotB'])
            plots_given.append(options['--plotC'])
            plotMultiSVG(plots_given = plots_given, outfile = outfile)

        elif cond3:
            plots_given.append(options['--plotA'])
            plots_given.append(options['--plotB'])
            plots_given.append(options['--plotC'])
            plots_given.append(options['--plotD'])
            plotMultiSVG(plots_given = plots_given, outfile = outfile)

        else:
            print(docopt_error_msg)
            print(''' Something didn't work... Exiting.
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
############ 
