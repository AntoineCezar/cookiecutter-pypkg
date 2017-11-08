#!/usr/bin/env python
import os
import shutil
import stat


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_readonly(remove, path, _):
    os.chmod(path, stat.S_IWRITE)
    remove(path)


def remove_dir(path):
    path = os.path.join(PROJECT_DIRECTORY, path)

    if not os.path.isdir(path):
        raise ValueError('{} is not a directory'.format(path))

    shutil.rmtree(path, onerror=remove_readonly)

    parent = os.path.dirname(path)

    if os.listdir(parent) == []:
        remove_dir(parent)


def remove_file(path):
    path = os.path.join(PROJECT_DIRECTORY, path)

    os.unlink(path)


if __name__ == '__main__':
    if '{{ cookiecutter.build_rpm }}' == 'n':
        remove_dir('packaging/rpm')

    if '{{ cookiecutter.test_runner }}' != 'pytest':
        remove_file('pytest.ini')
