Name:		python-Pebble
Version:	5.1.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pebble/pebble-%{version}.tar.gz
Summary:	Threading and multiprocessing eye-candy.
URL:		https://pypi.org/project/Pebble/
License:	LGPL
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
Threading and multiprocessing eye-candy.

%files
%{py_puresitedir}/Pebble*.*-info
%{py_puresitedir}/pebble
