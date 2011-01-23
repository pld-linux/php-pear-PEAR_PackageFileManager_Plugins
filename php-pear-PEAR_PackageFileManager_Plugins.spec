%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	PEAR_PackageFileManager_Plugins
Summary:	Plugins for PEAR_PackageFileManager to pick up what files to use
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4e9136999ee1f70b1e49d1cf96f50f92
URL:		http://pear.php.net/package/PEAR_PackageFileManager_Plugins/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	php-pear-PEAR >= 1:1.8.0-0.alpha1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.571
Requires:	php-pear
Requires:	php-pear-PEAR_PackageFileManager >= 1.7.0
Requires:	php-pear-XML_Serializer >= 0.18.0
Suggests:	php-simplexml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The plugins for PEAR_PackageFileManager to pick up what files to use.
Supported are:
- File
- CVS
- SVN
- Perforce

This package is to be used with PackageFileManager v1 and v2 and can't
be used on it's own.

In PEAR status of this package is: %{_status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/PEAR_PackageFileManager_Plugins/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PEAR/PackageFileManager/*.php
