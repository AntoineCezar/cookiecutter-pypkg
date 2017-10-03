"""
Does the following:

    1. Removes the RPM packaging method not chosen

"""
import os
import random
import shutil
import string
from pprint import pprint

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

# Global functions

def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)

def remove_tree(file_name):
    if os.path.exists(file_name):
        shutil.rmtree(file_name)

# Remove unused RPM files 
SPEC_FILE=os.path.join(PROJECT_DIRECTORY,'packaging/rpm/{{ cookiecutter.project_name }}.spec' )
SETUPTOOLS_FILE=os.path.join(PROJECT_DIRECTORY,'packaging/rpm/{{ cookiecutter.project_name }}.sh' )

if '{{ cookiecutter.rpm_packaging }}'.lower() == 'none':
    remove_tree(os.path.join(PROJECT_DIRECTORY,'packaging/rpm'))
else:
    if '{{ cookiecutter.rpm_packaging }}'.lower() != 'using a spec file':
        remove_file(SPEC_FILE)
    if '{{ cookiecutter.rpm_packaging }}'.lower() != 'using setuptools':
        remove_file(SETUPTOOLS_FILE)

    




