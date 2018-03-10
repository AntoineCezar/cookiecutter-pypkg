import os
{%- if cookiecutter.exemple == 'y' %}

from .greet import greet
{%- endif %}


__version_file__ = os.path.join(os.path.dirname(__file__), 'VERSION')
__version__ = open(version_file, 'r').read().strip()
{%- if cookiecutter.exemple == 'y' %}


__all__ = [
    'greet'
]
{%- endif %}
