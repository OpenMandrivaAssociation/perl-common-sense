%define upstream_name    common-sense
%define upstream_version 3.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Save a tree AND a kitten, use common::sense!
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/common/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
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

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 3.300.0-2mdv2011.0
+ Revision: 658559
- rebuild for updated spec-helper

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 3.300.0-1mdv2011.0
+ Revision: 551212
- update to 3.3

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 3.200.0-1mdv2010.1
+ Revision: 536219
- update to 3.2

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 3.100.0-1mdv2010.1
+ Revision: 532162
- update to 3.1

* Tue Dec 15 2009 Jérôme Quelin <jquelin@mandriva.org> 3.0.0-1mdv2010.1
+ Revision: 478793
- update to 3.0

* Fri Dec 04 2009 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 473274
- update to 2.03

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 2.20.0-1mdv2010.1
+ Revision: 460778
- update to 2.02

* Thu Sep 03 2009 Jérôme Quelin <jquelin@mandriva.org> 2.0.0-1mdv2010.0
+ Revision: 427478
- update to 2.0

* Mon Aug 24 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 420262
- update to 1.0

* Thu Aug 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 410630
- update to 0.04

* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 398908
- import perl-common-sense


* Thu Jul 23 2009 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist
