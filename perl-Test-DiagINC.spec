#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-DiagINC
Version  : 0.010
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-DiagINC-0.010.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-DiagINC-0.010.tar.gz
Summary  : 'List modules and versions loaded if tests fail'
Group    : Development/Tools
License  : Apache-2.0
Requires: perl-Test-DiagINC-license = %{version}-%{release}
Requires: perl-Test-DiagINC-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Capture::Tiny)

%description
NAME
Test::DiagINC - List modules and versions loaded if tests fail
VERSION
version 0.010

%package dev
Summary: dev components for the perl-Test-DiagINC package.
Group: Development
Provides: perl-Test-DiagINC-devel = %{version}-%{release}
Requires: perl-Test-DiagINC = %{version}-%{release}

%description dev
dev components for the perl-Test-DiagINC package.


%package license
Summary: license components for the perl-Test-DiagINC package.
Group: Default

%description license
license components for the perl-Test-DiagINC package.


%package perl
Summary: perl components for the perl-Test-DiagINC package.
Group: Default
Requires: perl-Test-DiagINC = %{version}-%{release}

%description perl
perl components for the perl-Test-DiagINC package.


%prep
%setup -q -n Test-DiagINC-0.010
cd %{_builddir}/Test-DiagINC-0.010

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-DiagINC
cp %{_builddir}/Test-DiagINC-0.010/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-DiagINC/85e14080c483146fd022a7140831a977f7eeaac8
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::DiagINC.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-DiagINC/85e14080c483146fd022a7140831a977f7eeaac8

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
