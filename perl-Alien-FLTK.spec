# FIXME: arch-dependent config.json in %{perl_vendorlib}/auto/share/dist
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Alien
%define		pnam	FLTK
Summary:	Alien::FLTK - use the stable 1.3.x branch of the Fast Light Toolkit
Summary(pl.UTF-8):	Alien::FLTK - korzystanie ze stabilnej gałęzi 1.3.x biblioteki Fast Light Toolkit
Name:		perl-Alien-FLTK
Version:	1.3.5
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Alien/%{pdir}-%{pnam}-v%{version}.tar.gz
# Source0-md5:	e5147c8b59040cb0b45b85776138439b
Patch0:		%{name}-system-fltk.patch
URL:		https://metacpan.org/release/Alien-FLTK
BuildRequires:	perl-Module-Build-Tiny >= 0.035
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl-Archive-Extract
BuildRequires:	perl-Devel-CheckBin
BuildRequires:	perl-ExtUtils-Config >= 0.003
BuildRequires:	perl-ExtUtils-Helpers >= 0.020
BuildRequires:	perl-ExtUtils-InstallPaths >= 0.002
BuildRequires:	perl-File-ShareDir >= 1.00
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-File-pushd
BuildRequires:	perl-JSON-Tiny
%endif
Requires:	fltk >= 1.3.5
# see comment on top
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution brings libraries for the (stable) 1.3.x branch of
the FLTK GUI toolkit.

%description -l pl.UTF-8
Ten pakiet udostępnia biblioteki ze stabilnej gałęzi 1.3.x toolkitu
graficznego FLTK.

%prep
%setup -q -n %{pdir}-%{pnam}-v%{version}
%patch0 -p1

%build
%{__perl} Build.PL \
	--perl=%{__perl} \
	--installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	--destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p examples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorlib}/Alien/FLTK.pm
%{perl_vendorlib}/auto/share/dist/Alien-FLTK
%{_mandir}/man3/Alien::FLTK.3pm*
%{_examplesdir}/%{name}-%{version}
