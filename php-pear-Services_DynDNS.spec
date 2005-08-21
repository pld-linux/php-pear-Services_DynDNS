%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	DynDNS
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides access to the DynDNS web service
Summary(pl):	%{_pearname} - dostêp do serwisów DynDNS
Name:		php-pear-%{_pearname}
Version:	0.3.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fc2e81f88ca678a905f3d8c08c6b9e6a
URL:		http://pear.php.net/package/Services_DynDNS/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Services_DynDNS provides object-oriented interfaces to the DynDNS REST
API.

In PEAR status of this package is: %{_status}.

%description -l pl
Services_DynDNS dostarcza zorientowanego obiektowo interfejsu do API
REST DynDNS.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Request

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Request/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Request

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
