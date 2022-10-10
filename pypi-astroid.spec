#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-astroid
Version  : 2.12.11
Release  : 166
URL      : https://files.pythonhosted.org/packages/23/4e/a6f7eda1ef95b05c71a948dbeda1ea8d299301c260fdf7cb317227e3a539/astroid-2.12.11.tar.gz
Source0  : https://files.pythonhosted.org/packages/23/4e/a6f7eda1ef95b05c71a948dbeda1ea8d299301c260fdf7cb317227e3a539/astroid-2.12.11.tar.gz
Summary  : An abstract syntax tree for Python with inference support.
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: pypi-astroid-license = %{version}-%{release}
Requires: pypi-astroid-python = %{version}-%{release}
Requires: pypi-astroid-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(lazy_object_proxy)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
Astroid
=======
.. image:: https://coveralls.io/repos/github/PyCQA/astroid/badge.svg?branch=main
:target: https://coveralls.io/github/PyCQA/astroid?branch=main
:alt: Coverage badge from coveralls.io

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
Requires: pypi(wrapt)

%description python3
python3 components for the pypi-astroid package.


%prep
%setup -q -n astroid-2.12.11
cd %{_builddir}/astroid-2.12.11
pushd ..
cp -a astroid-2.12.11 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665418060
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . wrapt
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . wrapt
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m unittest discover -s astroid/tests -p "unittest*.py" || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-astroid
cp %{_builddir}/astroid-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-astroid/83baf0020e7e2a77169bbf1111f5f9fcb418abca || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} wrapt
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
