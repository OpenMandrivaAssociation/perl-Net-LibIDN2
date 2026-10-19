%define	module Net-LibIDN2

Summary:	Perl bindings for GNU Libidn2
Name:		perl-%{module}
Version:	1.02
Release:	1
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/release/Net-LibIDN2
Source0:	https://cpan.metacpan.org/authors/id/T/TH/THOR/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Devel::CheckLib)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(ExtUtils::ParseXS)
BuildRequires:	pkgconfig(libidn2)

%description
Net::LibIDN2 is a Perl interface to GNU Libidn2, which implements
IDNA2008 and Punycode.

%prep
%autosetup -n %{module}-%{version}
# Prefer the packaged Devel::CheckLib over the bundled copy.
sed -i -e "/^use lib 'inc';$/d" Build.PL
sed -i -e '/^inc\/Devel\/CheckLib\.pm$/d' MANIFEST
sed -i -e "s|extra_compiler_flags => ''|extra_compiler_flags => '%{optflags}'|" Build.PL
sed -i -e "s|extra_linker_flags   => '-lidn2'|extra_linker_flags => '-lidn2 %{optflags}'|" Build.PL
rm -rf inc

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
find %{buildroot} -type d -empty -delete

%check
./Build test

%files
%doc README Changes
%license LICENSE
%{perl_vendorarch}/Net
%{perl_vendorarch}/auto/Net
%{_mandir}/man3/*
