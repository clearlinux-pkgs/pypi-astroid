#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-astroid
Version  : 2.9.3
Release  : 141
URL      : https://files.pythonhosted.org/packages/2d/be/33923f5dee9f7119abbaa688833b0c71c2ef4b66af3b06ffc64fc8c341ae/astroid-2.9.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/2d/be/33923f5dee9f7119abbaa688833b0c71c2ef4b66af3b06ffc64fc8c341ae/astroid-2.9.3.tar.gz
Summary  : An abstract syntax tree for Python with inference support.
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: pypi-astroid-license = %{version}-%{release}
Requires: pypi-astroid-python = %{version}-%{release}
Requires: pypi-astroid-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(lazy_object_proxy)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wrapt)

%description
No detailed description available

%package license
Summary: license components for the pypi-astroid package.
Group: Default

%description license
license components for the pypi-astroid package.


%package python
Summary: python components for the pypi-astroid package.
Group: Default
Requires: pypi-astroid-python3 = %{version}-%{release}

%description python
python components for the pypi-astroid package.


%package python3
Summary: python3 components for the pypi-astroid package.
Group: Default
Requires: python3-core
Provides: pypi(astroid)
Requires: pypi(lazy_object_proxy)
Requires: pypi(setuptools)
Requires: pypi(wrapt)

%description python3
python3 components for the pypi-astroid package.


%prep
%setup -q -n astroid-2.9.3
cd %{_builddir}/astroid-2.9.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642003160
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m unittest discover -s astroid/tests -p "unittest*.py" || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-astroid
cp %{_builddir}/astroid-2.9.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-astroid/83baf0020e7e2a77169bbf1111f5f9fcb418abca
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-astroid/83baf0020e7e2a77169bbf1111f5f9fcb418abca

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
