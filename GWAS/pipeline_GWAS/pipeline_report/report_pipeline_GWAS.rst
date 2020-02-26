.. include:: report_substitution_vars.rst

###########################
|project_name|
###########################


Authored by:

|all_author_names|

Date: |date|

Keywords: |keywords|

version = |version|

Licensed as |license|

Check the project at:

|project_url|

Correspondence to: |author_email|


.. See rst-basics_ for webpages and tutorials.

.. .. _rst-basics: https://github.com/EpiCompBio/welcome/blob/master/rst_basics.rst


Introduction
############


|short_description|


This file was created using Sphinx_. To modify it you'll need to change the
following files:

- Makefile
- conf.py
- index.rst
- report_pipeline_pq_example.rst
- report_substitution_vars.rst

Makefile makes it easier to invoke sphinx commands.

conf.py is the Sphinx configuration file, modify it to configure all aspects of how Sphinx reads and builds.

In report_substitution_vars.rst you can change some of the text that gets
automatically replaced.

See the `Sphinx tutorial`_ to get a better idea of what's happening.

.. _Sphinx: http://www.sphinx-doc.org
.. _`Sphinx tutorial`: http://www.sphinx-doc.org/en/stable/tutorial.html


Results
#######

Figures
============


.. figure:: ../F1_mtcars.*

    This is from "../F1_mtcars.*"

    You can add a legend here.



.. figure:: ../F2_mtcars.*
   :height: 300
   :width: 300
   :scale: 75
   :alt: A multi-panel plot from the R dataset mtcars



.. figure:: ../F2_mtcars.*
   :align: center

   This is a multi-panel plot from the file F2_mtcars.*


.. figure:: ../my_dataframe.*
   :align: center

   These are python matplotlib plots.

   The legend follows the empty line after the caption.


You can see the `image directive`_ for details.

.. _`image directive`: http://docutils.sourceforge.net/docs/ref/rst/directives.html#images


-----


PDF files can also be included e.g.::

  :download:`F1_mtcars.pdf <../F1_mtcars.pdf>`

but they'll only be available in html outputs.

To hide it in PDFs, use::

  .. only:: builder_html

     See :download:`this example script <../example.py>`.

You can see more information on this here_.

.. _here: http://www.sphinx-doc.org/en/stable/markup/inline.html#referencing-downloadable-files


Tables
============

To output tables as csv or tsv you can use::

   .. csv-table::
   :file: ../desc_stats_my_dataframe.tsv
   :delim: tab

to embed results in either html or pdf output:

.. csv-table::
   :file: ../desc_stats_my_dataframe.tsv
   :delim: tab


If you have html or tex files you can use the raw directive as a workaround.
Best not abused though. The :file: option may represent a security risk.
You'll need to use both html and latex files for their corresponding outputs. 

Note that for PDFs floating in latex (i.e. controlling where figures and tables will
appear) can be hard to control. See the raw version of this file, conf.py for latex options and `this webpage`_
for some information. 

.. _`this webpage`: https://tex.stackexchange.com/questions/39017/how-to-influence-the-position-of-float-environments-like-figure-and-table-in-lat/39020#39020


.. raw:: latex
   :file: ../my_dataframe_lm_table.tex


-----


.. raw:: html
   :file: ../my_dataframe_lm_table.html



.. raw:: latex
   :file: ../mtcars_lm_table.tex


-----


.. raw:: html
   :file: ../mtcars_lm_table.html



References
##########

Code used is available at |project_url|

References, e.g. :cite:`RN2398`, are pulled from a bibtex file which must be
specified at the bottom of the page as::

  .. bibliography:: scipy_references.bib


See the sphinxcontrib-bibtex_ extension for details.

There are other ways of including citations, see the `citation directive`_ for a simple approach.

.. _sphinxcontrib-bibtex: https://github.com/mcmtroffaes/sphinxcontrib-bibtex

.. _`citation directive`: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#citations


.. bibliography:: scipy_references.bib

