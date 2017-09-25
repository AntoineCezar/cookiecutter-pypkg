import argparse

from .greet import greet


def parse_args():
    parser = argparse.ArgumentParser(
        description='{{ cookiecutter.project_short_description }}'
    )

    parser.add_argument('name', metavar='NAME', type=str,
                        help='name to greet')

    return parser.parse_args()


def main():
    args = parse_args()
    greet(args.name)


if __name__ == "__main__":
    main()
