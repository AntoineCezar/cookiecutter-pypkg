Summary: {{ cookiecutter.project_short_description }}
Name: {{ cookiecutter.project_name }}
Version: {{ cookiecutter.version }}
Release: 0
Copyright: {{ cookiecutter.license }}
Group: System Environment/Base
Source: {{ cookiecutter.project_url }}
BuildRoot: /var/tmp/%{name}-buildroot
Requires: python
BuildRequires: python2-dev python3-dev py-setuptools
Provides: {{ cookiecutter.package_name }}


%description
{{ cookiecutter.project_description }}

%prep

%build
python2 setup.py build
python3 setup.py build

%install py2
mkdir -p $RPM_BUILD_ROOT/%{_usr}
python2 setup.py install --prefix=%{_usr} --root="$RPM_BUILD_ROOT" --skip-build

%files py2
%defattr(-,root,root)
%{_usr}/lib/python2*

%install py3
mkdir -p $RPM_BUILD_ROOT/%{_usr}
python3 setup.py install --prefix=%{_usr} --root="$RPM_BUILD_ROOT" --skip-build

%files py3
%defattr(-,root,root)
%{_usr}/lib/python3*


%clean
rm -rf $RPM_BUILD_ROOT

%changelog

