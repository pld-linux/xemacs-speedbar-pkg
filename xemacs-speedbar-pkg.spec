Summary:	Provides a seperate frame with convenient references
Summary(pl):	Speedbar - oddzielna ramka z wygodnymi odno¶nikami
Name:		xemacs-speedbar-pkg
%define 	srcname	speedbar
Version:	1.24
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
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

%description -l pl
Speedbar dodaje ramkê, w której s± wy¶wietlane pliki i miejsca w
plikach. Te rzeczy mog± byæ klikniête przy u¿yciu mouse-2, aby
ostatnia aktywna ramka wy¶wietla³a to miejsce pliku.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/speedbar/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
