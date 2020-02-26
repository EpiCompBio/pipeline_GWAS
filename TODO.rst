################################
Plan 
################################

:Date: 
:Author: 

Current state
##############

-
-
-


Future work
############



Main tasks
#################

Plan:

- What's the question?
- Write project pipeline steps, scripts needed, pseudocode and sketch
- Write scripts, write it up as a package
- Check Travis setup: pep8, flake8, create unit tests
- Update python and external dependencies file

-----

To do manually:

- Upload to GitHub account
- Manually connect to Travis for testing, add image to README.rst
- Keep track of installations for Docker instructions
- Manually connect to Zenodo, each release will trigger an archive and DOI
- Manually connect to ReadtheDocs, triggers will build the package's documentation on their webpage:

    + Manual configuration is needed on both the GitHub and ReadtheDocs sides:

		* Sign up to RTD, connect it to your GitHub account and allow permissions
		* At RTD setup the configuration as needed, check:

			- Repo:: https://github.com/github_username/project_name.git
			- Add the *.git* to it
			- Use virtualenv: (checked)
			- Requirements file:: requirements.txt
			- The rest should be OK with the defualts. The EPUB option may need further configuring though.
			- Copy the RTD image to your README.rst so the badge shows up.
		
- Setup conda recipe or PyPi if appropriate:
	+ Manually modify the Python packaging template files with your project information and then (info directly from diveintopython3_):
		* Run the Distutils built-in validation command: 
		
.. code-block:: python

	python setup.py check

Distutils can build different types of releases. Build a source distribution as a minimum that includes your source code, setup.py script, README and any additional files (which you need to manually specify in the MANIFEST.in template). Then, build a source distribution with:
		
.. code-block:: python

	python setup.py sdist

This will create a *"dist/"* folder which should contain a *".zip"* file that can then be shared.

- See diveintopython3_ for instructions for Python3 and Distutils (basic instructions copied here):

	+ Upload your software tools to the Python Package Index (PyPi):

	    = Register yourself (go to PyPi's registration_)
	    = Register your software
	    = Upload the packages you created with setup.py sdist and setup.py bdist_*
	    = To release a new version, update setup.py with the new version number, then run the same upload command:

.. code-block:: python

	python setup.py register sdist upload

Add bdist_wininst to include a Windows graphical installer_.

.. _diveintopython3: http://www.diveintopython3.net/packaging.html

.. _registration:  https://pypi.python.org/pypi?:action=register_form)

.. _installer: http://www.diveintopython3.net/packaging.html#bdist

- You need to manually choose a license, classify your software using the PyPI classification system () and write a README.txt file.

- See also CookieCutter's helpful tutorial_ for PyPi instructions.

.. _tutorial: https://cookiecutter-pypackage.readthedocs.io/en/latest/pypi_release_checklist.html

PIPELINE PLAN
#############

.. todo::

	TO DO

-----


The output should be input for:


References
##########


Also see:

