{{ cookiecutter.project_name | count * '=' }}
{{ cookiecutter.project_name }}
{{ cookiecutter.project_name | count * '=' }}

v{{ cookiecutter.version}}
{{ cookiecutter.project_short_description }}

Installation
------------

Requirements
~~~~~~~~~~~~

* setuptools >= 30.3.0 (to configure setup() using setup.cfg)
{% if cookiecutter.license != "None" %}

License
-------

{{ cookiecutter.license }}
{%- endif %}
