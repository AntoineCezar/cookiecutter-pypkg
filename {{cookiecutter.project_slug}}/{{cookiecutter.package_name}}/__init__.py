{%- if cookiecutter.exemple == 'y' %}
from .greet import greet


{% endif -%}
__version__ = '{{ cookiecutter.version }}'
{%- if cookiecutter.exemple == 'y' %}


__all__ = [
    'greet'
]
{% endif -%}
