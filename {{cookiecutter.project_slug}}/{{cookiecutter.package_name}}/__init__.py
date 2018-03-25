import pathlib
{%- if cookiecutter.exemple == 'y' %}

from .greet import greet
{%- endif %}


__version__ = (pathlib.Path(__file__).parent / 'VERSION').read_text().strip()
{%- if cookiecutter.exemple == 'y' %}


__all__ = [
    'greet'
]
{%- endif %}
