{{ cookiecutter.project_name | count * '=' }}
{{ cookiecutter.project_name }}
{{ cookiecutter.project_name | count * '=' }}

v{{ cookiecutter.version }}

{{ cookiecutter.project_short_description }}

Install
-------

Requirements for Installing Package:

* `pip` for installing packages
* `python3 -m venv venv` for creating a virtual environment.
* `setuptools >= 30.3.0` (to configure setup() using setup.cfg)

See the Python Packaging Authority's (PyPA) documention `Requirements for Installing Packages`_ for full details.

.. _`Requirements for Installing Packages`: https://packaging.python.org/tutorials/installing-packages/#requirements-for-installing-packages

On a Unix/Linux System
~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    $ export VENV=~/path/to/venv
    $ python3 -m venv $VENV
    $ $VENV/bin/pip install {{ cookiecutter.project_slug }}

For development use:

.. code:: sh

    $ export VENV=~/path/to/venv
    $ python3 -m venv $VENV
    $ cd /path/to/{{ cookiecutter.project_slug }}
    $ $VENV/bin/pip install -e . ".[develop]" ".[testing]"

A convenient Makefile is provided to ease development:

.. code:: sh

    $ make develop

For more useful commands run:

.. code:: sh

    $ make help

On a Windows System
~~~~~~~~~~~~~~~~~~~

.. code:: sh

    c:\> set VENV=c:\path\to\venv
    c:\> python -m venv %VENV%
    c:\> %VENV%\Scripts\pip install {{ cookiecutter.project_slug }}

For development use:

.. code:: sh

    c:\> set VENV=c:\path\to\venv
    c:\> python -m venv %VENV%
    c:\> cd \path\to\{{ cookiecutter.project_slug }}
    c:\> %VENV%\Scripts\pip install -e . ".[develop]" ".[testing]"
{% if cookiecutter.license != "None" %}

License
-------

{{ cookiecutter.license }}
{%- endif %}
