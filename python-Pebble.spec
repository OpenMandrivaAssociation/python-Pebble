%define module Pebble
%define oname pebble

Name:		python-Pebble
Version:	5.2.1
Release:	1
Summary:	Threading and multiprocessing eye-candy.
License:	LGPL
Group:		Development/Python
URL:		https://pypi.org/project/Pebble/
Source0:	https://files.pythonhosted.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(setuptools)

%description
Threading and multiprocessing eye-candy.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{module}-%{version}*.*-info
