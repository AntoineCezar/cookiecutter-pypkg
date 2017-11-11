{%- if cookiecutter.test_runner == 'unittest' %}
import unittest
import io

from {{ cookiecutter.package_name }} import greet


class TestGreet(unittest.TestCase):

    def test_it_greets_the_given_name(self):
        name = 'World'
        out = io.StringIO()

        greet(name, out)

        self.assertEqual(out.getvalue(), 'Hello {}!\n'.format(name))
{%- elif cookiecutter.test_runner == 'pytest' %}
import io

from {{ cookiecutter.package_name }} import greet


def test_it_greets_the_given_name():
    name = 'World'
    out = io.StringIO()

    greet(name, out)

    assert out.getvalue() == 'Hello {}!\n'.format(name)
{%- endif %}
