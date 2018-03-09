import argparse
{%- if cookiecutter.exemple != 'n' %}

from .greet import greet
{%- endif %}


def parse_args():
    parser = argparse.ArgumentParser(
        description='{{ cookiecutter.project_short_description }}'
    )

    {% if cookiecutter.exemple != 'n' -%}
    parser.add_argument('name', metavar='NAME', type=str,
                        help='name to greet')

    {% endif -%}
    return parser.parse_args()


def main():
    args = parse_args()
    {% if cookiecutter.exemple != 'n' -%}
    greet(args.name)
    {%- endif %}


if __name__ == "__main__":
    main()
