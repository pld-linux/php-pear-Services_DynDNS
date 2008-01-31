%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	DynDNS
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - provides access to the DynDNS web service
Summary(pl.UTF-8):	%{_pearname} - dostęp do usługi WWW DynDNS
Name:		php-pear-%{_pearname}
Version:	0.3.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fc2e81f88ca678a905f3d8c08c6b9e6a
URL:		http://pear.php.net/package/Services_DynDNS/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-common >= 3:4.1.0
Requires:	php-pear-HTTP_Request
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Services_DynDNS provides object-oriented interfaces to the DynDNS REST
API.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Services_DynDNS dostarcza zorientowanego obiektowo interfejsu do API
REST DynDNS.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
