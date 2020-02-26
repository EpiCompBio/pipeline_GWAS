'''
test_template.py
================

:Author: |author_names|
:Release: |version|
:Date: |today|


Purpose
=======

Run tests for project_template

# Workflow (for flake8 and pytest, other frameworks exist):
  # run flake8 for each file (within vim and in root dir)
  # run pytest, test locally, then upload for CI

See:
https://docs.pytest.org/en/latest/

If using helper functions for tests create a directory and file
eg tests/helpers/pytest_helpers.py
and import file as a module in test_*.py files.

A file conftest.py needs to exist containing:
###
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'helpers'))

# See:
# https://stackoverflow.com/questions/33508060/create-and-import-helper-functions-in-tests-without-creating-packages-in-test-di
###
so that the folder is put in the system path and can be discovered by the import statement.


If creating test data in a test_*.py file, use the decorator pytest.fixture eg:
import pytest
@pytest.fixture
def run_cmds():
    pytest_helpers.run_CLI_options(cli_options)


Note that pytest only picks files AND functions starting with 'test_'.


Usage and options
=================

Usage:
       pytest -v test_template.py
       test_template.py [-h | --help]

Options:
    -h --help           Show this screen

'''
##############
# Get all the modules needed
# System:
import pytest
import os
import tempfile

# Import helper functions from this package:
import pytest_helpers
##############


##############
# Tests for project_template

# Set up options to run:
test_name = ''

# Generate test data to compare against reference files

# Get directory for reference files:
ref_dir = os.path.abspath('ref_files')
print(ref_dir)

# Create temporary directory for test outputs:
test_dir = tempfile.mkdtemp()
print(test_dir)
os.chdir(test_dir)


# Generate test sets
# Functions that are needed to create test files should use the pytest.fixture decorator
@pytest.fixture
def run_cmds():
    pytest_helpers.run_CLI_options()


# pytest only picks files AND functions starting with 'test_'
def test_XXX():
    pytest_helpers.compare_all_files(ref_dir, test_dir)


print('Tests finished')
#####
##############
