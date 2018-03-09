%global srcname {{ cookiecutter.project_slug }}
%global sum {{ cookiecutter.project_short_description }}
Name:           python-{{ cookiecutter.project_slug }}
Version:        {{ cookiecutter.version }}
Release:        0
Summary:        {{ cookiecutter.project_short_description }}
License:        {{ cookiecutter.license }}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python2-devel python3-devel
AutoReq:        0
Requires:       python
URL:            {{ cookiecutter.project_url }}
Source0:        {{ cookiecutter.rpm_sources_url }}/%{srcname}-%{version}.tar.gz
# Turn off the brp-python-bytecompile script
# We don't want to generate bytecode from python and pyo/pyc files
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%description
{{ cookiecutter.project_short_description }}

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
{{ cookiecutter.project_short_description }}


%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
{{ cookiecutter.project_short_description }}


%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
# If, however, we're installing separate executables for python2 and python3,
# the order needs to be reversed so the unversioned executable is the python2 one.
%py2_install
%py3_install

%check
%{__python2} setup.py -m {{ cookiecutter.test_runner }}
%{__python3} setup.py -m {{ cookiecutter.test_runner }}

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python2-%{srcname}
%license COPYING
%doc README.rst
%{python2_sitelib}/*

%files -n python3-%{srcname}
%license COPYING
%doc README.rst
%{python3_sitelib}/*
%{_bindir}/%{srcname}

%changelog
