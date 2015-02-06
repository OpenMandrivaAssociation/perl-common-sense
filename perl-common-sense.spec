%define upstream_name    common-sense
%define upstream_version 3.73

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Save a tree AND a kitten, use common::sense!
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/common/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP
BuildArch:	noarch

Provides:	perl(common::sense)

%description
This module implements some sane defaults for Perl programs, as defined by
two typical (or not so typical - use your common sense) specimens of Perl
coders.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
