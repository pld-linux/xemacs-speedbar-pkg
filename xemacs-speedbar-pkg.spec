Summary:	Provides a seperate frame with convenient references
Summary(pl.UTF-8):	Speedbar - oddzielna ramka z wygodnymi odnośnikami
Name:		xemacs-speedbar-pkg
%define 	srcname	speedbar
Version:	1.27
Release:	2
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	4df8d109364493dca814ef7429d560d2
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The speedbar provides a frame in which files, and locations in files
are displayed. These items can be clicked on with mouse-2 in order to
make the last active frame display that file location.

%description -l pl.UTF-8
Speedbar dodaje ramkę, w której są wyświetlane pliki i miejsca w
plikach. Te rzeczy mogą być kliknięte przy użyciu mouse-2, aby
ostatnia aktywna ramka wyświetlała to miejsce pliku.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/speedbar/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
