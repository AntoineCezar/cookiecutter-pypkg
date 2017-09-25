import unittest
import io

from {{ cookiecutter.package_name }} import greet


class TestGreet(unittest.TestCase):

    def test_it_greets_the_given_name(self):
        name = 'World'
        out = io.StringIO()

        greet(name, out)

        self.assertEqual(out.getvalue(), 'Hello {}!\n'.format(name))
