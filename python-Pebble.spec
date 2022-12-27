Name:		python-Pebble
Version:	5.0.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/P/Pebble/Pebble-%{version}.tar.gz
Summary:	Threading and multiprocessing eye-candy.
URL:		https://pypi.org/project/Pebble/
License:	LGPL
Group:		Development/Python
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
Threading and multiprocessing eye-candy.

%prep
%autosetup -p1 -n Pebble-%{version}

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}

%files
%{py_puresitedir}/Pebble*.*-info
%{py_puresitedir}/pebble
