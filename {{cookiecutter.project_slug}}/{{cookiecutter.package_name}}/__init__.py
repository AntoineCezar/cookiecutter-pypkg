import os
{%- if cookiecutter.exemple == 'y' %}

from .greet import greet
{%- endif %}


__version_file__ = os.path.join(os.path.dirname(__file__), 'VERSION')
__version__ = open(__version_file__, 'r').read().strip()
{%- if cookiecutter.exemple == 'y' %}


__all__ = [
    'greet'
]
{%- endif %}
