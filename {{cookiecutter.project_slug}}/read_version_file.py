""" Read the version of the package.

At the time this package has been created, the "file:" directive does not work
in setup.cfg for "version".

Change:

version = attr: version.version

for:

version = file: {{ cookiecutter.package_name }}.VERSION

and delete this file if it works with newer version of setuptools.
"""
import os

version_file = os.path.join(
    os.path.dirname(__file__),
    '{{ cookiecutter.package_name }}', 'VERSION'
)
version = open(version_file, 'r').read().strip()
