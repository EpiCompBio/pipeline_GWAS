.. include:: substitution_vars.rst

.. GitHub doe not render rst substitutions

.. copy across your travis "build..." logo so that it appears in your Github page

.. .. image:: https://travis-ci.org/|github_user|/|project_name|.svg?branch=master
    :target: https://travis-ci.org/|github_user|/|project_name|

.. do the same for ReadtheDocs image:

.. note that if your project is called project_Super readthedocs will convert
.. it to project-super

.. .. image:: https://readthedocs.org/projects/|project_name|/badge/?version=latest
    :target: http://|project_name|.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

 .. Edit manually:

.. .. Zenodo gives a number instead, this needs to be put in manually here:
   .. image:: https://zenodo.org/badge/#######.svg
      :target: https://zenodo.org/badge/latestdoi/#####

**IN PROGRESS**


################################################
|project_name|
################################################


.. The following is a modified template from RTD
    http://www.writethedocs.org/guide/writing/beginners-guide-to-docs/#id1

.. For a discussion/approach see 
    http://tom.preston-werner.com/2010/08/23/readme-driven-development.html

|short_description|


|long_description|

Features
--------

- Something really useful
- Makes things faster


Requirements
------------

See requirements files and Dockerfile for full information. At the least you'll need:

* CGATCore
* R >= 3.2
* Python >= 3.5
* r-docopt
* r-data.table
* r-ggplot2

Installation
------------

.. code-block:: bash
   
    pip install git+git://github.com/|github_user|/|project_name|.git


To use
------

.. code-block:: bash

    # Create a folder or a whole data science project, e.g. project_quickstart -n QTL_project
    cd QTL_project/results
    mkdir tests ; cd tests
    # Download test files, e.g.:
    wget -nH -np -r --cut-dirs=4 -A .txt http://www.bios.unc.edu/research/genomic_software/Matrix_eQTL/Sample_Data/
    python pipeline_QTL --help
    python pipeline_QTL config
    etc



Contribute
----------

- `Issue Tracker`_
  
.. _`Issue Tracker`: github.com/|github_user|/|project_name|/issues

- `Source Code`_
  
.. _`Source Code`: github.com/|github_user|/|project_name|

- Pull requests welcome!


Support
-------

If you have any issues, pull requests, etc. please report them in the issue tracker. 


