#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-astroid
Version  : 2.15.4
Release  : 184
URL      : https://files.pythonhosted.org/packages/36/50/c2bde258f4b8021ee9075932ace925245a1ad9a816a0cab269f04f480c3b/astroid-2.15.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/36/50/c2bde258f4b8021ee9075932ace925245a1ad9a816a0cab269f04f480c3b/astroid-2.15.4.tar.gz
Summary  : An abstract syntax tree for Python with inference support.
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: pypi-astroid-license = %{version}-%{release}
Requires: pypi-astroid-python = %{version}-%{release}
Requires: pypi-astroid-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Astroid
=======
.. image:: https://codecov.io/gh/PyCQA/astroid/branch/main/graph/badge.svg?token=Buxy4WptLb
:target: https://codecov.io/gh/PyCQA/astroid
:alt: Coverage badge from codecov

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
%setup -q -n astroid-2.15.4
cd %{_builddir}/astroid-2.15.4
pushd ..
cp -a astroid-2.15.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682349915
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . wrapt
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
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
