import pkg_resources

from .greet import greet


__version__ = pkg_resources.get_distribution('{{ cookiecutter.package_name }}').version

__all__ = [
    'greet'
]
