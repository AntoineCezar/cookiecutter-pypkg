#!/bin/bash

#
# This script create RPM using python setuptools
#



# Common Functions 

function usage () {
	cat <<EOF
SYNOPSIS
	${0##*/} [Python version] [-h|--help]

DESCRIPTION
	This script create RPM using python setuptools
COMMAND LINE OPTIONS
	-h|--help	print this help
	Python version	is the target python version, by default current system version ($(python -V 2>&1 | sed -r "s/[^[:space:]]*[[:space:]]([0-9]+(\.[0-9])?).*/\1/"))
EOF

}


# Main
if [[ "$1" =~ (-h|--help) ]]; then
	usage
elif [[ "$1" =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
	PYTHON_VERSION="$1"
	target_version="--target_version='$PYTHON_VERSION.0'"
elif [ "$1" == "" ]; then
	target_version=""
else
	echo "ERROR: $1 invalid argument"
	usage
	exit 1

fi

		

cmd='python setup.py bdist_rpm \
	--name="{{ cookiecutter.package_name }}" \
	--description="{{ cookiecutter.project_short_description }}" \
	--version="{{ cookiecutter.version }}"\
	--author="{{ cookiecutter.author }}" \
	--author_email="{{ cookiecutter.email }}" \
	--licence="{{ cookiecutter.license }}" \
	--url="{{ cookiecutter.project_url }}" \
	--long_description="{{ cookiecutter.project_description }}" \
	--release="0" \
	--group="System Environment/Base" \
	--packager="{{ cookiecutter.author }} <{{ cookiecutter.email }}>" \
	--provides="{{ cookiecutter.package_name }}" \
	--requires="python" \
	$target_version'

echo " Running Command : $cmd"

$cmd
	

	

