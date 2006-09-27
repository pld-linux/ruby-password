Summary:	Ruby password manipulation library
Name:		ruby-password
Version:	0.5.3
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.caliban.org/files/ruby/%{name}-%{version}.tar.gz
# Source0-md5:	b4304bab359bdc95bc7f0938b0db4bed
Patch0:	%{name}-dictlocation.patch
URL:		http://www.caliban.org/ruby/ruby-password.shtml
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	cracklib-dicts
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby/Password is a suite of password handling methods for Ruby. It supports the manual entry of passwords from the keyboard in both buffered and unbuffered modes, password strength checking, random password generation, phonemic password generation (for easy memorisation by human-beings) and the encryption of passwords.

%prep
%setup -q
%patch0 -p1

%build
ruby extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

rdoc -o rdoc/ --main README README lib/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_bindir}}

%{__make} install \
  archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitelibdir=$RPM_BUILD_ROOT%{ruby_rubylibdir} \
	rubylibdir=$RPM_BUILD_ROOT%{ruby_rubylibdir}

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%attr(755,root,root) %{ruby_archdir}/*.so
%{ruby_rubylibdir}/password.rb
%{ruby_ridir}/Password
